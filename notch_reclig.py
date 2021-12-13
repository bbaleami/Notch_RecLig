# import packages
from pysb import *
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

Parameter('kf_notch2_dll1_inter', 0)
Parameter('kr_notch2_dll1_inter', 0)
Parameter('kf_notch2_dll1_intra', 0)
Parameter('kr_notch2_dll1_intra', 0)
Parameter('kf_notch2_dll3_inter', 0)
Parameter('kr_notch2_dll3_inter', 0)
Parameter('kf_notch2_dll3_intra', 0)
Parameter('kr_notch2_dll3_intra', 0)
Parameter('kf_notch2_dll4_inter', 0)
Parameter('kr_notch2_dll4_inter', 0)
Parameter('kf_notch2_dll4_intra', 0)
Parameter('kr_notch2_dll4_intra', 0)
Parameter('kf_notch2_jag1_inter', 0)
Parameter('kr_notch2_jag1_inter', 0)
Parameter('kf_notch2_jag1_intra', 0)
Parameter('kr_notch2_jag1_intra', 0)
Parameter('kf_notch2_jag2_inter', 0)
Parameter('kr_notch2_jag2_inter', 0)
Parameter('kf_notch2_jag2_intra', 0)
Parameter('kr_notch2_jag2_intra', 0)

Parameter('kf_notch3_dll1_inter', 0)
Parameter('kr_notch3_dll1_inter', 0)
Parameter('kf_notch3_dll1_intra', 0)
Parameter('kr_notch3_dll1_intra', 0)
Parameter('kf_notch3_dll3_inter', 0)
Parameter('kr_notch3_dll3_inter', 0)
Parameter('kf_notch3_dll3_intra', 0)
Parameter('kr_notch3_dll3_intra', 0)
Parameter('kf_notch3_dll4_inter', 0)
Parameter('kr_notch3_dll4_inter', 0)
Parameter('kf_notch3_dll4_intra', 0)
Parameter('kr_notch3_dll4_intra', 0)
Parameter('kf_notch3_jag1_inter', 0)
Parameter('kr_notch3_jag1_inter', 0)
Parameter('kf_notch3_jag1_intra', 0)
Parameter('kr_notch3_jag1_intra', 0)
Parameter('kf_notch3_jag2_inter', 0)
Parameter('kr_notch3_jag2_inter', 0)
Parameter('kf_notch3_jag2_intra', 0)
Parameter('kr_notch3_jag2_intra', 0)

Parameter('kf_notch4_dll1_inter', 0)
Parameter('kr_notch4_dll1_inter', 0)
Parameter('kf_notch4_dll1_intra', 0)
Parameter('kr_notch4_dll1_intra', 0)
Parameter('kf_notch4_dll3_inter', 0)
Parameter('kr_notch4_dll3_inter', 0)
Parameter('kf_notch4_dll3_intra', 0)
Parameter('kr_notch4_dll3_intra', 0)
Parameter('kf_notch4_dll4_inter', 0)
Parameter('kr_notch4_dll4_inter', 0)
Parameter('kf_notch4_dll4_intra', 0)
Parameter('kr_notch4_dll4_intra', 0)
Parameter('kf_notch4_jag1_inter', 0)
Parameter('kr_notch4_jag1_inter', 0)
Parameter('kf_notch4_jag1_intra', 0)
Parameter('kr_notch4_jag1_intra', 0)
Parameter('kf_notch4_jag2_inter', 0)
Parameter('kr_notch4_jag2_inter', 0)
Parameter('kf_notch4_jag2_intra', 0)
Parameter('kr_notch4_jag2_intra', 0)

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

Rule('notch2_binds_dll1_inter', NOTCH2(lig = None) + DLL1(rec = None, loc = 'inter') |
     NOTCH2(lig = 21) % DLL1(rec = 21, loc = 'inter'), kf_notch2_dll1_inter, kr_notch2_dll1_inter)
Rule('notch2_binds_dll1_intra', NOTCH2(lig = None) + DLL1(rec = None, loc = 'intra') |
     NOTCH2(lig = 21) % DLL1(rec = 21, loc = 'intra'), kf_notch2_dll1_intra, kr_notch2_dll1_intra)
