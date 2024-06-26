import ROOT

inputDir       = "../final/outputs/"
outdir         = "outputs"

# global parameters
intLumi        =  5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = "ZH #rightarrow ZZZ #rightarrow #mu^{+}#mu^{-}/e^{+}e^{-} + #mu^{+}#mu^{-}/e^{+}e^{-} + jj"
delphesVersion = "3.4.2"
energy         =  240.0
collider       = "FCC-ee"
formats        = ['png']
yaxis          = ['log']
stacksig       = ['stack']

variables = ['N_photons',
             'photons_e',
             'photons_p',

             'Z1_m',
             'Z1_p',
             'Z1_theta',
             'Z1_phi', 
             'Z1_eta', 
             'Z1_y',
             'Z1_recoil_m', 
                
             'Z2_m',
             'Z2_p',
             'Z2_theta',
             'Z2_phi',
             'Z2_eta',
             'Z2_y',
             'Z2_recoil_m',

             'Z3_m',
             'Z3_p',
             'Z3_px',
             'Z3_py',
             'Z3_pz' ,
             'Z3_pt',

             'N_zed_leptonic',

             'selected_muons_e', 
             'selected_electrons_e', 
             'selected_leptons_e', 

             'selected_muons_p', 
             'selected_electrons_p' , 
             'selected_leptons_p', 

             'selected_muons_px', 
             'selected_electrons_px' , 
             'selected_leptons_px', 

             'selected_muons_py', 
             'selected_electrons_py' , 
             'selected_leptons_py', 

             'selected_muons_pz', 
             'selected_electrons_pz' , 
             'selected_leptons_pz', 

             'selected_muons_pt', 
             'selected_electrons_pt' , 
             'selected_leptons_pt',

             'N_selected_leptons', 

             'N_LooseLeptons_10',
             'N_LooseLeptons_2',
             'N_LooseLeptons_1',
             'LooseLeptons_10_p',
             'LooseLeptons_10_pt',
             'LooseLeptons_10_theta',
             'LooseLeptons_10_phi',

             "zed_leptons_difftheta1",
             "zed_leptons_difftheta2",
             "zed_leptons_diffphi1",
             "zed_leptons_diffphi2",

             "taken_leptons_e",
             "taken_leptons_p",
             "taken_leptons_phi",
             "taken_leptons_theta",
             "taken_leptons_m",
             "taken_leptons_recoil_m",
             
             'j5_p', 
             'j6_p', 

             'j5_px', 
             'j6_px', 

             'j5_py', 
             'j6_py' , 

             'j5_pz', 
             'j6_pz', 

             'j5_e', 
             'j6_e', 

             'j5_pt', 
             'j6_pt', 

             'j5_theta', 
             'j6_theta',

             'j5_phi',
             'j6_phi',

             'j5_const', 
             'j6_const', 
             
             'diffthetajets_56',
             'diffphijets_56',

             "missing_theta",
             "angle_miss_j5",
             "angle_miss_j6",
             "min_angle_miss_jet",
             "max_angle_miss_jet",

             'dmerge_2_12', 
             'dmerge_2_23', 
             'dmerge_2_34', 
             'dmerge_2_45', 
             
             'ja_p',
             'jb_p',
             'jc_p',

             'ja_e',
             'jb_e',
             'jc_e',

             "min_const_3",
             "max_const_3",
             "mean_const_3",

             "diffthetajets_ab",
             "diffthetajets_bc",
             "diffthetajets_ac",

             "dmerge_3_12",
             "dmerge_3_23",
             "dmerge_3_34",
             "dmerge_3_45",


             'emiss', 
             'pxmiss', 
             'pymiss', 
             'pzmiss', 
             'etmiss', 
             'visible_mass_predef'
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['lllljj']   = ["sel0" ,"sel1","sel2","sel3"]#, "sel4", "sel5", "sel6", "sel7"]

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
plots['lllljj'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
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

