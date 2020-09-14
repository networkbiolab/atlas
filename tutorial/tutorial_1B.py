# exported from PySB model 'atlas_rbm.atlas'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, MultiState, Tag, ANY, WILD

Model()

Monomer('met', ['name', 'loc', 'dna', 'met', 'prot', 'rna'], {'name': ['ACETYL_COA', 'CO_A', 'CPD_3561', 'CPD_3785', 'CPD_3801', 'D_ARABINOSE', 'Fructofuranose', 'MELIBIOSE', 'PROTON', 'WATER', '_6_Acetyl_beta_D_Galactose', 'alpha_ALLOLACTOSE', 'alpha_GALACTOSE', 'alpha_glucose', 'alpha_lactose', 'beta_ALLOLACTOSE', 'beta_GALACTOSE', 'beta_glucose', 'beta_lactose'], 'loc': ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot', ['dna', 'dw', 'loc', 'met', 'name', 'prot', 'rna', 'up'], {'name': ['lacA', 'lacI', 'lacY', 'lacZ', 'spontaneous'], 'loc': ['bnuc', 'cproj', 'cyt', 'cytosk', 'ex', 'imem', 'mem', 'omem', 'per', 'wall']})

Parameter('t0_prot_lacA_cyt', 3.0)
Parameter('t0_prot_lacI_cyt', 0.0)
Parameter('t0_prot_lacZ_cyt', 4.0)
Parameter('t0_cplx_lacAx3_cyt', 0.0)
Parameter('t0_cplx_lacAx2_cyt', 0.0)
Parameter('t0_cplx_lacIx2_cyt', 0.0)
Parameter('t0_cplx_lacZx4_cyt', 0.0)
Parameter('t0_cplx_lacZx2_cyt', 0.0)
Parameter('fwd_PhysicalInteractionRule_1', 1.0)
Parameter('rvs_PhysicalInteractionRule_1', 0.0)
Parameter('fwd_PhysicalInteractionRule_2', 1.0)
Parameter('rvs_PhysicalInteractionRule_2', 0.0)
Parameter('fwd_PhysicalInteractionRule_3', 1.0)
Parameter('rvs_PhysicalInteractionRule_3', 0.0)
Parameter('fwd_PhysicalInteractionRule_4', 1.0)
Parameter('rvs_PhysicalInteractionRule_4', 0.0)
Parameter('fwd_PhysicalInteractionRule_5', 1.0)
Parameter('rvs_PhysicalInteractionRule_5', 0.0)
Parameter('t0_met_ACETYL_COA_cyt', 0.0)
Parameter('t0_met_CO_A_cyt', 0.0)
Parameter('t0_met_CPD_3561_cyt', 0.0)
Parameter('t0_met_CPD_3785_cyt', 0.0)
Parameter('t0_met_CPD_3801_cyt', 0.0)
Parameter('t0_met_D_ARABINOSE_cyt', 0.0)
Parameter('t0_met_Fructofuranose_cyt', 0.0)
Parameter('t0_met_MELIBIOSE_cyt', 0.0)
Parameter('t0_met_PROTON_cyt', 0.0)
Parameter('t0_met_WATER_cyt', 100.0)
Parameter('t0_met__6_Acetyl_beta_D_Galactose_cyt', 0.0)
Parameter('t0_met_alpha_ALLOLACTOSE_cyt', 0.0)
Parameter('t0_met_alpha_GALACTOSE_cyt', 0.0)
Parameter('t0_met_alpha_glucose_cyt', 0.0)
Parameter('t0_met_alpha_lactose_cyt', 0.0)
Parameter('t0_met_beta_ALLOLACTOSE_cyt', 0.0)
Parameter('t0_met_beta_GALACTOSE_cyt', 0.0)
Parameter('t0_met_beta_glucose_cyt', 0.0)
Parameter('t0_met_beta_lactose_cyt', 0.0)
Parameter('t0_prot_lacY_cyt', 0.0)
Parameter('t0_prot_spontaneous_cyt', 0.0)
Parameter('fwd_LACTOSE_MUTAROTATION_CYT', 1.0)
Parameter('rvs_LACTOSE_MUTAROTATION_CYT', 1.0)
Parameter('fwd_GALACTOSE_MUTAROTATION_CYT', 1.0)
Parameter('rvs_GALACTOSE_MUTAROTATION_CYT', 1.0)
Parameter('fwd_GLUCOSE_MUTAROTATION_CYT', 1.0)
Parameter('rvs_GLUCOSE_MUTAROTATION_CYT', 1.0)
Parameter('fwd_TRANS_RXN_24', 1.0)
Parameter('rvs_TRANS_RXN_24', 0.0)
Parameter('fwd_TRANS_RXN_24_beta', 1.0)
Parameter('rvs_TRANS_RXN_24_beta', 0.0)
Parameter('fwd_TRANS_RXN_94', 1.0)
Parameter('rvs_TRANS_RXN_94', 0.0)
Parameter('fwd_RXN0_7215', 1.0)
Parameter('rvs_RXN0_7215', 0.0)
Parameter('fwd_RXN0_7217', 1.0)
Parameter('rvs_RXN0_7217', 0.0)
Parameter('fwd_RXN_17755', 1.0)
Parameter('rvs_RXN_17755', 0.0)
Parameter('fwd_BETAGALACTOSID_RXN', 1.0)
Parameter('rvs_BETAGALACTOSID_RXN', 0.0)
Parameter('fwd_BETAGALACTOSID_RXN_alpha', 1.0)
Parameter('rvs_BETAGALACTOSID_RXN_alpha', 0.0)
Parameter('fwd_RXN0_5363', 1.0)
Parameter('rvs_RXN0_5363', 1.0)
Parameter('fwd_RXN0_5363_beta', 1.0)
Parameter('rvs_RXN0_5363_beta', 1.0)
Parameter('fwd_ALLOLACTOSE_DEG_alpha', 1.0)
Parameter('rvs_ALLOLACTOSE_DEG_alpha', 0.0)
Parameter('fwd_ALLOLACTOSE_DEG_beta', 1.0)
Parameter('rvs_ALLOLACTOSE_DEG_beta', 0.0)
Parameter('fwd_RXN_17726', 1.0)
Parameter('rvs_RXN_17726', 0.0)
Parameter('fwd_RXN0_7219', 1.0)
Parameter('rvs_RXN0_7219', 0.0)
Parameter('fwd_GALACTOACETYLTRAN_RXN_galactose', 1.0)
Parameter('rvs_GALACTOACETYLTRAN_RXN_galactose', 0.0)
Parameter('t0_met_beta_lactose_per', 100.0)
Parameter('t0_met_PROTON_per', 100.0)
Parameter('t0_prot_lacY_imem', 1.0)

Observable('obs_cplx_lacAx2_cyt', prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1))
Observable('obs_cplx_lacAx3_cyt', prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) % prot(dna=None, dw=2, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=2))
Observable('obs_cplx_lacIx2_cyt', prot(dna=None, dw=1, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=1))
Observable('obs_cplx_lacZx2_cyt', prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1))
Observable('obs_cplx_lacZx4_cyt', prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=2, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1) % prot(dna=None, dw=3, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=2) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=3))
Observable('obs_met_ACETYL_COA_cyt', met(name='ACETYL_COA', loc='cyt'))
Observable('obs_met_CO_A_cyt', met(name='CO_A', loc='cyt'))
Observable('obs_met_CPD_3561_cyt', met(name='CPD_3561', loc='cyt'))
Observable('obs_met_CPD_3785_cyt', met(name='CPD_3785', loc='cyt'))
Observable('obs_met_CPD_3801_cyt', met(name='CPD_3801', loc='cyt'))
Observable('obs_met_D_ARABINOSE_cyt', met(name='D_ARABINOSE', loc='cyt'))
Observable('obs_met_Fructofuranose_cyt', met(name='Fructofuranose', loc='cyt'))
Observable('obs_met_MELIBIOSE_cyt', met(name='MELIBIOSE', loc='cyt'))
Observable('obs_met_PROTON_cyt', met(name='PROTON', loc='cyt'))
Observable('obs_met_WATER_cyt', met(name='WATER', loc='cyt'))
Observable('obs_met__6_Acetyl_beta_D_Galactose_cyt', met(name='_6_Acetyl_beta_D_Galactose', loc='cyt'))
Observable('obs_met_alpha_ALLOLACTOSE_cyt', met(name='alpha_ALLOLACTOSE', loc='cyt'))
Observable('obs_met_alpha_GALACTOSE_cyt', met(name='alpha_GALACTOSE', loc='cyt'))
Observable('obs_met_alpha_glucose_cyt', met(name='alpha_glucose', loc='cyt'))
Observable('obs_met_alpha_lactose_cyt', met(name='alpha_lactose', loc='cyt'))
Observable('obs_met_beta_ALLOLACTOSE_cyt', met(name='beta_ALLOLACTOSE', loc='cyt'))
Observable('obs_met_beta_GALACTOSE_cyt', met(name='beta_GALACTOSE', loc='cyt'))
Observable('obs_met_beta_glucose_cyt', met(name='beta_glucose', loc='cyt'))
Observable('obs_met_beta_lactose_cyt', met(name='beta_lactose', loc='cyt'))
Observable('obs_prot_lacA_cyt', prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None))
Observable('obs_prot_lacI_cyt', prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None))
Observable('obs_prot_lacZ_cyt', prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None))
Observable('obs_met_beta_lactose_per', met(name='beta_lactose', loc='per', dna=None, met=None, prot=None, rna=None))
Observable('obs_met_PROTON_per', met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None))
Observable('obs_prot_lacY_imem', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None))