Rule('notch2_binds_dll3_inter', NOTCH2(lig = None) + DLL3(rec = None, loc = 'inter') |
     NOTCH2(lig = 23) % DLL3(rec = 23, loc = 'inter'), kf_notch2_dll3_inter, kr_notch2_dll3_inter)
Rule('notch2_binds_dll3_intra', NOTCH2(lig = None) + DLL3(rec = None, loc = 'intra') |
     NOTCH2(lig = 23) % DLL3(rec = 23, loc = 'intra'), kf_notch2_dll3_intra, kr_notch2_dll3_intra)
Rule('notch2_binds_dll4_inter', NOTCH2(lig = None) + DLL4(rec = None, loc = 'inter') |
     NOTCH2(lig = 24) % DLL4(rec = 24, loc = 'inter'), kf_notch2_dll4_inter, kr_notch2_dll4_inter)
Rule('notch2_binds_dll4_intra', NOTCH2(lig = None) + DLL4(rec = None, loc = 'intra') |
     NOTCH2(lig = 24) % DLL4(rec = 24, loc = 'intra'), kf_notch2_dll4_intra, kr_notch2_dll4_intra)
Rule('notch2_binds_jag1_inter', NOTCH2(lig = None) + JAG1(rec = None, loc = 'inter') |
     NOTCH2(lig = 25) % JAG1(rec = 25, loc = 'inter'), kf_notch2_jag1_inter, kr_notch2_jag1_inter)
Rule('notch2_binds_jag1_intra', NOTCH2(lig = None) + JAG1(rec = None, loc = 'intra') |
     NOTCH2(lig = 25) % JAG1(rec = 25, loc = 'intra'), kf_notch2_jag1_intra, kr_notch2_jag1_intra)
Rule('notch2_binds_jag2_inter', NOTCH2(lig = None) + JAG2(rec = None, loc = 'inter') |
     NOTCH2(lig = 26) % JAG2(rec = 26, loc = 'inter'), kf_notch2_jag2_inter, kr_notch2_jag2_inter)
Rule('notch2_binds_jag2_intra', NOTCH2(lig = None) + JAG2(rec = None, loc = 'intra') |
     NOTCH2(lig = 26) % JAG2(rec = 26, loc = 'intra'), kf_notch2_jag2_intra, kr_notch2_jag2_intra)

Rule('notch3_binds_dll1_inter', NOTCH3(lig = None) + DLL1(rec = None, loc = 'inter') |
     NOTCH3(lig = 31) % DLL1(rec = 31, loc = 'inter'), kf_notch3_dll1_inter, kr_notch3_dll1_inter)
Rule('notch3_binds_dll1_intra', NOTCH3(lig = None) + DLL1(rec = None, loc = 'intra') |
     NOTCH3(lig = 31) % DLL1(rec = 31, loc = 'intra'), kf_notch3_dll1_intra, kr_notch3_dll1_intra)
Rule('notch3_binds_dll3_inter', NOTCH3(lig = None) + DLL3(rec = None, loc = 'inter') |
     NOTCH3(lig = 33) % DLL3(rec = 33, loc = 'inter'), kf_notch3_dll3_inter, kr_notch3_dll3_inter)
Rule('notch3_binds_dll3_intra', NOTCH3(lig = None) + DLL3(rec = None, loc = 'intra') |
     NOTCH3(lig = 33) % DLL3(rec = 33, loc = 'intra'), kf_notch3_dll3_intra, kr_notch3_dll3_intra)
Rule('notch3_binds_dll4_inter', NOTCH3(lig = None) + DLL4(rec = None, loc = 'inter') |
     NOTCH3(lig = 34) % DLL4(rec = 34, loc = 'inter'), kf_notch3_dll4_inter, kr_notch3_dll4_inter)
Rule('notch3_binds_dll4_intra', NOTCH3(lig = None) + DLL4(rec = None, loc = 'intra') |
     NOTCH3(lig = 34) % DLL4(rec = 34, loc = 'intra'), kf_notch3_dll4_intra, kr_notch3_dll4_intra)
