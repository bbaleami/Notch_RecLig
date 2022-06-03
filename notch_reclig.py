# import packages
from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

# define model
Model()

# define monomers
Monomer('NOTCH1_ECD', ['icd', 'fng', 'fuc', 'lig', 'loc'], {'fuc': ['uf', 'f1', 'f2'], 'loc': ['golgi', 'pm', 'endo']})
Monomer('NOTCH1_ICD', ['ecd', 'rbpj', 'maml', 'ntc', 'loc'], {'loc': ['golgi', 'pm', 'nuc']})
Monomer('NOTCH2_ECD', ['icd', 'fng', 'fuc', 'lig', 'loc'], {'fuc': ['uf', 'f1', 'f2'], 'loc': ['golgi', 'pm', 'endo']})
Monomer('NOTCH2_ICD', ['ecd', 'rbpj', 'maml', 'ntc', 'loc'], {'loc': ['golgi', 'pm', 'nuc']})
Monomer('NOTCH3_ECD', ['icd', 'fng', 'fuc', 'lig', 'loc'], {'fuc': ['uf', 'f1', 'f2'], 'loc': ['golgi', 'pm', 'endo']})
Monomer('NOTCH3_ICD', ['ecd', 'rbpj', 'maml', 'ntc', 'loc'], {'loc': ['golgi', 'pm', 'nuc']})
Monomer('NOTCH4_ECD', ['icd', 'fng', 'fuc', 'lig', 'loc'], {'fuc': ['uf', 'f1', 'f2'], 'loc': ['golgi', 'pm', 'endo']})
Monomer('NOTCH4_ICD', ['ecd', 'rbpj', 'maml', 'ntc', 'loc'], {'loc': ['golgi', 'pm', 'nuc']})
Monomer('DLL1', ['rec', 'loc'], {'loc': ['cis', 'trans']})
Monomer('DLL3', ['rec', 'loc'], {'loc': ['cis', 'trans', 'golgi']})
Monomer('DLL4', ['rec', 'loc'], {'loc': ['cis', 'trans']})
Monomer('JAG1', ['rec', 'loc'], {'loc': ['cis', 'trans']})
Monomer('JAG2', ['rec', 'loc'], {'loc': ['cis', 'trans']})
Monomer('RFNG', ['rec'])
Monomer('LFNG', ['rec'])
Monomer('MFNG', ['rec'])
Monomer('RBPJ', ['nicd', 'maml', 'gene1', 'gene2'])
Monomer('MAML', ['nicd', 'rbpj'])
Monomer('GENE1', ['ntc'])
Monomer('GENE2', ['ntc'])
Monomer('GENE1_MRNA')
Monomer('GENE2_MRNA')

#### define parameters ####
# initial conditions
Parameter('notch1_init', 20)
Parameter('notch2_init', 0)
Parameter('notch3_init', 0)
Parameter('notch4_init', 0)
Parameter('dll1_cis_init', 0)
Parameter('dll1_trans_init', 10)
Parameter('dll3_cis_init', 0)
Parameter('dll3_trans_init', 0)
Parameter('dll3_golgi_init', 0)
Parameter('dll4_cis_init', 0)
Parameter('dll4_trans_init', 5)
Parameter('jag1_cis_init', 0)
Parameter('jag1_trans_init', 0)
Parameter('jag2_cis_init', 0)
Parameter('jag2_trans_init', 0)
Parameter('rfng_init', 0)
Parameter('lfng_init', 0)
Parameter('mfng_init', 0)
Parameter('rbpj_init', 0)
Parameter('maml_init', 0)
Parameter('gene1_init', 2)
Parameter('gene2_init', 2)
Parameter('gene1_mrna_init', 0)
Parameter('gene2_mrna_init', 0)

