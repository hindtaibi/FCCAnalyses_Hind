import ROOT

#Takes as input the output of finalBA
inputDir       = "../finalBA/outputs/"
outdir         = "outputs"

# global parameters
intLumi        =  5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = "ZH #rightarrow ZZZ"
delphesVersion = "3.4.2"
energy         =  240.0
collider       = "FCC-ee"
formats        = ['png']
yaxis          = ['log']
stacksig       = ["nostack"]

variables = ["photon_e",
             "photon_px",
             "photon_py",
             "photon_pz",
             "photon_theta",
             "photon_phi",
             "photon_eta",
             "ll1a_recoil_m",
             "ll2a_recoil_m",
             "ll1jj_m",
             "ll2jj_m",
             "ll2jj_recoil_m",
             "ll1miss_m",
             "ll2miss_m",
             "ZZ_m",
             "ZZ_m_zoom",
             "ZZ_recoil_m",
             "Za_e",
             "Za_p",
             "Za_px",
             "Za_py",
             "Za_pz",
             "Za_theta",
             "Za_phi",
             "Za_m",
             "Za_recoil_m",
             "Za_eta",
             "Zb_e",
             "Zb_p",
             "Zb_px",
             "Zb_py",
             "Zb_pz",
             "Zb_theta",
             "Zb_phi",
             "Zb_m",
             "Zb_recoil_m",
             "Zb_eta",
             "jj_e",
             "jj_p",
             "jj_px",
             "jj_py",
             "jj_pz",
             "jj_theta",
             "jj_phi",
             "jj_m",
             "jj_eta",
             "j1_e",
             "j1_p",
             "j1_px",
             "j1_py",
             "j1_pz",
             "j1_theta",
             "j1_phi",
             "j1_m",
             "j1_eta",
             "j2_e",
             "j2_p",
             "j2_px",
             "j2_py",
             "j2_pz",
             "j2_theta",
             "j2_phi",
             "j2_m",
             "j2_eta",
             "emiss",
             "etmiss",
             "pxmiss",
             "pymiss",
             "pzmiss",
             "visible_m",
             "missing_theta",
             "Za_recoil_m_zoom",
             "Zb_recoil_m_zoom",
             "jj_recoil_m",
             "ll2jj_m_zoom",
             
             "ll1_angle",
             "ll1_theta_diff",
             "ll1_phi_diff",
             "ll1_delta_R",
             "ll2_angle",
             "ll2_theta_diff",
             "ll2_phi_diff",
             "ll2_delta_R",
             "lj1_theta_diff_min",
             "lj1_phi_diff_min",
             "lj1_delta_R_min",
             "lj2_theta_diff_min",
             "lj2_phi_diff_min",
             "lj2_delta_R_min",
             "ZZ_p",
             "Zbmiss_m",

             "ll2jj_m_fit",
             "ZZ_m_fit"
             ]

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['finalBA']   = ["precuts",
                           "precuts_Za_m",
                           "precuts_Za_m_Zb_m",
                           "precuts_Za_m_Zb_m_emiss",

                           "lljjll",
                           "lljjll_jj_m",
                           "lljjll_jj_m_Zb_recoil_m",
                           "lljjll_jj_m_Zb_recoil_m_ll2jj_recoil_m",
                           
                           "jjllll",
                           "jjllll_jj_m",
                           "jjllll_jj_m_Zb_recoil_m",

                           "region1",
                           "region2",

                           "fitRegion1",
                           "fitRegion2"
                           ]

extralabel = {}
extralabel["precuts"] = "Sel 0_{B}"
extralabel["precuts_Za_m"] = "Sel 1_{B}"
extralabel["precuts_Za_m_Zb_m"] = "Sel 2_{B}"
extralabel["precuts_Za_m_Zb_m_emiss"] = "Sel 3_{BA}"

extralabel["lljjll"] = "Sel 4_{BAA}"
extralabel["lljjll_jj_m"] = "Sel 5_{BAA}"
extralabel["lljjll_jj_m_Zb_recoil_m"] = "Sel 6_{BAA}"
extralabel["lljjll_jj_m_Zb_recoil_m_ll2jj_recoil_m"] = "Sel 7_{BAA}"

extralabel["jjllll"] = "Sel 4_{BAB}"
extralabel["jjllll_jj_m"] = "Sel 5_{BAB}"
extralabel["jjllll_jj_m_Zb_recoil_m"] = "Sel 6_{BAB}"

extralabel["region1"] = "Sel 7_{BAA}"
extralabel["region2"] = "Sel 6_{BAB}"

extralabel["fitRegion1"] = "Sel lljjll"
extralabel["fitRegion2"] = "Sel jjllll"



colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['HWW'] = ROOT.kGreen
colors['Hgg'] = ROOT.kYellow
colors['Htautau'] = ROOT.kCyan+2
colors['Hqq'] = ROOT.kPink-4
colors['Hmumu'] = ROOT.kViolet
colors['HZa'] = ROOT.kOrange+7
colors['ZZ'] = ROOT.kAzure+6
colors['WW'] = ROOT.kBlue

plots = {}                                  
plots['finalBA'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                            'wzp6_ee_eeH_HZZ_ecm240',
                                            'wzp6_ee_qqH_HZZ_ecm240',
                                            'wzp6_ee_ssH_HZZ_ecm240',
                                            'wzp6_ee_bbH_HZZ_ecm240',
                                            'wzp6_ee_ccH_HZZ_ecm240',
                                            'wzp6_ee_nunuH_HZZ_ecm240',
                                            'wzp6_ee_tautauH_HZZ_ecm240']},

                   'backgrounds':{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                         'wzp6_ee_eeH_HWW_ecm240'],
 
                                  'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 
                                             'wzp6_ee_eeH_Htautau_ecm240'],
 
                                  'Hmumu':['wzp6_ee_mumuH_Hmumu_ecm240', 
                                           'wzp6_ee_eeH_Hmumu_ecm240'],
 
                                  'HZa':['wzp6_ee_mumuH_HZa_ecm240', 
                                         'wzp6_ee_eeH_HZa_ecm240'],
                                  
                                  'Hqq':['wzp6_ee_mumuH_Hbb_ecm240', 
                                         'wzp6_ee_eeH_Hbb_ecm240',
                                         'wzp6_ee_eeH_Hss_ecm240',
                                         'wzp6_ee_mumuH_Hcc_ecm240',
                                         'wzp6_ee_eeH_Hcc_ecm240'],
                                  
                                  'Hgg':['wzp6_ee_mumuH_Hgg_ecm240',
                                         'wzp6_ee_eeH_Hgg_ecm240'],

                                  'ZZ':['p8_ee_ZZ_ecm240'],
                                  
                                  'WW':['p8_ee_WW_ecm240']
                                  }
                   }         

legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['HWW'] = 'ZH(WW)'
legend['ZZ'] = 'ZZ'
legend['Htautau'] = 'ZH(#tau#tau)'
legend['Hmumu'] = 'ZH(#mu#mu)'
legend['HZa'] = 'ZH(Z#gamma)'
legend['Hqq'] = 'ZH(qq)'
legend['WW'] = 'WW'
legend['Hgg'] = 'ZH(gg)'
