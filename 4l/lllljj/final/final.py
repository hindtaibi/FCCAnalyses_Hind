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
               #'wzp6_ee_mumuH_HZZ_ecm365':{},
               #'wzp6_ee_eeH_HZZ_ecm365':{}
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
cutList = {"sel0":"Z1_cos < 2" #No cut 
           #"sel1":"N_selected_leptons ==4",
           #"sel2":"N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101",
           #"sel3":"N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 115 && Z1_recoil_m < 135"
           #"sel4":"N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8",
           #"sel5":"N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60",
           #"sel6":"N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93",
           #"sel7":"N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4",
           #"sel8": "N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2",
           #"sel9": "N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5",
           #"sel10": "N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000", 
           #"sel11": "N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000 &&  dmerge_2_23 < 60 ",
           #"sel12": "N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000 && dmerge_2_23 > 60 ",


           #"sel13": "N_selected_leptons ==2 && Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 138 && meanNconst > 8 && Z3_m < 100 && Z3_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000 && dmerge_2_23 > 60 && meanNconst_3 > 10 "

           
           #"sel9": "Z1_m > 81 && Z1_m < 101 && Z1_recoil_m > 124 && Z1_recoil_m < 140 && emiss > 5 && Z3_m < 40 && Z3_m > 65 && dmerge_2_12 > 10 && dmerge_2_23 < 100 && Z3_p < 40"

           
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    #--------------------------------------------------------------------------------------------------------------------------------------------------Z bosons

    "Z1_m":        {"name":"Z1_m",       "title":"First dilepton mass [GeV]",                              "bin":125,"xmin":0,"xmax":200},
    "Z1_p":        {"name":"Z1_p",       "title":"First dilepton momentum [GeV]",                          "bin":125,"xmin":0,"xmax":200},
    #"Z1_z_zoom":   {"name":"Z1_m",       "title":"First dilepton mass (zoom) [GeV]",                       "bin":40,"xmin":79,"xmax":103},
    "Z1_theta":    {"name":"Z1_theta",   "title":"#theta of the first lepton pair",                        "bin":100,"xmin":-7,"xmax":7},
    "Z1_phi":      {"name":"Z1_phi",     "title":"#phi of the first lepton pair",                          "bin":100,"xmin":-7,"xmax":7},
    "Z1_cos":      {"name":"Z1_cos",     "title":"cos(#theta) of the first lepton pair",                   "bin":100,"xmin":-1,"xmax":1},
    "Z1_eta":      {"name":"Z1_eta",     "title":"Pseudo-rapidity #eta of the first lepton pair",          "bin":100,"xmin":-10,"xmax":10},
    "Z1_y":        {"name":"Z1_y",       "title":"Rapidity y of the first lepton pair",                    "bin":100,"xmin":-5,"xmax":5},
    "Z1_recoil_m": {"name":"Z1_recoil_m","title":"Leptonic recoil mass of the first lepton pair [GeV]",    "bin":100,"xmin":0,"xmax":200},
    
    "Z2_m":        {"name":"Z2_m",       "title":"Second dilepton mass [GeV]",                             "bin":125,"xmin":0,"xmax":200},
    "Z2_p":        {"name":"Z2_p",       "title":"Second dilepton momentum [GeV]",                         "bin":125,"xmin":0,"xmax":200},
    "Z2_theta":    {"name":"Z2_theta",   "title":"#theta of the second lepton pair ",                      "bin":100,"xmin":-7,"xmax":7},
    "Z2_phi":      {"name":"Z2_phi",     "title":"#phi of the second lepton pair",                         "bin":100,"xmin":-7,"xmax":7},
    "Z2_cos":      {"name":"Z2_cos",     "title":"cos(#theta) of the second lepton pair",                  "bin":100,"xmin":-1,"xmax":1},
    "Z2_eta":      {"name":"Z2_eta",     "title":"Pseudo-rapidity #eta of the second lepton pair",         "bin":100,"xmin":-10,"xmax":10},
    "Z2_y":        {"name":"Z2_y",       "title":"Rapidity y of the second lepton pair",                   "bin":100,"xmin":-5,"xmax":5},
    "Z2_recoil_m": {"name":"Z2_recoil_m","title":"Leptonic recoil mass of the second lepton pair [GeV]",   "bin":100,"xmin":0,"xmax":200},

    "Z3_m":             {"name":"Z3_m",  "title":"Dijet mass (Durham kt N=2)",                "bin":100, "xmin":0,    "xmax":200},
    #"Z3_m_zoom1":       {"name":"Z3_m",  "title":"Dijet mass (Durham kt N=2)",                "bin":100, "xmin":80,   "xmax":120},
    #"Z3_m_zoom2":       {"name":"Z3_m",  "title":"Dijet mass (Durham kt N=2)",                "bin":100, "xmin":30,   "xmax":70},
    #"Z3_m_centered":    {"name":"Z3_m",  "title":"Dijet mass (Durham kt N=2)",                "bin":100, "xmin":60,   "xmax":100},
    #"Z3_m_centered_2":  {"name":"Z3_m",  "title":"Dijet mass (Durham kt N=2)",                "bin":20,  "xmin":60,   "xmax":100},
    "Z3_p":             {"name":"Z3_p",  "title":"Dijet momentum (Durham kt N=2)",            "bin":100, "xmin":0,    "xmax":200},
    "Z3_px":            {"name":"Z3_px", "title":"Dijet px (Durham kt N=2)",                  "bin":100, "xmin":-100, "xmax":100},
    "Z3_py":            {"name":"Z3_py", "title":"Dijet py (Durham kt N=2)",                  "bin":100, "xmin":-100, "xmax":100},
    "Z3_pz":            {"name":"Z3_pz", "title":"Dijet pz (Durham kt N=2)",                  "bin":100, "xmin":-100, "xmax":100},
    "Z3_pt":            {"name":"Z3_pt", "title":"Dijet transverse momentum (Durham kt N=2)", "bin":100, "xmin":0,    "xmax":200},

    "N_zed_leptonic":   {"name":"N_zed_leptonic",       "title":"Number of reconstructed leptonic Z",   "bin":10, "xmin":0, "xmax":10},

    


    #"leptonic_recoil_m_zoom":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":200,"xmin":80,"xmax":160},
    #"leptonic_recoil_m_zoom1":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":100,"xmin":120,"xmax":140},
    #"leptonic_recoil_m_zoom2":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":200,"xmin":120,"xmax":140},
    #"leptonic_recoil_m_zoom3":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":400,"xmin":120,"xmax":140},
    #"leptonic_recoil_m_zoom4":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":800,"xmin":120,"xmax":140},
    #"leptonic_recoil_m_zoom5":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":2000,"xmin":120,"xmax":140},
    #"leptonic_recoil_m_zoom6":{"name":"Z1_recoil_m","title":"Leptonic recoil mass [GeV]","bin":100,"xmin":122,"xmax":125},

    #--------------------------------------------------------------------------------------------------------------------------------------------------Leptons

    "selected_muons_e":     {"name":"selected_muons_e",    "title":"Energy of selected muons [GeV]",    "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_e": {"name":"selected_electrons_e","title":"Energy of selected electrons [GeV]","bin":100, "xmin":0, "xmax":200},
    "selected_leptons_e":   {"name":"selected_leptons_e",  "title":"Energy of selected leptons [GeV]",  "bin":100, "xmin":0, "xmax":200},

    "selected_muons_p":     {"name":"selected_muons_p",    "title":"Momentum of selected muons [GeV]",    "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_p": {"name":"selected_electrons_p","title":"Momentum of selected electrons [GeV]","bin":100, "xmin":0, "xmax":200},
    "selected_leptons_p":   {"name":"selected_leptons_p",  "title":"Momentum of selected leptons [GeV]",  "bin":100, "xmin":0, "xmax":200},

    "selected_muons_px":    {"name":"selected_muons_px",    "title":"px of selected (wrt momentum) muons [GeV]",                   "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_px":{"name":"selected_electrons_px","title":"px of selected (wrt momentum) electrons [GeV]",               "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_px":  {"name":"selected_leptons_px",  "title":"px of both selected (wrt momentum) muons and electrons [GeV]","bin":100, "xmin":-100, "xmax":100},

    "selected_muons_py":    {"name":"selected_muons_py",    "title":"py of selected (wrt momentum) muons [GeV]",                    "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_py":{"name":"selected_electrons_py","title":"py of selected (wrt momentum) electrons [GeV]",                "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_py":  {"name":"selected_leptons_py",  "title":"py of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_pz":    {"name":"selected_muons_pz",    "title":"pz of selected (wrt momentum) muons [GeV]",                    "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pz":{"name":"selected_electrons_pz","title":"pz of selected (wrt momentum) electrons [GeV]",                "bin":100, "xmin":-100, "xmax":100},
    "selected_leptons_pz":  {"name":"selected_leptons_pz",  "title":"pz of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_pt":    {"name":"selected_muons_pt",    "title":"pt of selected (wrt momentum) muons [GeV]",                    "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pt":{"name":"selected_electrons_pt","title":"pt of selected (wrt momentum) electrons [GeV]",                "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_pt":  {"name":"selected_leptons_pt",  "title":"pt of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":0, "xmax":200},

    "N_selected_leptons":   {"name":"N_selected_leptons",   "title":"Number of selected leptons",           "bin":10, "xmin":0, "xmax":10}, 

    "N_LooseLeptons_10":    {"name":"N_LooseLeptons_10",    "title":"Number of leptons with p>10 GeV",                   "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_2":     {"name":"N_LooseLeptons_2",     "title":"Number of leptons with p>2 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_1":     {"name":"N_LooseLeptons_1",     "title":"Number of leptons with p>1 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "LooseLeptons_10_pt":   {"name":"LooseLeptons_10_pt",   "title":"Transverse momentum of leptons with p>10GeV [GeV]", "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_p":    {"name":"LooseLeptons_10_p",    "title":"Momentum of leptons with p>10GeV [GeV]",            "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_theta":{"name":"LooseLeptons_10_theta","title":"#theta of leptons with p>10GeV [GeV]",              "bin":100, "xmin":0, "xmax":4},
    "LooseLeptons_10_phi":  {"name":"LooseLeptons_10_phi",  "title":"#phi of leptons with p>10 GeV [GeV]",               "bin":100, "xmin":-7,"xmax":7},

    #--------------------------------------------------------------------------------------------------------------------------------------------------Jets
    
    #N = 2

    "j5_p":         {"name":"j5_p",        "title":"Momentum of the 1st jet from Durham kt N=2 [GeV]",          "bin":100,"xmin":0,    "xmax":200},
    "j6_p":         {"name":"j6_p",        "title":"Momentum of the 2nd jet from Durham kt N=2 [GeV]",          "bin":100,"xmin":0,    "xmax":200},    

    "j5_px":        {"name":"j5_px",       "title":"px of the 1st jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":-100, "xmax":100},
    "j6_px":        {"name":"j6_px",       "title":"px of the 2nd jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":-100, "xmax":100},
    
    "j5_py":        {"name":"j5_py",       "title":"py of the 1st jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":-100, "xmax":100},
    "j6_py":        {"name":"j6_py",       "title":"py of the 2nd jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":-100, "xmax":100},

    "j5_pz":        {"name":"j5_pz",       "title":"pz of the 1st jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":-100, "xmax":100},
    "j6_pz":        {"name":"j6_pz",       "title":"pz of the 2nd jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":-100, "xmax":100},

    "j5_pt":        {"name":"j5_pt",       "title":"pt of the 1st jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":0,    "xmax":200},
    "j6_pt":        {"name":"j6_pt",       "title":"pt of the 2nd jet from Durham kt N=2 [GeV]",                "bin":100,"xmin":0,    "xmax":200},
         
    "j5_e":         {"name":"j5_e",        "title":"Energy of the 1st jet from Durham kt N=2 [GeV]",            "bin":100,"xmin":0,    "xmax":200},
    "j6_e":         {"name":"j6_e",        "title":"Energy of the 2nd jet from Durham kt N=2 [GeV]",            "bin":100,"xmin":0,    "xmax":200},

    "j5_theta":     {"name":"j5_theta",    "title":"#theta of the 1st jet from Durham kt N=2 [GeV]",            "bin":100,"xmin":0,    "xmax":4},
    "j6_theta":     {"name":"j6_theta",    "title":"#theta of the 2nd jet from Durham kt N=2 [GeV]",            "bin":100,"xmin":0,    "xmax":4},

    "j5_phi":       {"name":"j5_phi",      "title":"#theta of the 1st jet from Durham kt N=2 [GeV]",            "bin":100,"xmin":0,    "xmax":4},
    "j6_phi":       {"name":"j6_phi",      "title":"#theta of the 2nd jet from Durham kt N=2 [GeV]",            "bin":100,"xmin":0,    "xmax":4},

    "j5_const":     {"name":"j5_const",    "title":"Number of constituents of the 1st jet from Durham kt N=2",  "bin":70, "xmin":0,    "xmax":70},
    "j6_const":     {"name":"j6_const",    "title":"Number of constituents of the 2nd jet from Durham kt N=2",  "bin":70, "xmin":0,    "xmax":70},

    "min_const_2":    {"name":"min_const_2",   "title":"Minimum number of constituents from Durham kt N=2",         "bin":70, "xmin":0,    "xmax":70},
    "max_const_2":    {"name":"max_const_2",   "title":"Maximum number of constituents from Durham kt N=2",         "bin":70, "xmin":0,    "xmax":70},
    "mean_const_2":   {"name":"mean_const_2",  "title":"Mean number of constituents from Durham kt N=2",            "bin":70, "xmin":0,    "xmax":70},

    "diffthetajets_56":      {"name":"diffthetajets_56",   "title":"Angular diff (theta) between the jets 5 and 6",         "bin":100, "xmin":0, "xmax":4},
    "diffphijets_56":        {"name":"diffphijets_56",     "title":"Angular diff (phi) between the jets 5 and 6",           "bin":100, "xmin":0, "xmax":4},
    
    "missing_theta":        {"name":"missing_theta",     "title":"#theta extracted from the missing tlv",                   "bin":100, "xmin":0, "xmax":4},
    "angle_miss_j5":        {"name":"angle_miss_j5",     "title":"angular difference between missing tlv and j5",           "bin":100, "xmin":0, "xmax":4},
    "angle_miss_j6":        {"name":"angle_miss_j6",     "title":"angular difference between missing tlv and j6",           "bin":100, "xmin":0, "xmax":4},
    "min_angle_miss_jet":   {"name":"min_angle_miss_jet","title":"Minimal angular difference between missing tlv and jets", "bin":100, "xmin":0, "xmax":4},
    "max_angle_miss_jet":   {"name":"max_angle_miss_jet","title":"Maximal angular difference between missing tlv and jets", "bin":100, "xmin":0, "xmax":4},

    "dmerge_2_12":{"name":"dmerge_2_12","title":"dmerge_12","bin":125,"xmin":0,"xmax":12000},
    "dmerge_2_23":{"name":"dmerge_2_23","title":"dmerge_23","bin":125,"xmin":0,"xmax":1000},
    "dmerge_2_34":{"name":"dmerge_2_34","title":"dmerge_34","bin":125,"xmin":0,"xmax":700},
    "dmerge_2_45":{"name":"dmerge_2_45","title":"dmerge_45","bin":125,"xmin":0,"xmax":700},

    #N = 3

    "ja_p":         {"name":"ja_p",        "title":"Momentum of the 1st jet from Durham kt N=3 [GeV]",          "bin":100,"xmin":0,    "xmax":200},
    "jb_p":         {"name":"jb_p",        "title":"Momentum of the 2nd jet from Durham kt N=3 [GeV]",          "bin":100,"xmin":0,    "xmax":200},
    "jc_p":         {"name":"jc_p",        "title":"Momentum of the 3rd jet from Durham kt N=3 [GeV]",          "bin":100,"xmin":0,    "xmax":200},

    "ja_e":         {"name":"ja_e",        "title":"Energy of the 1st jet from Durham kt N=3 [GeV]",            "bin":100,"xmin":0,    "xmax":200},
    "jb_e":         {"name":"jb_e",        "title":"Energy of the 2nd jet from Durham kt N=3 [GeV]",            "bin":100,"xmin":0,    "xmax":200},
    "jc_e":         {"name":"jc_e",        "title":"Energy of the 3rd jet from Durham kt N=3 [GeV]",            "bin":100,"xmin":0,    "xmax":200},

    "min_const_3":  {"name":"min_const_3", "title":"Minimum number of constituents from Durham kt N=3",         "bin":40, "xmin":0,    "xmax":40},
    "max_const_3":  {"name":"max_const_3", "title":"Maximum number of constituents from Durham kt N=3",         "bin":40, "xmin":0,    "xmax":40},
    "mean_const_3": {"name":"mean_const_3","title":"Mean number of constituents from Durham kt N=3",            "bin":40, "xmin":0,    "xmax":40},

    "diffthetajets_ab":{"name":"diffthetajets_ab", "title":"Angular diff (theta) between the jets a and b", "bin" :100, "xmin":0, "xmax":4},
    "diffthetajets_bc":{"name":"diffthetajets_bc", "title":"Angular diff (theta) between the jets b and c", "bin" :100, "xmin":0, "xmax":4},
    "diffthetajets_ac":{"name":"diffthetajets_ac", "title":"Angular diff (theta) between the jets a and c", "bin" :100, "xmin":0, "xmax":4},

    "diffphijets_ab":  {"name":"diffphijets_ab",   "title":"Angular diff (phi) between the jets a and b",   "bin" :100, "xmin":0, "xmax":4},
    "diffphijets_bc":  {"name":"diffphijets_bc",   "title":"Angular diff (phi) between the jets b and c",   "bin" :100, "xmin":0, "xmax":4},
    "diffphijets_ac":  {"name":"diffphijets_ac",   "title":"Angular diff (phi) between the jets a and c",   "bin" :100, "xmin":0, "xmax":4},

    "dmerge_3_12":{"name":"dmerge_3_12","title":"dmerge_12 (N=3)","bin":125,"xmin":0,"xmax":12000},
    "dmerge_3_23":{"name":"dmerge_3_23","title":"dmerge_23 (N=3)","bin":125,"xmin":0,"xmax":1000},
    "dmerge_3_34":{"name":"dmerge_3_34","title":"dmerge_34 (N=3)","bin":125,"xmin":0,"xmax":700},
    "dmerge_3_45":{"name":"dmerge_3_45","title":"dmerge_45 (N=3)","bin":125,"xmin":0,"xmax":700},
    
    #--------------------------------------------------------------------------------------------------------------------------------------------------Missing/Visible stuff

    "visible_mass_predef":      {"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":0, "xmax":300},
    #"visible_mass_predef_zoom": {"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":200, "xmax":240},

    "emiss":        {"name":"emiss",  "title":"Missing energy [GeV]",            "bin":100, "xmin":0,   "xmax":100},
    "pxmiss":       {"name":"pxmiss", "title":"Missing px [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pymiss":       {"name":"pymiss", "title":"Missing py [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pzmiss":       {"name":"pzmiss", "title":"Missing pz [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    #"pzmiss_zoom":  {"name":"pzmiss", "title":"Missing pz [GeV]",                "bin":100, "xmin":0,   "xmax":60},
    "etmiss":       {"name":"etmiss", "title":"Missing transverse energy [GeV]", "bin":100, "xmin":0,   "xmax":100}
    #"etmiss_zoom":  {"name":"etmiss", "title":"Missing transverse energy [GeV]", "bin":100, "xmin":0,   "xmax":60},


}



    

