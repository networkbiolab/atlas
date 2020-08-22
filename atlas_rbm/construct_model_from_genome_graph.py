# -*- coding: utf-8 -*-

'''
Project "Reconstruction of RBM from biological networks", Rodrigo Santibáñez, 2019-2020 @ NBL, UMayor
Citation:
DOI:
'''

__author__  = 'Rodrigo Santibáñez'
__license__ = 'gpl-3.0'

from pysb import *
from pysb.util import *
from pysb.core import *

import re
import numpy
import pandas

from .utils import location_keys, location_values

def read_network(infile_path):
	with open(infile_path, 'r') as infile:
		data = pandas.read_csv(infile, delimiter = '\t', header = 0, comment = '#')

	return data

def check_genome_graph(data):
	# find duplicated reactions (reactions must has a unique name)
	duplicated = len(data[data.duplicated(['UPSTREAM', 'DOWNSTREAM'])].index)

	if duplicated > 0:
		data[data.duplicated(['UPSTREAM', 'DOWNSTREAM'])].to_csv('./conflicting_interactions.txt', sep = '\t', index = False)
		data = data[~data.duplicated(['UPSTREAM', 'DOWNSTREAM'], keep = 'first')]
		print('It was found possible duplicated interactions in the network.\n' \
			'Please check the conflicting_interactions.txt and correct them if necessary.')

	return data

def monomers_from_genome_graph(model, data, verbose = False, toFile = False):
	# find DNA parts
	architecture = list(data['UPSTREAM']) + [data['DOWNSTREAM'].iloc[-1]]

	names = []
	types = []
	for dna_part in architecture:
		dna_part = dna_part.replace('[', '').replace(']', '')
		if 'BS' in dna_part:
			names.append('_'.join(
				[dna_part.split('-')[0],
				dna_part.split('-')[2],
				dna_part.split('-')[3]]))
		else:
			names.append(dna_part.split('-')[0])
		types.append(dna_part.split('-')[1])

	# dna
	code = "Monomer('dna',\n" \
		"	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],\n" \
		"	{{ 'name' : [{:s}],\n" \
		"	'type' : [{:s}],\n" \
		"	'loc' : ['cyt']}})\n"

	code = code.format(
		', '.join([ '\'' + x + '\'' for x in sorted(set(names))]),
		', '.join([ '\'' + x + '\'' for x in sorted(set(types + ['BS']))]))

	if verbose:
		print(code)
	if toFile:
		with open(toFile, 'a+') as outfile:
			outfile.write(code)
	else:
		exec(code.replace('\n', ''))

	# rna
	code = "Monomer('rna',\n" \
		"	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],\n" \
		"	{{ 'name' : [{:s}],\n" \
		"	'type' : [{:s}],\n" \
		"	'loc' : ['cyt']}})\n"

	code = code.format(
		', '.join([ '\'' + x + '\'' for x in sorted(set(names))]),
		', '.join([ '\'' + x + '\'' for x in sorted(set(types + ['BS']))]))

	if verbose:
		print(code)
	if toFile:
		with open(toFile, 'a+') as outfile:
			outfile.write(code)
	else:
		exec(code.replace('\n', ''))

	# prot
	code = "Monomer('prot',\n" \
		"	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],\n" \
		"	{{ 'name' : [{:s}],\n" \
		"	'loc' : ['cyt', 'mem']}})\n"
	names = [ x for x in names if not x.startswith('BS') ]
	code = code.format(', '.join([ '\'' + x + '\'' for x in sorted(set(names))]))

	if verbose:
		print(code)
	if toFile:
		with open(toFile, 'a+') as outfile:
			outfile.write(code)
	else:
		exec(code.replace('\n', ''))

	# complexes
	code = "Monomer('cplx',\n" \
		"	['name', 'loc', 'dna', 'met', 'prot', 'rna'],\n" \
		"	{ 'name' : ['RNAP_CPLX', 'RIBOSOME_CPLX'],\n" \
		"	'loc' : ['cyt']})\n"

	if verbose:
		print(code)
	if toFile:
		with open(toFile, 'a+') as outfile:
			outfile.write(code)
	else:
		exec(code.replace('\n', ''))