# rates for notch1 binding to ligands
Parameter('kf_notch1_dll1_uf', 1)
Parameter('kr_notch1_dll1_uf', 1)
Parameter('kf_notch1_dll1_f1', 0)
Parameter('kr_notch1_dll1_f1', 0)
Parameter('kf_notch1_dll1_f2', 0)
Parameter('kr_notch1_dll1_f2', 0)
Parameter('kf_notch1_dll3_uf', 0)
Parameter('kr_notch1_dll3_uf', 0)
Parameter('kf_notch1_dll3_f1', 0)
Parameter('kr_notch1_dll3_f1', 0)
Parameter('kf_notch1_dll3_f2', 0)
Parameter('kr_notch1_dll3_f2', 0)
Parameter('kf_notch1_dll4_uf', 0.1)
Parameter('kr_notch1_dll4_uf', 0.1)
Parameter('kf_notch1_dll4_f1', 0)
Parameter('kr_notch1_dll4_f1', 0)
Parameter('kf_notch1_dll4_f2', 0)
Parameter('kr_notch1_dll4_f2', 0)
Parameter('kf_notch1_jag1_uf', 0)
Parameter('kr_notch1_jag1_uf', 0)
Parameter('kf_notch1_jag1_f1', 0)
Parameter('kr_notch1_jag1_f1', 0)
Parameter('kf_notch1_jag1_f2', 0)
Parameter('kr_notch1_jag1_f2', 0)
Parameter('kf_notch1_jag2_uf', 0)
Parameter('kr_notch1_jag2_uf', 0)
Parameter('kf_notch1_jag2_f1', 0)
Parameter('kr_notch1_jag2_f1', 0)
Parameter('kf_notch1_jag2_f2', 0)
Parameter('kr_notch1_jag2_f2', 0)

# rates for  notch2 binding to ligands
Parameter('kf_notch2_dll1_uf', 0)
Parameter('kr_notch2_dll1_uf', 0)
Parameter('kf_notch2_dll1_f1', 0)
Parameter('kr_notch2_dll1_f1', 0)
Parameter('kf_notch2_dll1_f2', 0)
Parameter('kr_notch2_dll1_f2', 0)
Parameter('kf_notch2_dll3_uf', 0)
Parameter('kr_notch2_dll3_uf', 0)
Parameter('kf_notch2_dll3_f1', 0)
Parameter('kr_notch2_dll3_f1', 0)
Parameter('kf_notch2_dll3_f2', 0)
Parameter('kr_notch2_dll3_f2', 0)
Parameter('kf_notch2_dll4_uf', 0)
Parameter('kr_notch2_dll4_uf', 0)
Parameter('kf_notch2_dll4_f1', 0)
Parameter('kr_notch2_dll4_f1', 0)
Parameter('kf_notch2_dll4_f2', 0)
Parameter('kr_notch2_dll4_f2', 0)
Parameter('kf_notch2_jag1_uf', 0)
Parameter('kr_notch2_jag1_uf', 0)
Parameter('kf_notch2_jag1_f1', 0)
Parameter('kr_notch2_jag1_f1', 0)
Parameter('kf_notch2_jag1_f2', 0)
Parameter('kr_notch2_jag1_f2', 0)
Parameter('kf_notch2_jag2_uf', 0)
Parameter('kr_notch2_jag2_uf', 0)
Parameter('kf_notch2_jag2_f1', 0)
Parameter('kr_notch2_jag2_f1', 0)
Parameter('kf_notch2_jag2_f2', 0)
Parameter('kr_notch2_jag2_f2', 0)

# rates for notch 3 binding to ligands
Parameter('kf_notch3_dll1_uf', 0)
Parameter('kr_notch3_dll1_uf', 0)
Parameter('kf_notch3_dll1_f1', 0)
Parameter('kr_notch3_dll1_f1', 0)
Parameter('kf_notch3_dll1_f2', 0)
Parameter('kr_notch3_dll1_f2', 0)
Parameter('kf_notch3_dll3_uf', 0)
Parameter('kr_notch3_dll3_uf', 0)
Parameter('kf_notch3_dll3_f1', 0)
Parameter('kr_notch3_dll3_f1', 0)
Parameter('kf_notch3_dll3_f2', 0)
Parameter('kr_notch3_dll3_f2', 0)
Parameter('kf_notch3_dll4_uf', 0)
Parameter('kr_notch3_dll4_uf', 0)
Parameter('kf_notch3_dll4_f1', 0)
Parameter('kr_notch3_dll4_f1', 0)
Parameter('kf_notch3_dll4_f2', 0)
Parameter('kr_notch3_dll4_f2', 0)
Parameter('kf_notch3_jag1_uf', 0)
Parameter('kr_notch3_jag1_uf', 0)
Parameter('kf_notch3_jag1_f1', 0)
Parameter('kr_notch3_jag1_f1', 0)
Parameter('kf_notch3_jag1_f2', 0)
Parameter('kr_notch3_jag1_f2', 0)
Parameter('kf_notch3_jag2_uf', 0)
Parameter('kr_notch3_jag2_uf', 0)
Parameter('kf_notch3_jag2_f1', 0)
Parameter('kr_notch3_jag2_f1', 0)
Parameter('kf_notch3_jag2_f2', 0)
Parameter('kr_notch3_jag2_f2', 0)

