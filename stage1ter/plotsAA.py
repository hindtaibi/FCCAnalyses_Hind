import ROOT

inputDir       = "../finalAA/outputs/"
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
stacksig       = ['nostack']

#Variables to plot
variables = [
                #---------------------------------Photons
                "photon_e",
                "photon_px",
                "photon_py",
                "photon_pz",
                "photon_theta",
                "photon_phi",
                "photon_eta",
                #---------------------------------Missing/Visible
                "emiss",
                "pxmiss",
                "pymiss",
                "pzmiss",
                "etmiss",
                "missing_theta",
                "visible_m",
                #---------------------------------Dijet
                "jj_e",
                "jj_p",
                "jj_px",
                "jj_py",
                "jj_pz",
                "jj_pt",
                "jj_theta",
                "jj_phi",
                "jj_eta",
                "jj_m",
                #---------------------------------j1
                "j1_e",
                "j1_p",
                "j1_px",
                "j1_py",
                "j1_pz",
                "j1_pt",
                "j1_theta",
                "j1_phi",
                "j1_eta",
                "j1_m",
                #---------------------------------j2
                "j2_e",
                "j2_p",
                "j2_px",
                "j2_py",
                "j2_pz",
                "j2_pt",
                "j2_theta",
                "j2_phi",
                "j2_eta",
                "j2_m",
                #---------------------------------Z1
                "Z1_m",
                "Z1_recoil_m",
                "Z1_theta",
                "Z1_phi",
                "Z1_eta",
                "Z1_e",
                "Z1_p",
                "Z1_px",
                "Z1_py",
                "Z1_pz",
                "Z1a_recoil_m",
                #---------------------------------Z2
                "Z2_m",
                "Z2_recoil_m",
                "Z2_theta",
                "Z2_phi",
                "Z2_eta",
                "Z2_e",
                "Z2_p",
                "Z2_px",
                "Z2_py",
                "Z2_pz",
                "Z2a_recoil_m",
                "Z2jj_m",
                "Z2miss_m",
                #---------------------------------Zoom
                "Z1_recoil_m_zoom",
                "Z2_recoil_m_zoom",
                #---------------------------------Combine
                "Z1_recoil_m_fit"
                
                ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['finalAA']   = ["precuts", 
                           "precuts_Z1_m",
                           "precuts_Z1_m_Z2_m",
                           "precuts_Z1_m_Z2_m_emiss",
                           "precuts_Z1_m_Z2_m_emiss_photon_e",
                           "precuts_Z1_m_Z2_m_emiss_photon_e_Z2a_recoil_m",   
                           "region1",
                           'fitRegion'
                           ]


extralabel = {}
extralabel["precuts"] = "Sel 0_{A}"
extralabel["precuts_Z1_m"] = "Precuts + 80 < m(Z_{1}) < 110"
extralabel["precuts_Z1_m_Z2_m"] = "Sel 1_{A}"
extralabel["precuts_Z1_m_Z2_m_emiss"] = "Sel 2_{AA}"
extralabel["precuts_Z1_m_Z2_m_emiss_photon_e"] = "Sel 3_{AA}"
extralabel["precuts_Z1_m_Z2_m_emiss_photon_e_Z2a_recoil_m"] = "Sel 4_{AA}"
extralabel["region1"] = "Sel 4_{AA}"
extralabel["fitRegion"] = "Sel lllljj"


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
plots['finalAA'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                            'wzp6_ee_eeH_HZZ_ecm240',
                                            'wzp6_ee_ccH_HZZ_ecm240',
                                            'wzp6_ee_ssH_HZZ_ecm240',
                                            'wzp6_ee_qqH_HZZ_ecm240',
                                            'wzp6_ee_bbH_HZZ_ecm240',
                                            'wzp6_ee_nunuH_HZZ_ecm240',
                                            'wzp6_ee_tautauH_HZZ_ecm240']},

                   'backgrounds':{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                         'wzp6_ee_eeH_HWW_ecm240'],
 
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
                                         'wzp6_ee_eeH_HZa_ecm240'],

                                  'Hgg':['wzp6_ee_mumuH_Hgg_ecm240',
                                         'wzp6_ee_eeH_Hgg_ecm240'],

				                  'ZZ':['p8_ee_ZZ_ecm240'],

                                  'WW':['p8_ee_WW_ecm240']
                                  }
                   }         

legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['HWW'] = 'Z,H(WW)'
legend['ZZ'] = 'ZZ'
legend['Htautau'] = 'Z,H(#tau#tau)'
legend['Hmumu'] = 'Z,H(#mu#mu)'
legend['HZa'] = 'Z,H(Z#gamma)'
legend['Hqq'] = 'Z,H(qq)'
legend['WW'] = 'WW'
legend['Hgg'] = 'Z,H(gg)'
