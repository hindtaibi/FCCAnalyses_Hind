import ROOT

inputDir       = "../final/outputs/"
outdir         = "outputs"

# global parameters
intLumi        =  5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = "ZH #rightarrow ZZZ #rightarrow #mu^{+}#mu^{-}/e^{+}e^{-} + #mu^{+}#mu^{-}/e^{+}e^{-} + xx"
delphesVersion = "3.4.2"
energy         =  240.0
collider       = "FCC-ee"
formats        = ['png']
yaxis          = ['log']
stacksig       = ['stack']

variables = ['N_photons',
             'photons_e',
             'photons_p',

             'Z1_e',
             'Z1_m',
             'Z1_p',
             'Z1_theta',
             'Z1_phi', 
             'Z1_eta', 
             'Z1_y',
             'Z1_recoil_m', 
             
             'Z2_e',
             'Z2_m',
             'Z2_p',
             'Z2_theta',
             'Z2_phi',
             'Z2_eta',
             'Z2_y',
             'Z2_recoil_m',

             'N_on_taken_leptons',
             'N_off_taken_leptons',

             'on_taken_leptons_e',
             'on_taken_leptons_p',
             'on_taken_leptons_phi',
             'on_taken_leptons_theta',
             'on_taken_leptons_m',
             'on_taken_leptons_recoil_m',

             'off_taken_leptons_e',
             'off_taken_leptons_p',
             'off_taken_leptons_phi',
             'off_taken_leptons_theta',
             'off_taken_leptons_m',
             'off_taken_leptons_recoil_m',

             'N_LooseLeptons_10',
             'N_LooseLeptons_2',
             'N_LooseLeptons_1',
             'LooseLeptons_10_p',
             'LooseLeptons_10_pt',
             'LooseLeptons_10_theta',
             'LooseLeptons_10_phi',

             'on_difftheta1_muons',
             'on_difftheta2_muons',
             'on_difftheta1_electrons',
             'on_difftheta2_electrons',
             'on_diffphi1_muons',
             'on_diffphi2_muons',
             'on_diffphi1_electrons',
             'on_diffphi2_electrons',
             'off_difftheta_muons',
             'off_difftheta_electrons',
             'off_diffphi_muons',
             'off_diffphi_electrons',

             'emiss', 
             'pxmiss', 
             'pymiss', 
             'pzmiss', 
             'etmiss',

             'visible_mass_predef'
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['llllxx']   = ["sel0","sel1","sel2","sel3"]#, "sel4", "sel5", "sel6", "sel7"]

extralabel = {}
extralabel['sel0'] = "No cut"
extralabel['sel1'] = "emiss < 10"
extralabel['sel2'] = "Z1 mass"
extralabel['sel3'] = "Z1 & Z2 mass"
#extralabel['sel4'] = "2nd dilepton m"
#extralabel['sel5'] = "Dijet m"
#extralabel['sel6'] = "Dileptons m + dijet m"
#extralabel['sel7'] = "emiss < 10 + dileptons m + dijet m"



colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['HWW'] = ROOT.kGreen
colors['nunuH,HZZ'] = ROOT.kBlue
#colors['WW'] = ROOT.kOrange+6
#colors['ZZ'] = ROOT.kOrange-2
colors['Htautau'] = ROOT.kCyan+2
colors['Hqq'] = ROOT.kPink-9
colors['Hmumu'] = ROOT.kViolet
colors['HZa'] = ROOT.kOrange+6
#colors['VV'] = ROOT.kGreen+3

plots = {}                                  
plots['llllxx'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                         'wzp6_ee_eeH_HZZ_ecm240']},

                   'backgrounds':{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                         'wzp6_ee_eeH_HWW_ecm240'],

                                  'nunuH,HZZ':['wzp6_ee_nunuH_HZZ_ecm240'],
 
                                  'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 
                                             'wzp6_ee_eeH_Htautau_ecm240'],
                                   
                                  'Hqq':['wzp6_ee_mumuH_Hbb_ecm240', 
                                         'wzp6_ee_eeH_Hbb_ecm240',
                                         'wzp6_ee_mumuH_Hss_ecm240',
                                         'wzp6_ee_eeH_Hss_ecm240',
                                         'wzp6_ee_mumuH_Hcc_ecm240',
                                         'wzp6_ee_eeH_Hcc_ecm240'],

                                  'Hmumu':['wzp6_ee_mumuH_Hmumu_ecm240', 
                                           'wzp6_ee_eeH_Hmumu_ecm240'],
 
                                  'HZa':['wzp6_ee_mumuH_HZa_ecm240', 
                                         'wzp6_ee_eeH_HZa_ecm240']}
                  }
                                         

legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['HWW'] = 'H#rightarrowWW'
legend['nunuH,HZZ'] = '#nu#nuH, HZZ'
#legend['WW'] = 'WW'
#legend['ZZ'] = 'ZZ'
legend['Htautau'] = 'H#rightarrow#tau#tau'
legend['Hqq'] = 'H#rightarrowqq (bb, ss, cc)'
legend['Hmumu'] = 'H#rightarrow#mu#mu'
legend['HZa'] = 'H#rightarrowZa'
#legend['Mee'] = 'Mee'
#legend['VV'] = 'VV boson'