# rates for notch 4 binding to ligands
Parameter('kf_notch4_dll1_uf', 0)
Parameter('kr_notch4_dll1_uf', 0)
Parameter('kf_notch4_dll1_f1', 0)
Parameter('kr_notch4_dll1_f1', 0)
Parameter('kf_notch4_dll1_f2', 0)
Parameter('kr_notch4_dll1_f2', 0)
Parameter('kf_notch4_dll3_uf', 0)
Parameter('kr_notch4_dll3_uf', 0)
Parameter('kf_notch4_dll3_f1', 0)
Parameter('kr_notch4_dll3_f1', 0)
Parameter('kf_notch4_dll3_f2', 0)
Parameter('kr_notch4_dll3_f2', 0)
Parameter('kf_notch4_dll4_uf', 0)
Parameter('kr_notch4_dll4_uf', 0)
Parameter('kf_notch4_dll4_f1', 0)
Parameter('kr_notch4_dll4_f1', 0)
Parameter('kf_notch4_dll4_f2', 0)
Parameter('kr_notch4_dll4_f2', 0)
Parameter('kf_notch4_jag1_uf', 0)
Parameter('kr_notch4_jag1_uf', 0)
Parameter('kf_notch4_jag1_f1', 0)
Parameter('kr_notch4_jag1_f1', 0)
Parameter('kf_notch4_jag1_f2', 0)
Parameter('kr_notch4_jag1_f2', 0)
Parameter('kf_notch4_jag2_uf', 0)
Parameter('kr_notch4_jag2_uf', 0)
Parameter('kf_notch4_jag2_f1', 0)
Parameter('kr_notch4_jag2_f1', 0)
Parameter('kf_notch4_jag2_f2', 0)
Parameter('kr_notch4_jag2_f2', 0)

# rates for notch 4 binding to other receptors in golgi
Parameter('kf_notch4_notch1', 0)
Parameter('kr_notch4_notch1', 0)
Parameter('kf_notch4_notch2', 0)
Parameter('kr_notch4_notch2', 0)
Parameter('kf_notch4_notch3', 0)
Parameter('kr_notch4_notch3', 0)

# rates for notch1 o-fucosylation
Parameter('kf_notch1_rfng', 0)
Parameter('kr_notch1_rfng', 0)
Parameter('kf_notch1_lfng', 0)
Parameter('kr_notch1_lfng', 0)
Parameter('kf_notch1_mfng', 0)
Parameter('kr_notch1_mfng', 0)
Parameter('kcat_notch1_rfng', 0)
Parameter('kcat_notch1_lfng', 0)
Parameter('kcat_notch1_mfng', 0)

# rates for notch2 o-fucosylation
Parameter('kf_notch2_rfng', 0)
Parameter('kr_notch2_rfng', 0)
Parameter('kf_notch2_lfng', 0)
Parameter('kr_notch2_lfng', 0)
Parameter('kf_notch2_mfng', 0)
Parameter('kr_notch2_mfng', 0)
Parameter('kcat_notch2_rfng', 0)
Parameter('kcat_notch2_lfng', 0)
Parameter('kcat_notch2_mfng', 0)

# rates for notch3 o-fucosylation
Parameter('kf_notch3_rfng', 0)
Parameter('kr_notch3_rfng', 0)
Parameter('kf_notch3_lfng', 0)
Parameter('kr_notch3_lfng', 0)
Parameter('kf_notch3_mfng', 0)
Parameter('kr_notch3_mfng', 0)
Parameter('kcat_notch3_rfng', 0)
Parameter('kcat_notch3_lfng', 0)
Parameter('kcat_notch3_mfng', 0)

# rates for notch4 o-fucosylation
Parameter('kf_notch4_rfng', 0)
Parameter('kr_notch4_rfng', 0)
Parameter('kf_notch4_lfng', 0)
Parameter('kr_notch4_lfng', 0)
Parameter('kf_notch4_mfng', 0)
Parameter('kr_notch4_mfng', 0)
Parameter('kcat_notch4_rfng', 0)
Parameter('kcat_notch4_lfng', 0)
Parameter('kcat_notch4_mfng', 0)

