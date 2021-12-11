# import package
from  pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

# define model
Model()

# define monomers
Monomer('NOTCH1', ['lig'])
Monomer('NOTCH2', ['lig'])
Monomer('NOTCH3', ['lig'])
Monomer('NOTCH4', ['lig'])
Monomer('DLL1', ['rec', 'loc'], {'loc': ['intra', 'inter']})
Monomer('DLL3', ['rec', 'loc'], {'loc': ['intra', 'inter']})
Monomer('DLL4', ['rec', 'loc'], {'loc': ['intra', 'inter']})
Monomer('JAG1', ['rec', 'loc'], {'loc': ['intra', 'inter']})
Monomer('JAG2', ['rec', 'loc'], {'loc': ['intra', 'inter']})

# define parameters
Parameter('notch1_init', 10)
Parameter('notch2_init', 0)
Parameter('notch3_init', 0)
Parameter('notch4_init', 0)
Parameter('dll1_intra_init', 0)
Parameter('dll1_inter_init', 10)
Parameter('dll3_intra_init', 0)
Parameter('dll3_inter_init', 0)
Parameter('dll4_intra_init', 0)
Parameter('dll4_inter_init', 0)
Parameter('jag1_intra_init', 0)
Parameter('jag1_inter_init', 0)
Parameter('jag2_intra_init', 0)
Parameter('jag2_inter_init', 0)

Parameter('kf_notch1_dll1_inter', 1)
Parameter('kr_notch1_dll1_inter', 1)
Parameter('kf_notch1_dll1_intra', 0)
Parameter('kr_notch1_dll1_intra', 0)
Parameter('kf_notch1_dll3_inter', 0)
Parameter('kr_notch1_dll3_inter', 0)
Parameter('kf_notch1_dll3_intra', 0)
Parameter('kr_notch1_dll3_intra', 0)
Parameter('kf_notch1_dll4_inter', 0)
Parameter('kr_notch1_dll4_inter', 0)
Parameter('kf_notch1_dll4_intra', 0)
Parameter('kr_notch1_dll4_intra', 0)
Parameter('kf_notch1_jag1_inter', 0)
Parameter('kr_notch1_jag1_inter', 0)
Parameter('kf_notch1_jag1_intra', 0)
Parameter('kr_notch1_jag1_intra', 0)
Parameter('kf_notch1_jag2_inter', 0)
Parameter('kr_notch1_jag2_inter', 0)
Parameter('kf_notch1_jag2_intra', 0)
Parameter('kr_notch1_jag2_intra', 0)

# define initials
Initial(NOTCH1(lig = None), notch1_init)
Initial(NOTCH2(lig = None), notch2_init)
Initial(NOTCH3(lig = None), notch3_init)
Initial(NOTCH4(lig = None), notch4_init)
Initial(DLL1(rec = None, loc = 'intra'), dll1_intra_init)
Initial(DLL1(rec = None, loc = 'inter'), dll1_inter_init)
Initial(DLL3(rec = None, loc = 'intra'), dll3_intra_init)
Initial(DLL3(rec = None, loc = 'inter'), dll3_inter_init)
Initial(DLL4(rec = None, loc = 'intra'), dll4_intra_init)
Initial(DLL4(rec = None, loc = 'inter'), dll4_inter_init)
Initial(JAG1(rec = None, loc = 'intra'), jag1_intra_init)
Initial(JAG1(rec = None, loc = 'inter'), jag1_inter_init)
Initial(JAG2(rec = None, loc = 'intra'), jag2_intra_init)
Initial(JAG2(rec = None, loc = 'inter'), jag2_inter_init)

print(model)
print(model.monomers)
print(model.monomers['NOTCH3'])
print()
print(model.parameters)
print()
for ic in model.initial_conditions:
    print(ic)

# define rules
# for binding sites: first number is for receptor and second number is for ligand (e.g., notch2 binds dll3 would be 23)
Rule('notch1_binds_dll1_inter', NOTCH1(lig = None) + DLL1(rec = None, loc = 'inter') |
     NOTCH1(lig = 11) % DLL1(rec = 11, loc = 'inter'), kf_notch1_dll1_inter, kr_notch1_dll1_inter)
Rule('notch1_binds_dll1_intra', NOTCH1(lig = None) + DLL1(rec = None, loc = 'intra') |
     NOTCH1(lig = 11) % DLL1(rec = 11, loc = 'intra'), kf_notch1_dll1_intra, kr_notch1_dll1_intra)
Rule('notch1_binds_dll3_inter', NOTCH1(lig = None) + DLL3(rec = None, loc = 'inter') |
     NOTCH1(lig = 13) % DLL3(rec = 13, loc = 'inter'), kf_notch1_dll3_inter, kr_notch1_dll3_inter)
Rule('notch1_binds_dll3_intra', NOTCH1(lig = None) + DLL3(rec = None, loc = 'intra') |
     NOTCH1(lig = 13) % DLL3(rec = 13, loc = 'intra'), kf_notch1_dll3_intra, kr_notch1_dll3_intra)
Rule('notch1_binds_dll4_inter', NOTCH1(lig = None) + DLL4(rec = None, loc = 'inter') |
     NOTCH1(lig = 14) % DLL4(rec = 14, loc = 'inter'), kf_notch1_dll4_inter, kr_notch1_dll4_inter)
Rule('notch1_binds_dll4_intra', NOTCH1(lig = None) + DLL4(rec = None, loc = 'intra') |
     NOTCH1(lig = 14) % DLL4(rec = 14, loc = 'intra'), kf_notch1_dll4_intra, kr_notch1_dll4_intra)
Rule('notch1_binds_jag1_inter', NOTCH1(lig = None) + JAG1(rec = None, loc = 'inter') |
     NOTCH1(lig = 15) % JAG1(rec = 15, loc = 'inter'), kf_notch1_jag1_inter, kr_notch1_jag1_inter)
Rule('notch1_binds_jag1_intra', NOTCH1(lig = None) + JAG1(rec = None, loc = 'intra') |
     NOTCH1(lig = 15) % JAG1(rec = 15, loc = 'intra'), kf_notch1_jag1_intra, kr_notch1_jag1_intra)
Rule('notch1_binds_jag2_inter', NOTCH1(lig = None) + JAG2(rec = None, loc = 'inter') |
     NOTCH1(lig = 16) % JAG2(rec = 16, loc = 'inter'), kf_notch1_jag2_inter, kr_notch1_jag2_inter)
Rule('notch1_binds_jag2_intra', NOTCH1(lig = None) + JAG2(rec = None, loc = 'intra') |
     NOTCH1(lig = 16) % JAG2(rec = 16, loc = 'intra'), kf_notch1_jag2_intra, kr_notch1_jag2_intra)

# define observables
print(model.rules)

# simulation commands

