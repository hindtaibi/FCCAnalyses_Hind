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
             "visible_m",
	         "ll1a_m",
	         "ll2a_m",
             "N_on_extra_leptons",
             "N_other_extra_leptons",
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
	         "diffthetajets_56",
	         "diffphijets_56"
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['SignalOnlyB'] = ["precuts"]

extralabel = {}
extralabel["precuts"] = "Precuts: 1 on shell leptonic Z & 1 pff shell leptonic Z"


colors = {}
colors['Signal,HZZ'] = ROOT.kRed
#colors['HWW'] = ROOT.kGreen
#colors['nunuH,HZZ'] = ROOT.kBlue
#colors['Hgg'] = ROOT.kYellow
#colors['ZZ'] = ROOT.kOrange-2
#colors['Htautau'] = ROOT.kCyan+2
#colors['Hqq'] = ROOT.kPink-9
#colors['Hmumu'] = ROOT.kViolet
#colors['HZa'] = ROOT.kOrange+6
#colors['ZZ'] = ROOT.kAzure+6

plots = {}                                  
plots['SignalOnlyB'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                                'wzp6_ee_eeH_HZZ_ecm240',
                                                'wzp6_ee_nunuH_HZZ_ecm240',
                                                'wzp6_ee_qqH_HZZ_ecm240',
                                                'wzp6_ee_qqH_HZZ_ecm240',
                                                'wzp6_ee_bbH_HZZ_ecm240',
                                                'wzp6_ee_ccH_HZZ_ecm240']},

                       'backgrounds':{}
                   }         

legend = {}
legend['Signal,HZZ'] = 'Signal'
#legend['HWW'] = 'H#rightarrowWW'
#legend['ZZ'] = 'ZZ'
#legend['Htautau'] = 'H#rightarrow#tau#tau'
#legend['Hmumu'] = 'H#rightarrow#mu#mu'
#legend['HZa'] = 'H#rightarrowZa'
#legend['Hqq'] = 'H#rightarrowqq'
#legend['Hgg'] = 'Hgg'
#legend['Mee'] = 'Mee'
#legend['VV'] = 'VV boson'
