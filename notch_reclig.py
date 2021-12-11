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


# define observables


# simulation commands