Rule('notch3_binds_jag1_inter', NOTCH3(lig = None) + JAG1(rec = None, loc = 'inter') |
     NOTCH3(lig = 35) % JAG1(rec = 35, loc = 'inter'), kf_notch3_jag1_inter, kr_notch3_jag1_inter)
Rule('notch3_binds_jag1_intra', NOTCH3(lig = None) + JAG1(rec = None, loc = 'intra') |
     NOTCH3(lig = 35) % JAG1(rec = 35, loc = 'intra'), kf_notch3_jag1_intra, kr_notch3_jag1_intra)
Rule('notch3_binds_jag2_inter', NOTCH3(lig = None) + JAG2(rec = None, loc = 'inter') |
     NOTCH3(lig = 36) % JAG2(rec = 36, loc = 'inter'), kf_notch3_jag2_inter, kr_notch3_jag2_inter)
Rule('notch3_binds_jag2_intra', NOTCH3(lig = None) + JAG2(rec = None, loc = 'intra') |
     NOTCH3(lig = 36) % JAG2(rec = 36, loc = 'intra'), kf_notch3_jag2_intra, kr_notch3_jag2_intra)

Rule('notch4_binds_dll1_inter', NOTCH4(lig = None) + DLL1(rec = None, loc = 'inter') |
     NOTCH4(lig = 41) % DLL1(rec = 41, loc = 'inter'), kf_notch4_dll1_inter, kr_notch4_dll1_inter)
Rule('notch4_binds_dll1_intra', NOTCH4(lig = None) + DLL1(rec = None, loc = 'intra') |
     NOTCH4(lig = 41) % DLL1(rec = 41, loc = 'intra'), kf_notch4_dll1_intra, kr_notch4_dll1_intra)
Rule('notch4_binds_dll3_inter', NOTCH4(lig = None) + DLL3(rec = None, loc = 'inter') |
     NOTCH4(lig = 43) % DLL3(rec = 43, loc = 'inter'), kf_notch4_dll3_inter, kr_notch4_dll3_inter)
Rule('notch4_binds_dll3_intra', NOTCH4(lig = None) + DLL3(rec = None, loc = 'intra') |
     NOTCH4(lig = 43) % DLL3(rec = 43, loc = 'intra'), kf_notch4_dll3_intra, kr_notch4_dll3_intra)
Rule('notch4_binds_dll4_inter', NOTCH4(lig = None) + DLL4(rec = None, loc = 'inter') |
     NOTCH4(lig = 44) % DLL4(rec = 44, loc = 'inter'), kf_notch4_dll4_inter, kr_notch4_dll4_inter)
Rule('notch4_binds_dll4_intra', NOTCH4(lig = None) + DLL4(rec = None, loc = 'intra') |
     NOTCH4(lig = 44) % DLL4(rec = 44, loc = 'intra'), kf_notch4_dll4_intra, kr_notch4_dll4_intra)
Rule('notch4_binds_jag1_inter', NOTCH4(lig = None) + JAG1(rec = None, loc = 'inter') |
     NOTCH4(lig = 45) % JAG1(rec = 45, loc = 'inter'), kf_notch4_jag1_inter, kr_notch4_jag1_inter)
Rule('notch4_binds_jag1_intra', NOTCH4(lig = None) + JAG1(rec = None, loc = 'intra') |
     NOTCH4(lig = 15) % JAG1(rec = 15, loc = 'intra'), kf_notch4_jag1_intra, kr_notch4_jag1_intra)
Rule('notch4_binds_jag2_inter', NOTCH4(lig = None) + JAG2(rec = None, loc = 'inter') |
     NOTCH4(lig = 46) % JAG2(rec = 46, loc = 'inter'), kf_notch4_jag2_inter, kr_notch4_jag2_inter)
Rule('notch4_binds_jag2_intra', NOTCH4(lig = None) + JAG2(rec = None, loc = 'intra') |
     NOTCH4(lig = 46) % JAG2(rec = 46, loc = 'intra'), kf_notch4_jag2_intra, kr_notch4_jag2_intra)