Rule('ALLOLACTOSE_DEG_alpha', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='alpha_ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='alpha_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='alpha_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_ALLOLACTOSE_DEG_alpha, rvs_ALLOLACTOSE_DEG_alpha)
Rule('ALLOLACTOSE_DEG_beta', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='beta_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_ALLOLACTOSE_DEG_beta, rvs_ALLOLACTOSE_DEG_beta)
Rule('BETAGALACTOSID_RXN', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_lactose', loc='cyt', prot=None) + met(name='WATER', loc='cyt', prot=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_GALACTOSE', loc='cyt', prot=None) + met(name='beta_glucose', loc='cyt', prot=None), fwd_BETAGALACTOSID_RXN, rvs_BETAGALACTOSID_RXN)
Rule('BETAGALACTOSID_RXN_alpha', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='alpha_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='alpha_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_BETAGALACTOSID_RXN_alpha, rvs_BETAGALACTOSID_RXN_alpha)
Rule('GALACTOACETYLTRAN_RXN_galactose', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=ANY) + met(name='beta_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='ACETYL_COA', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=ANY) + met(name='_6_Acetyl_beta_D_Galactose', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='CO_A', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_GALACTOACETYLTRAN_RXN_galactose, rvs_GALACTOACETYLTRAN_RXN_galactose)
Rule('GALACTOSE_MUTAROTATION_CYT', met(name='alpha_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) | met(name='beta_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_GALACTOSE_MUTAROTATION_CYT, rvs_GALACTOSE_MUTAROTATION_CYT)
Rule('GLUCOSE_MUTAROTATION_CYT', met(name='alpha_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None) | met(name='beta_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_GLUCOSE_MUTAROTATION_CYT, rvs_GLUCOSE_MUTAROTATION_CYT)
Rule('LACTOSE_MUTAROTATION_CYT', met(name='alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None) | met(name='beta_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_LACTOSE_MUTAROTATION_CYT, rvs_LACTOSE_MUTAROTATION_CYT)
Rule('PhysicalInteractionRule_1', prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) + prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) | prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1), fwd_PhysicalInteractionRule_1, rvs_PhysicalInteractionRule_1)
Rule('PhysicalInteractionRule_2', prot(dna=None, dw=2, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=2) + prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1) | prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=4) % prot(dna=None, dw=2, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1) % prot(dna=None, dw=3, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=2) % prot(dna=None, dw=4, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=3), fwd_PhysicalInteractionRule_2, rvs_PhysicalInteractionRule_2)
Rule('PhysicalInteractionRule_3', prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) + prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) | prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1), fwd_PhysicalInteractionRule_3, rvs_PhysicalInteractionRule_3)
Rule('PhysicalInteractionRule_4', prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) + prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1) | prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=3) % prot(dna=None, dw=2, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1) % prot(dna=None, dw=3, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=2), fwd_PhysicalInteractionRule_4, rvs_PhysicalInteractionRule_4)
Rule('PhysicalInteractionRule_5', prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None) + prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None) | prot(dna=None, dw=1, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=1), fwd_PhysicalInteractionRule_5, rvs_PhysicalInteractionRule_5)
Rule('RXN0_5363', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='alpha_ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN0_5363, rvs_RXN0_5363)
Rule('RXN0_5363_beta', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN0_5363_beta, rvs_RXN0_5363_beta)
Rule('RXN0_7215', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None) + met(name='CPD_3561', loc='per', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='CPD_3561', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN0_7215, rvs_RXN0_7215)
Rule('RXN0_7217', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None) + met(name='CPD_3785', loc='per', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='CPD_3785', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN0_7217, rvs_RXN0_7217)
Rule('RXN0_7219', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='CPD_3785', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='D_ARABINOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN0_7219, rvs_RXN0_7219)
Rule('RXN_17726', prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='CPD_3561', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=ANY, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=ANY) + met(name='beta_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='Fructofuranose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN_17726, rvs_RXN_17726)
Rule('RXN_17755', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None) + met(name='CPD_3801', loc='per', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='CPD_3801', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_RXN_17755, rvs_RXN_17755)
Rule('TRANS_RXN_24', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None) + met(name='alpha_lactose', loc='per', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_TRANS_RXN_24, rvs_TRANS_RXN_24)
Rule('TRANS_RXN_24_beta', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None) + met(name='beta_lactose', loc='per', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='beta_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_TRANS_RXN_24_beta, rvs_TRANS_RXN_24_beta)
Rule('TRANS_RXN_94', prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None) + met(name='MELIBIOSE', loc='per', dna=None, met=None, prot=None, rna=None) | prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None) + met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None) + met(name='MELIBIOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), fwd_TRANS_RXN_94, rvs_TRANS_RXN_94)

Initial(prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None), t0_prot_lacA_cyt)
Initial(prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None), t0_prot_lacI_cyt)
Initial(prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None), t0_prot_lacZ_cyt)
Initial(prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) % prot(dna=None, dw=2, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=2), t0_cplx_lacAx3_cyt)
Initial(prot(dna=None, dw=1, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacA', prot=None, rna=None, up=1), t0_cplx_lacAx2_cyt)
Initial(prot(dna=None, dw=1, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacI', prot=None, rna=None, up=1), t0_cplx_lacIx2_cyt)
Initial(prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=2, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1) % prot(dna=None, dw=3, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=2) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=3), t0_cplx_lacZx4_cyt)
Initial(prot(dna=None, dw=1, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=None) % prot(dna=None, dw=None, loc='cyt', met=None, name='lacZ', prot=None, rna=None, up=1), t0_cplx_lacZx2_cyt)
Initial(met(name='ACETYL_COA', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_ACETYL_COA_cyt)
Initial(met(name='CO_A', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_CO_A_cyt)
Initial(met(name='CPD_3561', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_CPD_3561_cyt)
Initial(met(name='CPD_3785', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_CPD_3785_cyt)
Initial(met(name='CPD_3801', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_CPD_3801_cyt)
Initial(met(name='D_ARABINOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_D_ARABINOSE_cyt)
Initial(met(name='Fructofuranose', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_Fructofuranose_cyt)
Initial(met(name='MELIBIOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_MELIBIOSE_cyt)
Initial(met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_PROTON_cyt)
Initial(met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_WATER_cyt)
Initial(met(name='_6_Acetyl_beta_D_Galactose', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met__6_Acetyl_beta_D_Galactose_cyt)
Initial(met(name='alpha_ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_alpha_ALLOLACTOSE_cyt)
Initial(met(name='alpha_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_alpha_GALACTOSE_cyt)
Initial(met(name='alpha_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_alpha_glucose_cyt)
Initial(met(name='alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_alpha_lactose_cyt)
Initial(met(name='beta_ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_beta_ALLOLACTOSE_cyt)
Initial(met(name='beta_GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_beta_GALACTOSE_cyt)
Initial(met(name='beta_glucose', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_beta_glucose_cyt)
Initial(met(name='beta_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None), t0_met_beta_lactose_cyt)
Initial(prot(dna=None, dw=None, loc='cyt', met=None, name='lacY', prot=None, rna=None, up=None), t0_prot_lacY_cyt)
Initial(prot(dna=None, dw=None, loc='cyt', met=None, name='spontaneous', prot=None, rna=None, up=None), t0_prot_spontaneous_cyt)
Initial(met(name='beta_lactose', loc='per', dna=None, met=None, prot=None, rna=None), t0_met_beta_lactose_per)
Initial(met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None), t0_met_PROTON_per)
Initial(prot(dna=None, dw=None, loc='imem', met=None, name='lacY', prot=None, rna=None, up=None), t0_prot_lacY_imem)

