from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'ACETYL_COA', 'ALLOLACTOSE', 'Alpha_lactose', 'Beta_D_Galactosides', 'CO_A', 'CPD_15972', 'CPD_3561', 'CPD_3785', 'CPD_3801', 'D_ARABINOSE', 'Fructofuranose', 'GALACTOSE', 'Glucopyranose', 'MELIBIOSE', 'PROTON', 'WATER', '_6_Acetyl_Beta_D_Galactosides' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'lacA', 'lacY', 'lacZ' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Observable('obs_met_ACETYL_COA_cyt', met(name = 'ACETYL_COA', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_ALLOLACTOSE_cyt', met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_Alpha_lactose_cyt', met(name = 'Alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_Beta_D_Galactosides_cyt', met(name = 'Beta_D_Galactosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_CO_A_cyt', met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_CPD_15972_cyt', met(name = 'CPD_15972', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_CPD_3561_cyt', met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_CPD_3785_cyt', met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_CPD_3801_cyt', met(name = 'CPD_3801', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_D_ARABINOSE_cyt', met(name = 'D_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_Fructofuranose_cyt', met(name = 'Fructofuranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_GALACTOSE_cyt', met(name = 'GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_Glucopyranose_cyt', met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_MELIBIOSE_cyt', met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_PROTON_cyt', met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met_WATER_cyt', met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Observable('obs_met__6_Acetyl_Beta_D_Galactosides_cyt', met(name = '_6_Acetyl_Beta_D_Galactosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Initial(met(name = 'ACETYL_COA', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_ACETYL_COA_cyt', 0))
Initial(met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_ALLOLACTOSE_cyt', 0))
Initial(met(name = 'Alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_Alpha_lactose_cyt', 0))
Initial(met(name = 'Beta_D_Galactosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_Beta_D_Galactosides_cyt', 0))
Initial(met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CO_A_cyt', 0))
Initial(met(name = 'CPD_15972', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_15972_cyt', 0))
Initial(met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_3561_cyt', 0))
Initial(met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_3785_cyt', 0))
Initial(met(name = 'CPD_3801', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_3801_cyt', 0))
Initial(met(name = 'D_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_D_ARABINOSE_cyt', 0))
Initial(met(name = 'Fructofuranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_Fructofuranose_cyt', 0))
Initial(met(name = 'GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_GALACTOSE_cyt', 0))
Initial(met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_Glucopyranose_cyt', 0))
Initial(met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_MELIBIOSE_cyt', 0))
Initial(met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_PROTON_cyt', 0))
Initial(met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_WATER_cyt', 0))
Initial(met(name = '_6_Acetyl_Beta_D_Galactosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met__6_Acetyl_Beta_D_Galactosides_cyt', 0))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_cyt', 0))
Initial(prot(name = 'lacY', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacY_cyt', 0))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_cyt', 0))
Rule('GALACTOACETYLTRAN_RXN',
	prot(name = 'lacA', loc = 'cyt') +
	met(name = 'Beta_D_Galactosides', loc = 'cyt', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', prot = None) | 
	prot(name = 'lacA', loc = 'cyt') +
	met(name = '_6_Acetyl_Beta_D_Galactosides', loc = 'cyt', prot = None) +
	met(name = 'CO_A', loc = 'cyt', prot = None), 
	Parameter('fwd_GALACTOACETYLTRAN_RXN', 1.000000), 
	Parameter('rvs_GALACTOACETYLTRAN_RXN', 0.000000))
Rule('TRANS_RXN_24',
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'per', prot = None) +
	met(name = 'Alpha_lactose', loc = 'per', prot = None) | 
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', prot = None), 
	Parameter('fwd_TRANS_RXN_24', 1.000000), 
	Parameter('rvs_TRANS_RXN_24', 0.000000))
Rule('TRANS_RXN_94',
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'per', prot = None) +
	met(name = 'MELIBIOSE', loc = 'per', prot = None) | 
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_TRANS_RXN_94', 1.000000), 
	Parameter('rvs_TRANS_RXN_94', 0.000000))
Rule('RXN0_7215',
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'per', prot = None) +
	met(name = 'CPD_3561', loc = 'per', prot = None) | 
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3561', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_7215', 1.000000), 
	Parameter('rvs_RXN0_7215', 0.000000))
Rule('RXN0_7217',
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'per', prot = None) +
	met(name = 'CPD_3785', loc = 'per', prot = None) | 
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3785', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_7217', 1.000000), 
	Parameter('rvs_RXN0_7217', 0.000000))
Rule('RXN_17755',
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'per', prot = None) +
	met(name = 'CPD_3801', loc = 'per', prot = None) | 
	prot(name = 'lacY', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3801', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN_17755', 1.000000), 
	Parameter('rvs_RXN_17755', 0.000000))
Rule('BETAGALACTOSID_RXN',
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'CPD_15972', loc = 'cyt', prot = None) +
	met(name = 'WATER', loc = 'cyt', prot = None) | 
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', prot = None), 
	Parameter('fwd_BETAGALACTOSID_RXN', 1.000000), 
	Parameter('rvs_BETAGALACTOSID_RXN', 0.000000))
Rule('RXN0_5363',
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'Alpha_lactose', loc = 'cyt', prot = None) | 
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_5363', 1.000000), 
	Parameter('rvs_RXN0_5363', 1.000000))
Rule('RXN_17726',
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'CPD_3561', loc = 'cyt', prot = None) +
	met(name = 'WATER', loc = 'cyt', prot = None) | 
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', prot = None) +
	met(name = 'Fructofuranose', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN_17726', 1.000000), 
	Parameter('rvs_RXN_17726', 0.000000))
Rule('RXN0_7219',
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'CPD_3785', loc = 'cyt', prot = None) +
	met(name = 'WATER', loc = 'cyt', prot = None) | 
	prot(name = 'lacZ', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', prot = None) +
	met(name = 'D_ARABINOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_7219', 1.000000), 
	Parameter('rvs_RXN0_7219', 0.000000))