print()
print(model)
print()
print(model.rules)


# define observables
Observable('notch1_bound_all', NOTCH1(lig = ANY))
Observable('notch1_unbound', NOTCH1(lig = None))
# Observable('notch2_bound_all', NOTCH2(lig = ANY))
# Observable('notch2_unbound', NOTCH2(lig = None))
# Observable('notch3_bound_all', NOTCH3(lig = ANY))
# Observable('notch3_unbound', NOTCH3(lig = None))
# Observable('notch4_bound_all', NOTCH4(lig = ANY))
# Observable('notch4_unbound', NOTCH4(lig = None))
# Observable('dll1_inter_all', DLL1(rec = ANY, loc = 'inter'))
Observable('dll1_inter_unbound', DLL1(rec = None, loc = 'inter'))
# Observable('dll1_intra_all', DLL1(rec = ANY, loc = 'intra'))
# Observable('dll1_intra_unbound', DLL1(rec = None, loc = 'intra'))
# Observable('dll3_inter_all', DLL3(rec = ANY, loc = 'inter'))
# Observable('dll3_inter_unbound', DLL3(rec = None, loc = 'inter'))
# Observable('dll3_intra_all', DLL3(rec = ANY, loc = 'intra'))
# Observable('dll3_intra_unbound', DLL3(rec = None, loc = 'intra'))
# Observable('dll4_inter_all', DLL4(rec = ANY, loc = 'inter'))
# Observable('dll4_inter_unbound', DLL4(rec = None, loc = 'inter'))
# Observable('dll4_intra_all', DLL4(rec = ANY, loc = 'intra'))
# Observable('dll4_intra_unbound', DLL4(rec = None, loc = 'intra'))
# Observable('jag1_inter_all', JAG1(rec = ANY, loc = 'inter'))
# Observable('jag1_inter_unbound', JAG1(rec = None, loc = 'inter'))
# Observable('jag1_intra_all', JAG1(rec = ANY, loc = 'intra'))
# Observable('jag1_intra_unbound', JAG1(rec = None, loc = 'intra'))
# Observable('jag2_inter_all', JAG2(rec = ANY, loc = 'inter'))
# Observable('jag2_inter_unbound', JAG2(rec = None, loc = 'inter'))
# Observable('jag2_intra_all', JAG2(rec = ANY, loc = 'intra'))
# Observable('jag2_intra_unbound', JAG2(rec = None, loc = 'intra'))