def polymerase_docking_rules(model, data, verbose = False, toFile = False):
	architecture = list(data['UPSTREAM']) + [data['DOWNSTREAM'].iloc[-1]]

	for idx, dna_part in enumerate(architecture):
		if 'pro' in dna_part: # docking rules
			name = dna_part.split('-')[0]
			type = dna_part.split('-')[1]

			code = 'Rule(\'docking_{:s}\',\n' \
				'	cplx(name = \'RNAP-CPLX\', dna = None) +\n' \
				'	dna(name = \'{:s}\', type = \'{:s}\', prot = None) |\n' \
				'	cplx(name = \'RNAP-CPLX\', dna = 1) %\n' \
				'	dna(name = \'{:s}\', type = \'{:s}\', prot = 1),\n' \
				'	Parameter(\'fwd_docking_{:s}\', {:f}),\n' \
				'	Parameter(\'rvs_docking_{:s}\', {:f}))\n'
			code = code.format(
					dna_part, name, type, name, type,
					dna_part, float(data['RNAP_FWD_DOCK_RATE'].iloc[idx]),
					dna_part, float(data['RNAP_RVS_DOCK_RATE'].iloc[idx]))

			code = code.replace('-', '_').replace('[', '').replace(']', '')
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code)

def polymerase_sliding_rules(model, data, verbose = False, toFile = False):
	for idx, (dna_part1, dna_part2) in enumerate(zip(data['UPSTREAM'], data['DOWNSTREAM'])):
		dna_part1, dna_part2 = (dna_part1, dna_part2)
		name1 = dna_part1.split('-')[0]
		type1 = dna_part1.split('-')[1]
		name2 = dna_part2.split('-')[0]
		type2 = dna_part2.split('-')[1]

		if 'BS' in dna_part1:  # catch binding sites to add to sliding rules
			name1 = '_'.join(
				[dna_part1.split('-')[0],
				dna_part1.split('-')[2],
				dna_part1.split('-')[3]])
			type1 = dna_part1.split('-')[0]
		elif 'BS' in dna_part2:
			name2 = '_'.join(
				[dna_part2.split('-')[0],
				dna_part2.split('-')[2],
				dna_part2.split('-')[3]])
			type2 = dna_part2.split('-')[0]

		code = 'Rule(\'sliding_{:s}\',\n' \
			'	cplx(name = \'RNAP-CPLX\', dna = 1) %\n' \
			'	dna(name = \'{:s}\', type = \'{:s}\', prot = 1) +\n' \
			'	None +\n' \
			'	dna(name = \'{:s}\', type = \'{:s}\', prot = None) >>\n' \
			'	cplx(name = \'RNAP-CPLX\', dna = 1) %\n' \
			'	dna(name = \'{:s}\', type = \'{:s}\', prot = 1) +\n' \
			'	rna(name = \'{:s}\', type = \'{:s}\', prot = None, rna = None) +\n' \
			'	dna(name = \'{:s}\', type = \'{:s}\', prot = None),\n' \
			'	Parameter(\'fwd_sliding_{:s}\', {:f}))\n'
		code = code.format(
			dna_part1, name1, type1, name2, type2, name2, type2, name2, type2, name1, type1,
			dna_part1, float(data['RNAP_FWD_SLIDE_RATE'].iloc[idx]))

		code = code.replace('-', '_').replace('[', '').replace(']', '')
		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code)

def polymerase_falloff_rules(model, data, verbose = False, toFile = False):
	architecture = list(data['UPSTREAM']) + [data['DOWNSTREAM'].iloc[-1]]

	for idx, dna_part in enumerate(architecture):
		if 'ter' in dna_part: # falloff rules
			name = dna_part.split('-')[0]
			type = dna_part.split('-')[1]

			code = 'Rule(\'falloff_{:s}\',\n' \
				'	cplx(name = \'RNAP-CPLX\', dna = 1) %\n' \
				'	dna(name = \'{:s}\', type = \'{:s}\', prot = 1) >>\n' \
				'	cplx(name = \'RNAP-CPLX\', dna = None) +\n' \
				'	dna(name = \'{:s}\', type = \'{:s}\', prot = None),\n' \
				'	Parameter(\'fwd_falloff_{:s}\', {:f}))\n'
			code = code.format(
				dna_part, name, type, name, type,
				dna_part, float(data['RNAP_FWD_FALL_RATE'].iloc[idx-1]))

			code = code.replace('-', '_').replace('[', '').replace(']', '')
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code)

def ribosome_docking_rules(model, data, verbose = False, toFile = False):
	architecture = list(data['UPSTREAM']) + [data['DOWNSTREAM'].iloc[-1]]

	for idx, dna_part in enumerate(architecture):
		if 'rbs' in dna_part: # docking rules
			name = dna_part.split('-')[0]
			type = dna_part.split('-')[1]

			code = 'Rule(\'dr_{:s}\',\n' \
				'	cplx(name = \'RIBOSOME-CPLX\', rna = None) +\n' \
				'	rna(name = \'{:s}\', type = \'{:s}\', prot = None) |\n' \
				'	cplx(name = \'RIBOSOME-CPLX\', rna = 1) %\n' \
				'	rna(name = \'{:s}\', type = \'{:s}\', prot = 1),\n' \
				'	Parameter(\'fwd_dr_{:s}\', {:f}),\n' \
				'	Parameter(\'rvs_dr_{:s}\', {:f}))\n'
			code = code.format(
				dna_part, name, type, name, type,
				dna_part, float(data['RIB_FWD_DOCK_RATE'].iloc[idx]),
				dna_part, float(data['RIB_RVS_DOCK_RATE'].iloc[idx]))

			code = code.replace('-', '_').replace('[', '').replace(']', '')
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code)