# rates for notch relocating from golgi to pm
Parameter('k_notch1_golgi_to_pm', 1)
Parameter('k_notch2_golgi_to_pm', 0)
Parameter('k_notch3_golgi_to_pm', 0)
Parameter('k_notch4_golgi_to_pm', 0)

# rates for notch activation
Parameter('kcat_notch1_dll1', 1)
Parameter('kcat_notch1_dll4', 0.1)
Parameter('kcat_notch1_jag1', 0)
Parameter('kcat_notch1_jag2', 0)
Parameter('kcat_notch2_dll1', 0)
Parameter('kcat_notch2_dll4', 0)
Parameter('kcat_notch2_jag1', 0)
Parameter('kcat_notch2_jag2', 0)
Parameter('kcat_notch3_dll1', 0)
Parameter('kcat_notch3_dll4', 0)
Parameter('kcat_notch3_jag1', 0)
Parameter('kcat_notch3_jag2', 0)
Parameter('kcat_notch4_dll1', 0)
Parameter('kcat_notch4_dll4', 0)
Parameter('kcat_notch4_jag1', 0)
Parameter('kcat_notch4_jag2', 0)

# rates for nicd releasing from pm and relocating to nucleus
Parameter('k_notch1_ICD_pm_to_nuc', 0)
Parameter('k_notch2_ICD_pm_to_nuc', 0)
Parameter('k_notch3_ICD_pm_to_nuc', 0)
Parameter('k_notch4_ICD_pm_to_nuc', 0)

# rates for binding of factors of nicd transcription activation complex in the nucleus
Parameter('kf_notch1_ICD_rbpj_maml_gene1', 0)
Parameter('kr_notch1_ICD_rbpj_maml_gene1', 0)
Parameter('kf_notch2_ICD_rbpj_maml_gene1', 0)
Parameter('kr_notch2_ICD_rbpj_maml_gene1', 0)
Parameter('kf_notch3_ICD_rbpj_maml_gene1', 0)
Parameter('kr_notch3_ICD_rbpj_maml_gene1', 0)
Parameter('kf_notch4_ICD_rbpj_maml_gene1', 0)
Parameter('kr_notch4_ICD_rbpj_maml_gene1', 0)
Parameter('kf_notch1_ICD_rbpj_maml_gene2', 0)
Parameter('kr_notch1_ICD_rbpj_maml_gene2', 0)
Parameter('kf_notch2_ICD_rbpj_maml_gene2', 0)
Parameter('kr_notch2_ICD_rbpj_maml_gene2', 0)
Parameter('kf_notch3_ICD_rbpj_maml_gene2', 0)
Parameter('kr_notch3_ICD_rbpj_maml_gene2', 0)
Parameter('kf_notch4_ICD_rbpj_maml_gene2', 0)
Parameter('kr_notch4_ICD_rbpj_maml_gene2', 0)

# rates for transcription of target genes by each NTC complex
Parameter('kcat_gene1_transcription_notch1_ntc', 0)
Parameter('kcat_gene1_transcription_notch2_ntc', 0)
Parameter('kcat_gene1_transcription_notch3_ntc', 0)
Parameter('kcat_gene1_transcription_notch4_ntc', 0)
Parameter('kcat_gene2_transcription_notch1_ntc', 0)
Parameter('kcat_gene2_transcription_notch2_ntc', 0)
Parameter('kcat_gene2_transcription_notch3_ntc', 0)
Parameter('kcat_gene2_transcription_notch4_ntc', 0)

# nicd degradation rate
Parameter('k_notch1_ICD_deg', 0)
Parameter('k_notch2_ICD_deg', 0)
Parameter('k_notch3_ICD_deg', 0)
Parameter('k_notch4_ICD_deg', 0)

