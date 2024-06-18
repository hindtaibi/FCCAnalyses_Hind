import ROOT

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
stacksig       = ['stack']

variables = ['emiss',
    	     'pxmiss',
             'pymiss',
	         'pzmiss',
	         "photon_e",
	         "photon_theta",
	         "photon_phi",
             "Za_e",
             "Za_p",
             "Za_px",
             "Za_py",
             "Za_pz",
             "Za_theta",
             "Za_phi",
             "Za_m",
             "Za_recoil_m",
             "Zb_e",
             "Zb_p",
             "Zb_px",
             "Zb_py",
             "Zb_pz",
             "Zb_theta",
             "Zb_phi",
             "Zb_m",
             "Zb_recoil_m",
             "jj_e",
             "jj_p",
             "jj_px",
             "jj_py",
             "jj_pz",
             "jj_theta",
             "jj_phi",
             "jj_m",
	         "ll1a_m",
	         "ll2a_m",
             #"ll1a_ll1_m",
             #"ll2a_ll2_m",
	         "ll1jj_m",
	         "ll2jj_m",
	         "ll1miss_m",
	         "ll2miss_m",
	         "ll1_theta_diff",
	         "ll1_phi_diff",
	         "ll2_theta_diff",
	         "ll2_phi_diff",
	         "diffthetajets_34",
	         "diffphijets_34"
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['finalBA']   = ["precuts", 
                           "precuts_emiss",
                           "precuts_emiss_jj_m",
                           "precuts_emiss_jj_m_Za_recoil"]

extralabel = {}
extralabel["precuts"] = "Precuts: 2 leptonic Z: 20 < m^{b}_{ll} < 80 and 80 < m^{a}_{ll} < 110"
extralabel["precuts_emiss"] = "Precuts + emiss < 8"
extralabel["precuts_emiss_jj_m"] = "Precuts + emiss < 8 + jj_m > 5"
extralabel["precuts_emiss_jj_m_Za_recoil"] = "Precuts + emiss < 8 + jj_m > 5 + Za_recoil > 120"


colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['HWW'] = ROOT.kGreen
colors['nunuH,HZZ'] = ROOT.kBlue
colors['Hgg'] = ROOT.kYellow
#colors['nunuH,Hbb'] = ROOT.kOrange-2
colors['Htautau'] = ROOT.kCyan+2
colors['Hqq'] = ROOT.kPink-9
colors['Hmumu'] = ROOT.kViolet
colors['HZa'] = ROOT.kOrange+6
#colors['Haa'] = ROOT.kGreen+3
colors['ZZ'] = ROOT.kAzure+6

plots = {}                                  
plots['finalBA'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                              'wzp6_ee_eeH_HZZ_ecm240']},

                   'backgrounds':{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                         'wzp6_ee_eeH_HWW_ecm240'],
 
                                  'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 
                                             'wzp6_ee_eeH_Htautau_ecm240'],
 
                                  'Hmumu':['wzp6_ee_mumuH_Hmumu_ecm240', 
                                           'wzp6_ee_eeH_Hmumu_ecm240'],
 
                                  'HZa':['wzp6_ee_mumuH_HZa_ecm240', 
                                         'wzp6_ee_eeH_HZa_ecm240'],
                                         
                                  'nunuH,HZZ':['wzp6_ee_nunuH_HZZ_ecm240'],
                                  
                                  'Hqq':['wzp6_ee_mumuH_Hbb_ecm240', 
                                         'wzp6_ee_eeH_Hbb_ecm240',
                                         'wzp6_ee_eeH_Hss_ecm240',
                                         'wzp6_ee_mumuH_Hcc_ecm240',
                                         'wzp6_ee_eeH_Hcc_ecm240'],
                                  
                                  'Hgg':['wzp6_ee_mumuH_Hgg_ecm240',
                                         'wzp6_ee_eeH_Hgg_ecm240'],
                                  
                                  'ZZ':['p8_ee_ZZ_ecm240']
                                  }
                   }         

legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['HWW'] = 'H#rightarrowWW'
legend['nunuH,HZZ'] = '#nu#nuH, HZZ'
#legend['nunuH,Hbb'] = '#nu#nuH, Hbb'
legend['Htautau'] = 'H#rightarrow#tau#tau'
legend['Hmumu'] = 'H#rightarrow#mu#mu'
legend['HZa'] = 'H#rightarrowZa'
legend['Hqq'] = 'H#rightarrowqq (bb, ss, cc)'
legend['Hgg'] = 'Hgg'
#legend['Haa'] = 'Haa'
legend['ZZ'] = 'ZZ'
