#Input directory where the files produced at the pre-selection level are
inputDir  = "../stage2/outputs/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs"

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},        #Signal
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               #'wzp6_ee_mumuH_Haa_ecm240':{},        #Empty after stage2
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               #'wzp6_ee_mumuH_Hgg_ecm240':{},        #Empty after stage2
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_nunuH_HZZ_ecm240':{},
               #'wzp6_ee_nunuH_HWW_ecm240':{},        #Empty after stage2
               #'wzp6_ee_nunuH_HZa_ecm240':{},        #Empty after stage2
               #'wzp6_ee_nunuH_Haa_ecm240':{},        #Empty after stage2
               #'wzp6_ee_nunuH_Hbb_ecm240':{},        #Empty after stage2       
               #'wzp6_ee_nunuH_Hcc_ecm240':{},        #Empty after stage2
               #'wzp6_ee_nunuH_Hgg_ecm240':{},        #Empty after stage2
               #'wzp6_ee_nunuH_Hmumu_ecm240':{},      #Empty after stage2
               #'wzp6_ee_nunuH_Hss_ecm240':{},        #Empty after stage2
               #'wzp6_ee_nunuH_Htautau_ecm240':{},    #Empty after stage2
               'wzp6_ee_eeH_HZZ_ecm240':{},          #Signal
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               #'wzp6_ee_eeH_Haa_ecm240':{},          #Empty after stage2
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               #'wzp6_ee_eeH_Hgg_ecm240':{},          #Empty after stage2
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{}
            }

#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
#procDictAdd={"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

#Number of CPUs to use
nCPUS = 128

#produces ROOT TTrees, default is False
doTree = False
doScale = False


#Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {"sel0":"Z1_theta < 10",   #No cut
           "sel1":"emiss < 8",
           "sel2":"Z1_m > 81 && Z1_m < 101",
           "sel3":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101",
           "sel4":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50"
           #"sel6":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50",
           #"sel7":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50 && emiss < 10"
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------Photons

    "N_photons":      {"name":"N_photons",      "title":"Number of photons",                                     "bin":10, "xmin":0,    "xmax":10},
    "photons_e":      {"name":"photons_e",      "title":"Energy of the photons [GeV]",                           "bin":125,"xmin":0,    "xmax":50},
    "photons_px":     {"name":"photons_px",     "title":"p_{x} of the photons [GeV]",                            "bin":125,"xmin":0,    "xmax":40},
    "photons_py":     {"name":"photons_py",     "title":"p_{y} of the photons [GeV]",                            "bin":125,"xmin":0,    "xmax":40},
    "photons_pz":     {"name":"photons_pz",     "title":"p_{z} of the photons [GeV]",                            "bin":125,"xmin":0,    "xmax":40},
    "photons_pt":     {"name":"photons_px",     "title":"p_{t} of the photons [GeV]",                            "bin":125,"xmin":0,    "xmax":40},
    "photons_phi":    {"name":"photons_phi",    "title":"#varphi of the photons [GeV]",                          "bin":100,"xmin":-3.5, "xmax":3.5},
    "photons_theta":  {"name":"photons_theta",  "title":"#theta of the photons [GeV]",                           "bin":100,"xmin":0,    "xmax":3.2},   

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------Z bosons

    "Z1_m":        {"name":"Z1_m",       "title":"1st dilepton mass [GeV]",                              "bin":125,"xmin":0,   "xmax":140},
    "Z1_p":        {"name":"Z1_p",       "title":"1st dilepton momentum [GeV]",                          "bin":125,"xmin":0,   "xmax":100},
    "Z1_e":        {"name":"Z1_e",       "title":"1st dilepton energy [GeV]",                            "bin":125,"xmin":0,   "xmax":5},
    "Z1_theta":    {"name":"Z1_theta",   "title":"#theta of the 1st lepton pair",                        "bin":100,"xmin":0,   "xmax":3.5},
    "Z1_phi":      {"name":"Z1_phi",     "title":"#phi of the 1st lepton pair",                          "bin":100,"xmin":-3.5,"xmax":3.5},
    "Z1_recoil_m": {"name":"Z1_recoil_m","title":"Leptonic recoil mass of the 1st lepton pair [GeV]",    "bin":100,"xmin":0,   "xmax":200},
    
    "Z2_m":        {"name":"Z2_m",       "title":"2nd dilepton mass [GeV]",                             "bin":125,"xmin":0,    "xmax":160},
    "Z2_p":        {"name":"Z2_p",       "title":"2nd dilepton momentum [GeV]",                         "bin":125,"xmin":0,    "xmax":120},
    "Z2_e":        {"name":"Z2_e",       "title":"2nd dilepton energy [GeV]",                           "bin":125,"xmin":0,    "xmax":200},
    "Z2_theta":    {"name":"Z2_theta",   "title":"#theta of the 2nd lepton pair ",                      "bin":100,"xmin":0,    "xmax":3.5},
    "Z2_phi":      {"name":"Z2_phi",     "title":"#phi of the 2nd lepton pair",                         "bin":100,"xmin":-3.5, "xmax":3.5},
    "Z2_recoil_m": {"name":"Z2_recoil_m","title":"Leptonic recoil mass of the 2nd lepton pair [GeV]",   "bin":100,"xmin":0,    "xmax":130},

    "Z3_m":             {"name":"Z3_m",       "title":"Dijet mass (Durham kt N=2)",               "bin":100, "xmin":0,    "xmax":100},
    "Z3_p":             {"name":"Z3_p",       "title":"Dijet p (Durham kt N=2)",                  "bin":100, "xmin":0,    "xmax":80},
    "Z3_px":            {"name":"Z3_px",      "title":"Dijet p_{x} (Durham kt N=2)",              "bin":100, "xmin":-40,  "xmax":40},
    "Z3_py":            {"name":"Z3_py",      "title":"Dijet p_{y} (Durham kt N=2)",              "bin":100, "xmin":-40,  "xmax":40},
    "Z3_pz":            {"name":"Z3_pz",      "title":"Dijet p_{z} (Durham kt N=2)",              "bin":100, "xmin":-40,  "xmax":40},
    "Z3_pt":            {"name":"Z3_pt",      "title":"Dijet p_{t} (Durham kt N=2)",              "bin":100, "xmin":0,    "xmax":60},
    "Z3_theta":     	{"name":"Z3_theta",   "title":"#theta of the dijet ",                     "bin":100, "xmin":0,    "xmax":3.5},
    "Z3_phi":           {"name":"Z3_phi",     "title":"#phi of the dijet",                        "bin":100, "xmin":-3.5, "xmax":3.5},

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------Leptons
    
    "on_difftheta1_muons":      {"name":"on_difftheta1_muons",      "title":"on_difftheta1_muons",          "bin":100, "xmin":0,  "xmax":3.5},
    "on_difftheta2_muons":      {"name":"on_difftheta2_muons",      "title":"on_difftheta2_muons",          "bin":100, "xmin":0,  "xmax":3.5},
    "on_difftheta1_electrons":  {"name":"on_difftheta1_electrons",  "title":"on_difftheta1_electrons",      "bin":100, "xmin":0,  "xmax":3.5},
    "on_difftheta2_electrons":  {"name":"on_difftheta2_electrons",  "title":"on_difftheta2_electrons",      "bin":100, "xmin":0,  "xmax":3.5},

    "on_diffphi1_muons":        {"name":"on_diffphi1_muons",        "title":"on_diffphi1_muons",            "bin":100, "xmin":0,  "xmax":7},
    "on_diffphi2_muons":        {"name":"on_diffphi2_muons",        "title":"on_diffphi2_muons",            "bin":100, "xmin":0,  "xmax":7},
    "on_diffphi1_electrons":    {"name":"on_diffphi1_electrons",    "title":"on_diffphi1_electrons",        "bin":100, "xmin":0,  "xmax":7},
    "on_diffphi2_electrons":    {"name":"on_diffphi2_electrons",    "title":"on_diffphi2_electrons",        "bin":100, "xmin":0,  "xmax":7},
    
    "N_LooseLeptons_10":    {"name":"N_LooseLeptons_10",    "title":"Number of leptons with p>10 GeV",                   "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_2":     {"name":"N_LooseLeptons_2",     "title":"Number of leptons with p>2 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_1":     {"name":"N_LooseLeptons_1",     "title":"Number of leptons with p>1 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "LooseLeptons_10_e":    {"name":"LooseLeptons_10_e",    "title":"Energy of leptons with p>10GeV [GeV]",              "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_p":    {"name":"LooseLeptons_10_p",    "title":"p of leptons with p>10GeV [GeV]",                   "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_theta":{"name":"LooseLeptons_10_theta","title":"#theta of leptons with p>10GeV [GeV]",              "bin":100, "xmin":0, "xmax":4},
    "LooseLeptons_10_phi":  {"name":"LooseLeptons_10_phi",  "title":"#phi of leptons with p>10 GeV [GeV]",               "bin":100, "xmin":-7,"xmax":7},

    "N_all_taken_leptons":        {"name":"N_all_taken_leptons", 	    "title":"Number of selected leptons",         	 "bin":10,  "xmin":0,    "xmax":8},
    "all_taken_leptons_e":        {"name":"all_taken_leptons_e",        "title":"Energy of selected leptons [GeV]",      "bin":100, "xmin":0,    "xmax":100},
    "all_taken_leptons_p":        {"name":"all_taken_leptons_p",        "title":"Momentum of selected leptons [GeV]",    "bin":100, "xmin":0,    "xmax":100},
    "all_taken_leptons_phi":      {"name":"all_taken_leptons_phi",      "title":"#phi of selected leptons",              "bin":100, "xmin":-3.5, "xmax":3.5},
    "all_taken_leptons_theta":    {"name":"all_taken_leptons_theta",    "title":"#theta of selected leptons",            "bin":100, "xmin":0,    "xmax":3.5},
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------Jets
    
    #N = 2

    "j5_p":         {"name":"j5_p",        "title":"p of the 1st jet (Durham kt N=2) [GeV]",                 "bin":100,"xmin":0,    "xmax":80},
    "j6_p":         {"name":"j6_p",        "title":"p of the 2nd jet (Durham kt N=2) [GeV]",                 "bin":100,"xmin":0,    "xmax":60},    

    "j5_px":        {"name":"j5_px",       "title":"p_{x} of the 1st jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":-40, "xmax":40},
    "j6_px":        {"name":"j6_px",       "title":"p_{x} of the 2nd jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":-40, "xmax":40},
    
    "j5_py":        {"name":"j5_py",       "title":"p_{y} of the 1st jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":-40, "xmax":40},
    "j6_py":        {"name":"j6_py",       "title":"p_{y} of the 2nd jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":-40, "xmax":40},

    "j5_pz":        {"name":"j5_pz",       "title":"p_{z} of the 1st jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":-40, "xmax":40},
    "j6_pz":        {"name":"j6_pz",       "title":"p_{z} of the 2nd jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":-40, "xmax":40},

    "j5_pt":        {"name":"j5_pt",       "title":"p_{t} of the 1st jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":0,    "xmax":80},
    "j6_pt":        {"name":"j6_pt",       "title":"p_{t} of the 2nd jet (Durham kt N=2) [GeV]",             "bin":100,"xmin":0,    "xmax":50},
         
    "j5_e":         {"name":"j5_e",        "title":"Energy of the 1st jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":80},
    "j6_e":         {"name":"j6_e",        "title":"Energy of the 2nd jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":60},

    "j5_theta":     {"name":"j5_theta",    "title":"#theta of the 1st jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},
    "j6_theta":     {"name":"j6_theta",    "title":"#theta of the 2nd jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},

    "j5_phi":       {"name":"j5_phi",      "title":"#theta of the 1st jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},
    "j6_phi":       {"name":"j6_phi",      "title":"#theta of the 2nd jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},

    "diffthetajets_56":      {"name":"diffthetajets_56",   "title":"Angular diff (#theta) between the jets 5 and 6",         "bin":100, "xmin":0, "xmax":3.2},
    "diffphijets_56":        {"name":"diffphijets_56",     "title":"Angular diff (#phi) between the jets 5 and 6",           "bin":100, "xmin":0, "xmax":6.4},
    
    #--------------------------------------------------------------------------------------------------------------------------------------------------Missing/Visible stuff

    "visible_mass_predef":      {"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":100, "xmax":300},
    
    "emiss":        {"name":"emiss",  "title":"Missing energy [GeV]",               "bin":100, "xmin":0,   "xmax":100},
    "pxmiss":       {"name":"pxmiss", "title":"Missing p_{x} [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pymiss":       {"name":"pymiss", "title":"Missing p_{y} [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pzmiss":       {"name":"pzmiss", "title":"Missing p_{z} [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "etmiss":       {"name":"etmiss", "title":"Missing transverse energy [GeV]",    "bin":100, "xmin":0,   "xmax":100}

}



    