# rates for necd-ligand commplex degradation
Parameter('k_notch1_ecd_dll1_deg', 1)
Parameter('k_notch1_ecd_dll4_deg', 0)
Parameter('k_notch1_ecd_jag1_deg', 0)
Parameter('k_notch1_ecd_jag2_deg', 0)
Parameter('k_notch2_ecd_dll1_deg', 0)
Parameter('k_notch2_ecd_dll4_deg', 0)
Parameter('k_notch2_ecd_jag1_deg', 0)
Parameter('k_notch2_ecd_jag2_deg', 0)
Parameter('k_notch3_ecd_dll1_deg', 0)
Parameter('k_notch3_ecd_dll4_deg', 0)
Parameter('k_notch3_ecd_jag1_deg', 0)
Parameter('k_notch3_ecd_jag2_deg', 0)
Parameter('k_notch4_ecd_dll1_deg', 0)
Parameter('k_notch4_ecd_dll4_deg', 0)
Parameter('k_notch4_ecd_jag1_deg', 0)
Parameter('k_notch4_ecd_jag2_deg', 0)

#### define initials ####
Initial(NOTCH1_ICD(ecd = 1, rbpj = None, maml = None, ntc = None, loc = 'golgi') %
        NOTCH1_ECD(icd = 1, fng = None, fuc = 'uf', lig = None, loc = 'golgi'),
        notch1_init)
Initial(NOTCH2_ICD(ecd = 1, rbpj = None, maml = None, ntc = None, loc = 'golgi') %
        NOTCH2_ECD(icd = 1, fng = None, fuc = 'uf', lig = None, loc = 'golgi'),
        notch2_init)
Initial(NOTCH3_ICD(ecd = 1, rbpj = None, maml = None, ntc = None, loc = 'golgi') %
        NOTCH3_ECD(icd = 1, fng = None, fuc = 'uf', lig = None, loc = 'golgi'),
        notch3_init)
Initial(NOTCH4_ICD(ecd = 1, rbpj = None, maml = None, ntc = None, loc = 'golgi') %
        NOTCH4_ECD(icd = 1, fng = None, fuc = 'uf', lig = None, loc = 'golgi'),
        notch4_init)
Initial(DLL1(rec = None, loc = 'cis'), dll1_cis_init)
Initial(DLL1(rec = None, loc = 'trans'), dll1_trans_init)
Initial(DLL3(rec = None, loc = 'cis'), dll3_cis_init)
Initial(DLL3(rec = None, loc = 'trans'), dll3_trans_init)
Initial(DLL3(rec = None, loc = 'golgi'), dll3_golgi_init)
Initial(DLL4(rec = None, loc = 'cis'), dll4_cis_init)
Initial(DLL4(rec = None, loc = 'trans'), dll4_trans_init)
Initial(JAG1(rec = None, loc = 'cis'), jag1_cis_init)
Initial(JAG1(rec = None, loc = 'trans'), jag1_trans_init)
Initial(JAG2(rec = None, loc = 'cis'), jag2_cis_init)
Initial(JAG2(rec = None, loc = 'trans'), jag2_trans_init)
Initial(RFNG(rec = None), rfng_init)
Initial(LFNG(rec = None), lfng_init)
Initial(MFNG(rec = None), mfng_init)
Initial(RBPJ(nicd = None, maml = None, gene1 = None, gene2 = None), rbpj_init)
Initial(MAML(nicd = None, rbpj = None), maml_init)
Initial(GENE1(ntc = None), gene1_init)
Initial(GENE2(ntc = None), gene2_init)
Initial(GENE1_MRNA(), gene1_mrna_init)
Initial(GENE2_MRNA(), gene2_mrna_init)

# print(model)
# print(model.monomers)
# print(model.monomers['NOTCH3_ICD'])
# print()
# print(model.parameters)
# print()
# for ic in model.initial_conditions:
#     print(ic)

#### define rules ####
# building lists of rec, lig, and loc for looping in a list comprehension to make the binding rules
loc = ['trans', 'cis']
par = model.parameters
rec = ['NOTCH1', 'NOTCH2', 'NOTCH3', 'NOTCH4']
lig = ['DLL1', 'DLL3', 'DLL4', 'JAG1', 'JAG2']
mon = model.monomers
fng = ['RFNG', 'LFNG', 'MFNG']
fng_fuc = ['f1', 'f2', 'f2']
fuc = ['uf', 'f1', 'f2']

# rules for o-fucosylation of receptors in golgi
# notch reversibly binds fringe
[Rule('%s_binds_%s' % (y.lower(), x.lower()),
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, fng = None, fuc = 'uf', loc = 'golgi') + mon[x](rec = None) |
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, fng = 2, fuc = 'uf', loc = 'golgi') % mon[x](rec = 2),
      par['kf_%s_%s' % (y.lower(), x.lower())], par['kr_%s_%s' % (y.lower(), x.lower())])
 for y in rec for x in fng]