def ribosome_sliding_rules(model, data, verbose = False, toFile = False):
	for idx, (dna_part1, dna_part2) in enumerate(zip(data['UPSTREAM'], data['DOWNSTREAM'])):
		dna_part1, dna_part2 = (dna_part1, dna_part2)

		if 'BS' in dna_part1:  # catch binding sites to add to sliding rules
			name1 = '_'.join(
				[dna_part1.split('-')[0],
				dna_part1.split('-')[2],
				dna_part1.split('-')[3]])
			type1 = dna_part1.split('-')[0]
		elif 'BS' in dna_part2:
			name2 = '_'.join(
				[dna_part2.split('-')[0],
				dna_part2.split('-')[2],
				dna_part2.split('-')[3]])
			type2 = dna_part2.split('-')[0]
		else:
			name1 = dna_part1.split('-')[0]
			type1 = dna_part1.split('-')[1]
			name2 = dna_part2.split('-')[0]
			type2 = dna_part2.split('-')[1]

		if 'pro' in type1: # slide from the first CDS
			forward = False
		if 'rbs' in type1:
			forward = True

		if forward:
			if 'cds' in type2:
				code = 'Rule(\'sr_{:s}\',\n' \
					'	cplx(name = \'RIBOSOME-CPLX\', rna = 1) %\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = 1) +\n' \
					'	None +\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = None) >> \n' \
					'	cplx(name = \'RIBOSOME-CPLX\', rna = 1) %\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = 1) +\n' \
					'	prot(name = \'{:s}\', loc = \'cyt\', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = None),\n' \
					'	Parameter(\'fwd_sr_{:s}\', {:f}))\n'
				code = code.format(
					dna_part1, name1, type1, name2, type2, name2, type2, name2, name2, type2,
					dna_part1, float(data['RIB_FWD_SLIDE_RATE'].iloc[idx]))

			else: # sliding without protein synthesis
				code = 'Rule(\'sr_{:s}\',\n' \
					'	cplx(name = \'RIBOSOME-CPLX\', rna = 1) %\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = 1) +\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = None) >>\n' \
					'	cplx(name = \'RIBOSOME-CPLX\', rna = 1) %\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = 1) +\n' \
					'	rna(name = \'{:s}\', type = \'{:s}\', prot = None),\n' \
					'	Parameter(\'fwd_sr_{:s}\', {:f}))\n'
				code = code.format(
					dna_part1, name1, type1, name2, type2, name2, type2, name1, type1,
					dna_part1, float(data['RIB_FWD_SLIDE_RATE'].iloc[idx]))

			code = code.replace('-', '_').replace('[', '').replace(']', '')
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code)

def ribosome_falloff_rules(model, data, verbose = False, toFile = False):
	architecture = list(data['UPSTREAM']) + [data['DOWNSTREAM'].iloc[-1]]

	for idx, dna_part in enumerate(architecture):
		if 'ter' in dna_part: # falloff rules
			name = dna_part.split('-')[0]
			type = dna_part.split('-')[1]

			code = 'Rule(\'fr_{:s}\',\n' \
				'	cplx(name = \'RIBOSOME-CPLX\', rna = 1) %\n' \
				'	rna(name = \'{:s}\', type = \'{:s}\', prot = 1) >>\n' \
				'	cplx(name = \'RIBOSOME-CPLX\', rna = None) +\n' \
				'	rna(name = \'{:s}\', type = \'{:s}\', prot = None),\n' \
				'	Parameter(\'fwd_fr_{:s}\', 0))\n'
			code = code.format(
				dna_part, name, type, name, type,
				dna_part, float(data['RIB_FWD_FALL_RATE'].iloc[idx-1]))

			code = code.replace('-', '_').replace('[', '').replace(']', '')
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code)

