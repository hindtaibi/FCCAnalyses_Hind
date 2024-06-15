import ROOT

inputDir       = "../final/outputs/"
outdir         = "outputs"

# global parameters
intLumi        =  5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = "ZH #rightarrow ZZZ #rightarrow #mu^{+}#mu^{-}/e^{+}e^{-} + #mu^{+}#mu^{-}/e^{+}e^{-} + #mu^{+}#mu^{-}/e^{+}e^{-}"
delphesVersion = "3.4.2"
energy         =  240.0
collider       = "FCC-ee"
formats        = ['png']
yaxis          = ['log']
stacksig       = ['stack']

variables = ['N_photons',
             'photons_e',
             'photons_px',
             'photons_py',
             'photons_pz',
             'photons_pt',
             'photons_phi',
             'photons_theta',

             'Z1_e',
             'Z1_m',
             'Z1_p',
             'Z1_theta',
             'Z1_phi', 
             'Z1_recoil_m', 
             
             'Z2_e',
             'Z2_m',
             'Z2_p',
             'Z2_theta',
             'Z2_phi',
             'Z2_recoil_m',
             
             'Z2_e',
             'Z2_m',
             'Z2_p',
             'Z2_theta',
             'Z2_phi',
             'Z2_recoil_m',
             
             'on_difftheta1_muons',
             'on_difftheta2_muons',
             'on_difftheta1_electrons',
             'on_difftheta2_electrons',
             'on_diffphi1_muons',
             'on_diffphi2_muons',
             'on_diffphi1_electrons',
             'on_diffphi2_electrons',
             "off_difftheta_muons",
             "off_difftheta_electrons",
             "off_diffphi_muons",
             "off_diffphi_electrons",
             
             'N_LooseLeptons_10',
             'N_LooseLeptons_2',
             'N_LooseLeptons_1',
             'LooseLeptons_10_p',
             'LooseLeptons_10_e',
             'LooseLeptons_10_theta',
             'LooseLeptons_10_phi',

             'N_all_taken_leptons',
             "all_taken_leptons_e",
             "all_taken_leptons_p",
             "all_taken_leptons_theta",
             "all_taken_leptons_phi",
                       
             'emiss', 
             'pxmiss', 
             'pymiss', 
             'pzmiss', 
             'etmiss',

             'visible_mass_predef'
             ]


###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['llllll']   = ["sel0"]

extralabel = {}
extralabel['sel0'] = "No cut"
#extralabel['sel1'] = "emiss < 8"
#extralabel['sel2'] = "Z1 mass"
#extralabel['sel3'] = "Z1 & Z2 mass"
#extralabel['sel4'] = "Z1, Z2 & Z3 mass"
#extralabel['sel5'] = "Dijet m"
#extralabel['sel6'] = "Dileptons m + dijet m"
#extralabel['sel7'] = "emiss < 10 + dileptons m + dijet m"



colors = {}
colors['Signal,HZZ'] = ROOT.kRed
#colors['HWW'] = ROOT.kGreen
#colors['nunuH,HZZ'] = ROOT.kBlue
#colors['WW'] = ROOT.kOrange+6
#colors['ZZ'] = ROOT.kOrange-2
#colors['Htautau'] = ROOT.kCyan+2
#colors['Hqq'] = ROOT.kPink-9
#colors['Hmumu'] = ROOT.kViolet
#colors['HZa'] = ROOT.kOrange+6
#colors['VV'] = ROOT.kGreen+3

plots = {}                                  
plots['llllll'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240',
                                           'wzp6_ee_eeH_HZZ_ecm240']},

                   'backgrounds':{}#'HWW':['wzp6_ee_mumuH_HWW_ecm240', 
                                    #     'wzp6_ee_eeH_HWW_ecm240']}
                  }
                                         

legend = {}
legend['Signal,HZZ'] = 'Signal'
#legend['HWW'] = 'H#rightarrowWW'
#legend['nunuH,HZZ'] = '#nu#nuH, HZZ'
#legend['WW'] = 'WW'
#legend['ZZ'] = 'ZZ'
#legend['Htautau'] = 'H#rightarrow#tau#tau'
#legend['Hqq'] = 'H#rightarrowqq (bb, ss, cc)'
#legend['Hmumu'] = 'H#rightarrow#mu#mu'
#legend['HZa'] = 'H#rightarrowZa'
#legend['Mee'] = 'Mee'
#legend['VV'] = 'VV boson'