# notch gets o-fucosylated
[Rule('%s_fucosylates_%s' % (x.lower(), y.lower()),
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, fng = 2, fuc = 'uf', loc = 'golgi') % mon[x](rec = 2) >>
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, fng = None, fuc = fng_fuc[fng.index(x)], loc = 'golgi') + mon[x](rec = None),
      par['kcat_%s_%s' % (y.lower(), x.lower())])
 for y in rec for x in fng]

# rules for inhibitory reactions in the golgi
# notch reversibly binds dll3
[Rule('%s_with_%s_binds_dll3' % (y.lower(), x.lower()),
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, lig = None, fuc = x, loc = 'golgi') + DLL3(rec = None, loc = 'golgi') |
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, lig = 2, fuc = x, loc = 'golgi') % DLL3(rec = 2, loc = 'golgi'),
      par['kf_%s_dll3_%s' % (y.lower(), x)], par['kr_%s_dll3_%s' % (y.lower(), x)])
 for y in rec for x in fuc]
# notch4 reversibly binds to other notch receptors
[Rule('notch4_binds_%s' % y.lower(),
      NOTCH4_ICD(ecd = ANY, loc = 'golgi') % NOTCH4_ECD(icd = ANY, lig = None, loc = 'golgi') + mon[y + '_ICD'](ecd = ANY, loc = 'golgi') % mon[y + '_ECD'](icd = ANY, lig = None, loc = 'golgi') |
      NOTCH4_ICD(ecd = ANY, loc = 'golgi') % NOTCH4_ECD(icd = ANY, lig = 2, loc = 'golgi') % mon[y + '_ICD'](ecd = ANY, loc = 'golgi') % mon[y + '_ECD'](icd = ANY, lig = 2, loc = 'golgi'),
      par['kf_notch4_%s' % y.lower()], par['kr_notch4_%s' % y.lower()])
 for y in rec[0:-1]]

# relocating notch receptors from golgi to plasma membrane
[Rule('%s_goes_to_PM' % y.lower(),
      mon[y + '_ICD'](ecd = 1, loc = 'golgi') % mon[y + '_ECD'](icd = 1, lig = None, loc = 'golgi') >>
      mon[y + '_ICD'](ecd = 1, loc = 'pm') % mon[y + '_ECD'](icd = 1, lig = None, loc = 'pm'),
      par['k_%s_golgi_to_pm' % y.lower()])
 for y in rec]

# receptor ligand binding rules on pm
[Rule('%s_%s_binds_%s_%s' % (y.lower(), x, z.lower(), q),
      mon[y + '_ICD'](ecd = 1, loc = 'pm') % mon[y + '_ECD'](icd = 1, lig = None, loc = 'pm', fuc = x) + mon[z](rec = None, loc = q) |
      mon[y + '_ICD'](ecd = 1, loc = 'pm') % mon[y + '_ECD'](icd = 1, lig = 2, loc = 'pm', fuc = x) % mon[z](rec = 2, loc = q),
      par['kf_%s_%s_%s' % (y.lower(), z.lower(), x)], par['kr_%s_%s_%s' % (y.lower(), z.lower(), x)])
 for y in rec for x in fuc for z in lig for q in loc]

# notch receptor is activated on pm
[Rule('%s_activated_by_%s' % (y.lower(), z.lower()),
      mon[y + '_ICD'](ecd = 1, loc = 'pm') % mon[y + '_ECD'](icd = 1, lig = 2, loc = 'pm') % mon[z](rec = 2, loc = 'trans') >>
      mon[y + '_ICD'](ecd = None, loc = 'pm') + mon[y + '_ECD'](icd = None, lig = 2, loc = 'endo') % mon[z](rec = 2, loc = 'trans'),
      par['kcat_%s_%s' % (y.lower(), z.lower())])
 for y in rec for z in lig if z != 'DLL3']

# nicd releases from membrane and relocates to nucleus
[Rule('%s_ICD_relocates_to_nucleus' % y.lower(),
      mon[y + '_ICD'](ecd = None, loc = 'pm') >> mon[y + '_ICD'](ecd = None, loc = 'nuc'),
      par['k_%s_ICD_pm_to_nuc' % y.lower()])
 for y in rec]