def observables_from_genome_graph(model, data, verbose = False, toFile = False):
	architecture = data['UPSTREAM'] + ',' + data['DOWNSTREAM']
	operons = []
	for dna_part in architecture:
		if dna_part.startswith('['):
			operon = []
			operon.append(dna_part.split(',')[0][1:])
		elif dna_part.endswith(']'):
			operon.append(dna_part.split(',')[0])
			operon.append(dna_part.split(',')[1][:-1])
			operons.append(','.join(operon))
		else:
			operon.append(dna_part.split(',')[0])

	# prots
	for operon in list(set(operons)):
		names = [(m.start(0), m.end(0)) for m in re.finditer(r'\w+-cds\d?', operon)]

		prots = []
		for lst in names:
			prots.append(operon[lst[0]:lst[1]].split('-')[0])

		for name in prots:
			code = 'Initial(prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None),\n' \
			'	Parameter(\'t0_prot_{:s}_{:s}\', 0))\n'
			code = code.format(name, 'cyt', name, 'cyt')

			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ' ').replace('\n', ' '))

			code = 'Observable(\'obs_prot_{:s}_{:s}\',\n' \
				'	prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None))\n'
			code = code.format(name, 'cyt', name, 'cyt')

			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ''))

		operon_name = ''.join(prots)

		# dnas
		## create link indexes
		dw = [None] * len(operon.split(','))
		start_link = 1
		for index in range(len(operon.split(','))-1):
			dw[index] = start_link
			start_link += 1
		up = dw[-1:] + dw[:-1]

		complex_pysb = []
		for index, monomer in enumerate(operon.split(',')):
			complex_pysb.append('dna(name = \'{:s}\', type = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {:s}, dw = {:s})'.format(
				monomer.split('-')[0], monomer.split('-')[1], 'cyt', str(up[index]), str(dw[index])))

		complex_pysb = ' %\n	'.join(complex_pysb)

		code = 'Initial({:s},\n' \
			'	Parameter(\'t0_dna_{:s}\', 0))\n'
		code = code.format(complex_pysb, operon_name)

		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code.replace('\t', ' ').replace('\n', ' '))

		code = 'Observable(\'obs_dna_{:s}\',\n' \
			'	{:s})\n'
		code = code.format(operon_name, complex_pysb)

		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code.replace('\t', ' ').replace('\n', ' '))

		# rnas start at any promoter and ends at any terminator
		rna_forms = []
		a = [(m.start(0), m.end(0)) for m in re.finditer(r'\w+-pro\d?', operon)]
		b = [(m.start(0), m.end(0)) for m in re.finditer(r'\w+-ter\d?', operon)]
		for lst in itertools.product(a, b):
			rna_forms.append(operon[lst[0][0]:lst[1][1]].split(','))

		for idx, rna_form in enumerate(rna_forms):
			## create link indexes
			dw = [None] * (len(rna_form)-1)
			start_link = 1
			for index in range(len(rna_form)-2):
				dw[index] = start_link
				start_link += 1
			up = dw[-1:] + dw[:-1]

			complex_pysb = []
			for index, monomer in enumerate(rna_form[1:]):
				complex_pysb.append('rna(name = \'{:s}\', type = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {:s}, dw = {:s})'.format(
					monomer.split('-')[0], monomer.split('-')[1], 'cyt', str(up[index]), str(dw[index])))

			complex_pysb = ' %\n	'.join(complex_pysb)

			code = 'Initial({:s},\n' \
				'	Parameter(\'t0_rna_{:s}_form{:d}\', 0))\n'
			code = code.format(complex_pysb, operon_name, idx+1)

			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ' ').replace('\n', ' '))

			code = 'Observable(\'obs_rna_{:s}_form{:d}\',\n' \
				'	{:s})\n'
			code = code.format(operon_name, idx+1, complex_pysb)

			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ' ').replace('\n', ' '))

def construct_model_from_genome_graph(network, verbose = False, toFile = False):
	if toFile:
		with open(toFile, 'w') as outfile:
			outfile.write('from pysb import *\nModel()\n\n')

	if isinstance(network, str):
		data = read_network(network)
	elif isinstance(network, pandas.DataFrame):
		data = network
	elif isinstance(network, numpy.array):
		data = pandas.DataFrame(data = network)
	else:
		raise Exception("The network format is not yet supported.")
	data = check_genome_graph(data)

	model = Model()
	monomers_from_genome_graph(model, data, verbose, toFile)

	# write docking, slide, and falloff of RNA Polymerase from DNA
	polymerase_docking_rules(model, data, verbose, toFile)
	polymerase_sliding_rules(model, data, verbose, toFile)
	polymerase_falloff_rules(model, data, verbose, toFile)

	# write docking, slide, and falloff of RIBOSOME-CPLX from RNA
	ribosome_docking_rules(model, data, verbose, toFile)
	ribosome_sliding_rules(model, data, verbose, toFile)
	ribosome_falloff_rules(model, data, verbose, toFile)

	# TODO
	# write docking, slide, and falloff of RNASE-CPLX from RNA
	# write docking, slide, and falloff of PROTEASE-CPLX from protein
	observables_from_genome_graph(model, data, verbose, toFile)

	return model