Observable('notch1_bound_dll1_inter', NOTCH1(lig = 11) % DLL1(rec = 11, loc = 'inter'))
# Observable('notch1_bound_dll1_intra', NOTCH1(lig = 11) % DLL1(rec = 11, loc = 'intra'))
# Observable('notch1_bound_dll3_inter', NOTCH1(lig = 13) % DLL3(rec = 13, loc = 'inter'))
# Observable('notch1_bound_dll3_intra', NOTCH1(lig = 13) % DLL3(rec = 13, loc = 'intra'))
# Observable('notch1_bound_dll4_inter', NOTCH1(lig = 14) % DLL4(rec = 14, loc = 'inter'))
# Observable('notch1_bound_dll4_intra', NOTCH1(lig = 14) % DLL4(rec = 14, loc = 'intra'))
# Observable('notch1_bound_jag1_inter', NOTCH1(lig = 15) % JAG1(rec = 15, loc = 'inter'))
# Observable('notch1_bound_jag1_intra', NOTCH1(lig = 15) % JAG1(rec = 15, loc = 'intra'))
# Observable('notch1_bound_jag2_inter', NOTCH1(lig = 16) % JAG2(rec = 16, loc = 'inter'))
# Observable('notch1_bound_jag2_intra', NOTCH1(lig = 16) % JAG2(rec = 16, loc = 'intra'))
#
# Observable('notch2_bound_dll1_inter', NOTCH2(lig = 21) % DLL1(rec = 21, loc = 'inter'))
# Observable('notch2_bound_dll1_intra', NOTCH2(lig = 21) % DLL1(rec = 21, loc = 'intra'))
# Observable('notch2_bound_dll3_inter', NOTCH2(lig = 23) % DLL3(rec = 23, loc = 'inter'))
# Observable('notch2_bound_dll3_intra', NOTCH2(lig = 23) % DLL3(rec = 23, loc = 'intra'))
# Observable('notch2_bound_dll4_inter', NOTCH2(lig = 24) % DLL4(rec = 24, loc = 'inter'))
# Observable('notch2_bound_dll4_intra', NOTCH2(lig = 24) % DLL4(rec = 24, loc = 'intra'))
# Observable('notch2_bound_jag1_inter', NOTCH2(lig = 25) % JAG1(rec = 25, loc = 'inter'))
# Observable('notch2_bound_jag1_intra', NOTCH2(lig = 25) % JAG1(rec = 25, loc = 'intra'))
# Observable('notch2_bound_jag2_inter', NOTCH2(lig = 26) % JAG2(rec = 26, loc = 'inter'))
# Observable('notch2_bound_jag2_intra', NOTCH2(lig = 26) % JAG2(rec = 26, loc = 'intra'))
#
# Observable('notch3_bound_dll1_inter', NOTCH3(lig = 31) % DLL1(rec = 31, loc = 'inter'))
# Observable('notch3_bound_dll1_intra', NOTCH3(lig = 31) % DLL1(rec = 31, loc = 'intra'))
# Observable('notch3_bound_dll3_inter', NOTCH3(lig = 33) % DLL3(rec = 33, loc = 'inter'))
# Observable('notch3_bound_dll3_intra', NOTCH3(lig = 33) % DLL3(rec = 33, loc = 'intra'))
# Observable('notch3_bound_dll4_inter', NOTCH3(lig = 34) % DLL4(rec = 34, loc = 'inter'))
# Observable('notch3_bound_dll4_intra', NOTCH3(lig = 34) % DLL4(rec = 34, loc = 'intra'))
# Observable('notch3_bound_jag1_inter', NOTCH3(lig = 35) % JAG1(rec = 35, loc = 'inter'))
# Observable('notch3_bound_jag1_intra', NOTCH3(lig = 35) % JAG1(rec = 35, loc = 'intra'))
# Observable('notch3_bound_jag2_inter', NOTCH3(lig = 36) % JAG2(rec = 36, loc = 'inter'))
# Observable('notch3_bound_jag2_intra', NOTCH3(lig = 36) % JAG2(rec = 36, loc = 'intra'))
#
# Observable('notch4_bound_dll1_inter', NOTCH4(lig = 41) % DLL1(rec = 41, loc = 'inter'))
# Observable('notch4_bound_dll1_intra', NOTCH4(lig = 41) % DLL1(rec = 41, loc = 'intra'))
# Observable('notch4_bound_dll3_inter', NOTCH4(lig = 43) % DLL3(rec = 43, loc = 'inter'))
# Observable('notch4_bound_dll3_intra', NOTCH4(lig = 43) % DLL3(rec = 43, loc = 'intra'))
# Observable('notch4_bound_dll4_inter', NOTCH4(lig = 44) % DLL4(rec = 44, loc = 'inter'))
# Observable('notch4_bound_dll4_intra', NOTCH4(lig = 44) % DLL4(rec = 44, loc = 'intra'))
# Observable('notch4_bound_jag1_inter', NOTCH4(lig = 45) % JAG1(rec = 45, loc = 'inter'))
# Observable('notch4_bound_jag1_intra', NOTCH4(lig = 45) % JAG1(rec = 45, loc = 'intra'))
# Observable('notch4_bound_jag2_inter', NOTCH4(lig = 46) % JAG2(rec = 46, loc = 'inter'))
# Observable('notch4_bound_jag2_intra', NOTCH4(lig = 46) % JAG2(rec = 46, loc = 'intra'))



print()
print(model)
print(model.observables)
print()
print(len(model.observables))

# simulation commands