# nicd binding to co-activators on target gene
[Rule('%s_ICD_binds_RBPJ_MAML_gene1' % y.lower(),
      mon[y + '_ICD'](rbpj = None, maml = None, loc = 'nuc') + RBPJ(nicd = None, maml = None, gene1 = None) + MAML(nicd = None, rbpj = None) + GENE1(ntc = None) |
      mon[y + '_ICD'](rbpj = 1, maml = 2, loc = 'nuc') % RBPJ(nicd = 1, maml = 3, gene1 = 4) % MAML(nicd = 2, rbpj = 3) % GENE1(ntc = 4),
      par['kf_%s_ICD_rbpj_maml_gene1' % y.lower()], par['kr_%s_ICD_rbpj_maml_gene1' % y.lower()])
 for y in rec]

# transcription of target gene
[Rule('gene1_transcription_under_%s_ntc' % y.lower(),
      mon[y + '_ICD'](rbpj = 1, maml = 2, loc = 'nuc') % RBPJ(nicd = 1, maml = 3, gene1 = 4) % MAML(nicd = 2, rbpj = 3) % GENE1(ntc = 4) >>
      mon[y + '_ICD'](rbpj = 1, maml = 2, loc = 'nuc') % RBPJ(nicd = 1, maml = 3, gene1 = 4) % MAML(nicd = 2, rbpj = 3) % GENE1(ntc = 4) + GENE1_MRNA(),
      par['kcat_gene1_transcription_%s_ntc' % y.lower()])
for y in rec]

# degradation of nicd in the nucleus
[Rule('%s_ICD_degradation' % y.lower(),
      mon[y + '_ICD'](rbpj = None, maml = None, loc = 'nuc') >> None,
      par['k_%s_ICD_deg' % y.lower()])
 for y in rec]

# degradation of necd-ligand complex
[Rule('%s_ECD_%s_degradation' % (y.lower(), z.lower()),
      mon[y + '_ECD'](icd = None, lig = 2, loc = 'endo') % mon[z](rec = 2, loc = 'trans') >> None,
      par['k_%s_ecd_%s_deg' % (y.lower(), z.lower())])
 for y in rec for z in lig if z != 'DLL3']

print()
print(model.rules)
print()
print(model)

# define observables
Observable('notch1_bound_all', NOTCH1_ECD(lig = ANY))
Observable('notch1_unbound_all', NOTCH1_ECD(lig = None))
Observable('dll1_trans_bound', DLL1(rec = ANY, loc = 'trans'))
Observable('notch1_bound_dll1_trans_pm', NOTCH1_ICD(ecd = ANY) % NOTCH1_ECD(icd = ANY, lig = 2) % DLL1(rec = 2, loc = 'trans'))
Observable('notch1_ecd_bound_dll1_trans', NOTCH1_ECD(icd = None, lig = 2) % DLL1(rec = 2, loc = 'trans'))

#
# # simulation commands
# tspan = np.linspace(0, 1, 101)
#
# sim = ScipyOdeSimulator(model, tspan, verbose = True)
#
# output = sim.run()
#
# plt.figure()
# for obs in model.observables:
#     plt.plot(tspan, output.observables[obs.name], lw = 2, label = obs.name)
#
# plt.xlabel('Time')
# plt.ylabel('Concentration')
# plt.legend(loc = 0)
#
# plt.show()

#
#
# # simulation commands
# tspan = np.linspace(0, 1, 101)
#
# sim = ScipyOdeSimulator(model, tspan, verbose = True)
#
# output = sim.run()
#
# plt.figure()
# for obs in model.observables:
#     plt.plot(tspan, output.observables[obs.name], lw = 2, label = obs.name)
#
# plt.xlabel('Time')
# plt.ylabel('Concentration')
# plt.legend(loc = 0)
#
# # this is how we get an array of one species' concentration
# print(output.species[:, 0])
# # this is how to get the names of all of the species in the model
# for sp in model.species:
#     print(sp)
#
#
# plt.figure()
# for i, sp in enumerate(model.species):
#     plt.plot(tspan, output.species[:, i], lw = 2, label = str(model.species[i]))
# plt.xlabel('Time')
# plt.ylabel('Concentration')
# plt.legend(loc = 0)
#
# plt.show()
#
#

