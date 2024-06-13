import ROOT

inputDir       = "../finalAB/outputs/"
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
	         "on_lla_inv_m",
	         "other_lla_inv_m",
	         "Za_e",
	         "Za_p",
	         "Za_px",
	         "Za_py",
	         "Za_pz",
	         "Za_theta",
	         "Za_phi",
	         "Za_m",
	         "Za_recoil_m",
	         "on_ll_theta_diff",
	         "on_ll_phi_diff",
	         "Zb_e",
	         "Zb_p",
	         "Zb_px",
	         "Zb_py",
	         "Zb_pz",
	         "Zb_theta",
	         "Zb_phi",
	         "Zb_m",
	         "Zb_recoil_m",
	         "other_ll_theta_diff",
	         "other_ll_phi_diff",
	         "jj_e",
	         "jj_p",
	         "jj_px",
	         "jj_py",
	         "jj_pz",
	         "jj_theta",
	         "jj_phi",
	         "jj_m",
	         "diffthetajets_56",
	         "diffphijets_56"
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['finalAB']   = ["precuts", 
                           "precuts_emiss"]

extralabel = {}
extralabel["precuts"] = "Precuts: 2 leptonic Z and 80 < m_{ll}_{b} < 110"
extralabel["precuts_emiss"] = "Precuts + emiss > 8"


colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['HWW'] = ROOT.kGreen
#colors['nunuH,HZZ'] = ROOT.kBlue
#colors['Hgg'] = ROOT.kYellow
#colors['ZZ'] = ROOT.kOrange-2
colors['Htautau'] = ROOT.kCyan+2
#colors['Hqq'] = ROOT.kPink-9
colors['Hmumu'] = ROOT.kViolet
colors['HZa'] = ROOT.kOrange+6
#colors['VV'] = ROOT.kGreen+3

plots = {}                                  
plots['finalAB'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                              'wzp6_ee_eeH_HZZ_ecm240']},

                   'backgrounds':{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                         'wzp6_ee_eeH_HWW_ecm240'],
 
                                  'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 
                                             'wzp6_ee_eeH_Htautau_ecm240'],
 
                                  'Hmumu':['wzp6_ee_mumuH_Hmumu_ecm240', 
                                           'wzp6_ee_eeH_Hmumu_ecm240'],
 
                                  'HZa':['wzp6_ee_mumuH_HZa_ecm240', 
                                         'wzp6_ee_eeH_HZa_ecm240']
                                  }
                   }         

legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['HWW'] = 'H#rightarrowWW'
#legend['ZZ'] = 'ZZ'
legend['Htautau'] = 'H#rightarrow#tau#tau'
legend['Hmumu'] = 'H#rightarrow#mu#mu'
legend['HZa'] = 'H#rightarrowZa'
#legend['Mee'] = 'Mee'
#legend['VV'] = 'VV boson'
