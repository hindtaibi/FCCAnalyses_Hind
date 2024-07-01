import ROOT

inputDir       = "../finalBB/outputs/"
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
	     "ll1a_recoil_m",
	         "ll2a_recoil_m",
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
	         "diffphijets_34",
             "visible_m"
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['finalBB']   = ["precuts", 
                           "precuts_Za_m",
                           "precuts_Za_m_Zb_m",
                           "precuts_Za_m_Zb_m_emiss"]

extralabel = {}
extralabel["precuts"] = "Precuts: 1 on shell and 1 off shell leptonic Z"
extralabel["precuts_Za_m"] = "Precuts + 80 < m(Z_{a}) < 110"
extralabel["precuts_Za_m_Zb_m"] = "Precuts + 80 < m(Z_{a}) < 110 + 20 < m(Z_{b}) < 80"
extralabel["precuts_Za_m_Zb_m_emiss"] = "Precuts + 80 < m(Z_{a}) < 110 + 20 < m(Z_{b}) < 80 + emiss > 8"


colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['HWW'] = ROOT.kGreen
#colors['nunuH,HZZ'] = ROOT.kBlue
colors['Hgg'] = ROOT.kYellow
colors['nunuH,Hbb'] = ROOT.kGreen+3
colors['Htautau'] = ROOT.kCyan+2
colors['Hqq'] = ROOT.kPink-4
colors['Hmumu'] = ROOT.kViolet
colors['HZa'] = ROOT.kOrange+7
colors['ZZ'] = ROOT.kAzure+6
colors['WW'] = ROOT.kGray+1

plots = {}                                  
plots['finalBB'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                              'wzp6_ee_eeH_HZZ_ecm240',
                                              'wzp6_ee_qqH_HZZ_ecm240',
                                              'wzp6_ee_ssH_HZZ_ecm240',
                                              'wzp6_ee_bbH_HZZ_ecm240',
                                              'wzp6_ee_ccH_HZZ_ecm240',
					      'wzp6_ee_nunuH_HZZ_ecm240']},

                   'backgrounds':{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                         'wzp6_ee_eeH_HWW_ecm240'],
 
                                  'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 
                                             'wzp6_ee_eeH_Htautau_ecm240'],
 
                                  'Hmumu':['wzp6_ee_mumuH_Hmumu_ecm240', 
                                           'wzp6_ee_eeH_Hmumu_ecm240'],
 
                                  'HZa':['wzp6_ee_mumuH_HZa_ecm240', 
                                         'wzp6_ee_eeH_HZa_ecm240'],
                                         
                                  'nunuH,Hbb':['wzp6_ee_nunuH_Hbb_ecm240'],
                                  
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
legend['HWW'] = 'H#rightarrowWW'
#legend['nunuH,HZZ'] = '#nu#nuH, HZZ'
legend['nunuH,Hbb'] = '#nu#nuH, Hbb'
legend['Htautau'] = 'H#rightarrow#tau#tau'
legend['Hmumu'] = 'H#rightarrow#mu#mu'
legend['HZa'] = 'H#rightarrowZa'
legend['Hqq'] = 'H#rightarrowqq'
legend['Hgg'] = 'H#rightarrowgg'
legend['ZZ'] = 'ZZ'
legend['WW'] = 'WW'
