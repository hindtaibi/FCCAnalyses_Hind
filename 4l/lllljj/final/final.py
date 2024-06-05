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
cutList = {"sel0":"Z1_cos < 2",   #No cut
           "sel1":"emiss < 20",
           "sel2":"emiss < 10",
           "sel3":"Z1_m > 81 && Z1_m < 101",
           "sel4":"Z2_m > 81 && Z2_m < 101",
           "sel5":"Z3_m > 10 && Z3_m < 50",
           "sel6":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50",
           "sel7":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50 && emiss < 10"
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    
    Z bosons

    "Z1_m":        {"name":"Z1_m",       "title":"1st dilepton mass [GeV]",                              "bin":125,"xmin":0,"xmax":200},
    "Z1_p":        {"name":"Z1_p",       "title":"1st dilepton momentum [GeV]",                          "bin":125,"xmin":0,"xmax":200},
    "Z1_theta":    {"name":"Z1_theta",   "title":"#theta of the 1st lepton pair",                        "bin":100,"xmin":-7,"xmax":7},
    "Z1_phi":      {"name":"Z1_phi",     "title":"#phi of the 1st lepton pair",                          "bin":100,"xmin":-7,"xmax":7},
    "Z1_cos":      {"name":"Z1_cos",     "title":"cos(#theta) of the 1st lepton pair",                   "bin":100,"xmin":-1,"xmax":1},
    "Z1_eta":      {"name":"Z1_eta",     "title":"Pseudo-rapidity #eta of the 1st lepton pair",          "bin":100,"xmin":-10,"xmax":10},
    "Z1_y":        {"name":"Z1_y",       "title":"Rapidity y of the 1st lepton pair",                    "bin":100,"xmin":-3,"xmax":3},
    "Z1_recoil_m": {"name":"Z1_recoil_m","title":"Leptonic recoil mass of the 1st lepton pair [GeV]",    "bin":100,"xmin":0,"xmax":200},
    
    "Z2_m":        {"name":"Z2_m",       "title":"2nd dilepton mass [GeV]",                             "bin":125,"xmin":0, "xmax":160},
    "Z2_p":        {"name":"Z2_p",       "title":"2nd dilepton momentum [GeV]",                         "bin":125,"xmin":0, "xmax":120},
    "Z2_theta":    {"name":"Z2_theta",   "title":"#theta of the 2nd lepton pair ",                      "bin":100,"xmin":0, "xmax":4},
    "Z2_phi":      {"name":"Z2_phi",     "title":"#phi of the 2nd lepton pair",                         "bin":100,"xmin":-4,"xmax":4},
    "Z2_cos":      {"name":"Z2_cos",     "title":"cos(#theta) of the 2nd lepton pair",                  "bin":100,"xmin":-1,"xmax":1},
    "Z2_eta":      {"name":"Z2_eta",     "title":"Pseudo-rapidity #eta of the 2nd lepton pair",         "bin":100,"xmin":-6,"xmax":6},
    "Z2_y":        {"name":"Z2_y",       "title":"Rapidity y of the 2nd lepton pair",                   "bin":100,"xmin":-3,"xmax":3},
    "Z2_recoil_m": {"name":"Z2_recoil_m","title":"Leptonic recoil mass of the 2nd lepton pair [GeV]",   "bin":100,"xmin":0,"xmax":10},

    "Z3_m":             {"name":"Z3_m",  "title":"Dijet mass (Durham kt N=2)",               "bin":100, "xmin":0,    "xmax":100},
    "Z3_p":             {"name":"Z3_p",  "title":"Dijet p (Durham kt N=2)",                  "bin":100, "xmin":0,    "xmax":80},
    "Z3_px":            {"name":"Z3_px", "title":"Dijet p_x (Durham kt N=2)",                "bin":100, "xmin":-40,  "xmax":40},
    "Z3_py":            {"name":"Z3_py", "title":"Dijet p_y (Durham kt N=2)",                "bin":100, "xmin":-40,  "xmax":40},
    "Z3_pz":            {"name":"Z3_pz", "title":"Dijet p_z (Durham kt N=2)",                "bin":100, "xmin":-40,  "xmax":40},
    "Z3_pt":            {"name":"Z3_pt", "title":"Dijet p_t (Durham kt N=2)",                "bin":100, "xmin":0,    "xmax":60},

    "N_zed_leptonic":   {"name":"N_zed_leptonic",       "title":"Number of reconstructed leptonic Z",   "bin":10, "xmin":0, "xmax":10},

    #--------------------------------------------------------------------------------------------------------------------------------------------------Leptons

    "selected_muons_e":     {"name":"selected_muons_e",    "title":"Energy of selected muons [GeV]",    "bin":100, "xmin":0, "xmax":100},
    "selected_electrons_e": {"name":"selected_electrons_e","title":"Energy of selected electrons [GeV]","bin":100, "xmin":0, "xmax":100},
    "selected_leptons_e":   {"name":"selected_leptons_e",  "title":"Energy of selected leptons [GeV]",  "bin":100, "xmin":0, "xmax":100},

    "selected_muons_p":     {"name":"selected_muons_p",    "title":"p of selected muons [GeV]",    "bin":100, "xmin":0, "xmax":100},
    "selected_electrons_p": {"name":"selected_electrons_p","title":"p of selected electrons [GeV]","bin":100, "xmin":0, "xmax":100},
    "selected_leptons_p":   {"name":"selected_leptons_p",  "title":"p of selected leptons [GeV]",  "bin":100, "xmin":0, "xmax":100},

    "selected_muons_px":    {"name":"selected_muons_px",    "title":"#p_x of selected muons [GeV]",                   "bin":100, "xmin":0, "xmax":80},
    "selected_electrons_px":{"name":"selected_electrons_px","title":"#p_x of selected electrons [GeV]",               "bin":100, "xmin":0, "xmax":80},
    "selected_leptons_px":  {"name":"selected_leptons_px",  "title":"#p_x of selected leptons [GeV]",                 "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_py":    {"name":"selected_muons_py",    "title":"#p_y of selected muons [GeV]",                    "bin":100, "xmin":0, "xmax":80},
    "selected_electrons_py":{"name":"selected_electrons_py","title":"#p_y of selected electrons [GeV]",                "bin":100, "xmin":0, "xmax":80},
    "selected_leptons_py":  {"name":"selected_leptons_py",  "title":"#p_y of selected leptons [GeV]",                  "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_pz":    {"name":"selected_muons_pz",    "title":"#p_z of selected muons [GeV]",                    "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pz":{"name":"selected_electrons_pz","title":"#p_z of selected electrons [GeV]",                "bin":100, "xmin":-100, "xmax":100},
    "selected_leptons_pz":  {"name":"selected_leptons_pz",  "title":"#p_z of selected leptons [GeV]",                  "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_pt":    {"name":"selected_muons_pt",    "title":"#p_t of selected muons [GeV]",                    "bin":100, "xmin":0, "xmax":100},
    "selected_electrons_pt":{"name":"selected_electrons_pt","title":"#p_t of selected electrons [GeV]",                "bin":100, "xmin":0, "xmax":100},
    "selected_leptons_pt":  {"name":"selected_leptons_pt",  "title":"#p_t of selected leptons [GeV]",                  "bin":100, "xmin":0, "xmax":100},

    "N_selected_leptons":   {"name":"N_selected_leptons",   "title":"Number of selected leptons",            "bin":10, "xmin":0, "xmax":10}, 

    "N_LooseLeptons_10":    {"name":"N_LooseLeptons_10",    "title":"Number of leptons with p>10 GeV",                   "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_2":     {"name":"N_LooseLeptons_2",     "title":"Number of leptons with p>2 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_1":     {"name":"N_LooseLeptons_1",     "title":"Number of leptons with p>1 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "LooseLeptons_10_pt":   {"name":"LooseLeptons_10_pt",   "title":"#p_t of leptons with p>10GeV [GeV]",                "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_p":    {"name":"LooseLeptons_10_p",    "title":"p of leptons with p>10GeV [GeV]",                   "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_theta":{"name":"LooseLeptons_10_theta","title":"#theta of leptons with p>10GeV [GeV]",              "bin":100, "xmin":0, "xmax":4},
    "LooseLeptons_10_phi":  {"name":"LooseLeptons_10_phi",  "title":"#phi of leptons with p>10 GeV [GeV]",               "bin":100, "xmin":-7,"xmax":7},

    #--------------------------------------------------------------------------------------------------------------------------------------------------Jets
    
    #N = 2

    "j5_p":         {"name":"j5_p",        "title":"p of the 1st jet (Durham kt N=2) [GeV]",                 "bin":100,"xmin":0,    "xmax":80},
    "j6_p":         {"name":"j6_p",        "title":"p of the 2nd jet (Durham kt N=2) [GeV]",                 "bin":100,"xmin":0,    "xmax":60},    

    "j5_px":        {"name":"j5_px",       "title":"p_x of the 1st jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":-40, "xmax":40},
    "j6_px":        {"name":"j6_px",       "title":"p_x of the 2nd jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":-40, "xmax":40},
    
    "j5_py":        {"name":"j5_py",       "title":"p_y of the 1st jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":-40, "xmax":40},
    "j6_py":        {"name":"j6_py",       "title":"p_y of the 2nd jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":-40, "xmax":40},

    "j5_pz":        {"name":"j5_pz",       "title":"p_z of the 1st jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":-40, "xmax":40},
    "j6_pz":        {"name":"j6_pz",       "title":"p_z of the 2nd jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":-40, "xmax":40},

    "j5_pt":        {"name":"j5_pt",       "title":"p_t of the 1st jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":0,    "xmax":80},
    "j6_pt":        {"name":"j6_pt",       "title":"p_t of the 2nd jet (Durham kt N=2) [GeV]",              "bin":100,"xmin":0,    "xmax":50},
         
    "j5_e":         {"name":"j5_e",        "title":"Energy of the 1st jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":80},
    "j6_e":         {"name":"j6_e",        "title":"Energy of the 2nd jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":60},

    "j5_theta":     {"name":"j5_theta",    "title":"#theta of the 1st jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},
    "j6_theta":     {"name":"j6_theta",    "title":"#theta of the 2nd jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},

    "j5_phi":       {"name":"j5_phi",      "title":"#theta of the 1st jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},
    "j6_phi":       {"name":"j6_phi",      "title":"#theta of the 2nd jet (Durham kt N=2) [GeV]",            "bin":100,"xmin":0,    "xmax":4},

    "j5_const":     {"name":"j5_const",    "title":"Number of constituents of the 1st jet (Durham kt N=2)",  "bin":70, "xmin":0,    "xmax":70},
    "j6_const":     {"name":"j6_const",    "title":"Number of constituents of the 2nd jet (Durham kt N=2)",  "bin":70, "xmin":0,    "xmax":30},

    "min_const_2":    {"name":"min_const_2",   "title":"Minimum number of constituents (Durham kt N=2)",         "bin":70, "xmin":0,    "xmax":70},
    "max_const_2":    {"name":"max_const_2",   "title":"Maximum number of constituents (Durham kt N=2)",         "bin":70, "xmin":0,    "xmax":70},
    "mean_const_2":   {"name":"mean_const_2",  "title":"Mean number of constituents (Durham kt N=2)",            "bin":70, "xmin":0,    "xmax":70},

    "diffthetajets_56":      {"name":"diffthetajets_56",   "title":"Angular diff (#theta) between the jets 5 and 6",         "bin":100, "xmin":0, "xmax":4},
    "diffphijets_56":        {"name":"diffphijets_56",     "title":"Angular diff (#phi) between the jets 5 and 6",           "bin":100, "xmin":0, "xmax":7},
    
    "missing_theta":        {"name":"missing_theta",     "title":"Missing #theta extracted from the missing tlv",           "bin":100, "xmin":0, "xmax":4},
    "angle_miss_j5":        {"name":"angle_miss_j5",     "title":"Angular difference between missing tlv and j5",           "bin":100, "xmin":0, "xmax":4},
    "angle_miss_j6":        {"name":"angle_miss_j6",     "title":"Angular difference between missing tlv and j6",           "bin":100, "xmin":0, "xmax":4},
    "min_angle_miss_jet":   {"name":"min_angle_miss_jet","title":"Minimal angular difference between missing tlv and jets", "bin":100, "xmin":0, "xmax":4},
    "max_angle_miss_jet":   {"name":"max_angle_miss_jet","title":"Maximal angular difference between missing tlv and jets", "bin":100, "xmin":0, "xmax":4},

    "dmerge_2_12":{"name":"dmerge_2_12","title":"dmerge_{12} (Durham kt N=2)","bin":125,"xmin":0,"xmax":500},
    "dmerge_2_23":{"name":"dmerge_2_23","title":"dmerge_{23} (Durham kt N=2)","bin":125,"xmin":0,"xmax":100},
    "dmerge_2_34":{"name":"dmerge_2_34","title":"dmerge_{34} (Durham kt N=2)","bin":125,"xmin":0,"xmax":70},
    "dmerge_2_45":{"name":"dmerge_2_45","title":"dmerge_{45} (Durham kt N=2)","bin":125,"xmin":0,"xmax":50},

    #N = 3

    "ja_p":         {"name":"ja_p",        "title":"p of the 1st jet (Durham kt N=3) [GeV]",          "bin":100,"xmin":0,    "xmax":60},
    "jb_p":         {"name":"jb_p",        "title":"p of the 2nd jet (Durham kt N=3) [GeV]",          "bin":100,"xmin":0,    "xmax":40},
    "jc_p":         {"name":"jc_p",        "title":"p of the 3rd jet (Durham kt N=3) [GeV]",          "bin":100,"xmin":0,    "xmax":30},

    "ja_e":         {"name":"ja_e",        "title":"Energy of the 1st jet (Durham kt N=3) [GeV]",            "bin":100,"xmin":0,    "xmax":60},
    "jb_e":         {"name":"jb_e",        "title":"Energy of the 2nd jet (Durham kt N=3) [GeV]",            "bin":100,"xmin":0,    "xmax":40},
    "jc_e":         {"name":"jc_e",        "title":"Energy of the 3rd jet (Durham kt N=3) [GeV]",            "bin":100,"xmin":0,    "xmax":30},

    "min_const_3":  {"name":"min_const_3", "title":"Minimum number of constituents (Durham kt N=3)",         "bin":40, "xmin":0,    "xmax":20},
    "max_const_3":  {"name":"max_const_3", "title":"Maximum number of constituents (Durham kt N=3)",         "bin":40, "xmin":0,    "xmax":40},
    "mean_const_3": {"name":"mean_const_3","title":"Mean number of constituents (Durham kt N=3)",            "bin":40, "xmin":0,    "xmax":25},

    "diffthetajets_ab":{"name":"diffthetajets_ab", "title":"Angular diff (#theta) between the jets a and b", "bin" :100, "xmin":0, "xmax":4},
    "diffthetajets_bc":{"name":"diffthetajets_bc", "title":"Angular diff (#theta) between the jets b and c", "bin" :100, "xmin":0, "xmax":4},
    "diffthetajets_ac":{"name":"diffthetajets_ac", "title":"Angular diff (#theta) between the jets a and c", "bin" :100, "xmin":0, "xmax":4},

    "diffphijets_ab":  {"name":"diffphijets_ab",   "title":"Angular diff (#phi) between the jets a and b",   "bin" :100, "xmin":0, "xmax":4},
    "diffphijets_bc":  {"name":"diffphijets_bc",   "title":"Angular diff (#phi) between the jets b and c",   "bin" :100, "xmin":0, "xmax":4},
    "diffphijets_ac":  {"name":"diffphijets_ac",   "title":"Angular diff (#phi) between the jets a and c",   "bin" :100, "xmin":0, "xmax":4},

    "dmerge_3_12":{"name":"dmerge_3_12","title":"dmerge_{12} (Durham kt N=3)","bin":125,"xmin":0,"xmax":12000},
    "dmerge_3_23":{"name":"dmerge_3_23","title":"dmerge_{23} (Durham kt N=3)","bin":125,"xmin":0,"xmax":100},
    "dmerge_3_34":{"name":"dmerge_3_34","title":"dmerge_{34} (Durham kt N=3)","bin":125,"xmin":0,"xmax":50},
    "dmerge_3_45":{"name":"dmerge_3_45","title":"dmerge_{45} (Durham kt N=3)","bin":125,"xmin":0,"xmax":50},
    
    #--------------------------------------------------------------------------------------------------------------------------------------------------Missing/Visible stuff

    "visible_mass_predef":      {"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":100, "xmax":300},
    #"visible_mass_predef_zoom": {"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":200, "xmax":240},

    "emiss":        {"name":"emiss",  "title":"Missing energy [GeV]",             "bin":100, "xmin":0,   "xmax":100},
    "pxmiss":       {"name":"pxmiss", "title":"Missing p_x [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pymiss":       {"name":"pymiss", "title":"Missing p_y [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pzmiss":       {"name":"pzmiss", "title":"Missing p_z [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "etmiss":       {"name":"etmiss", "title":"Missing transverse energy [GeV]",  "bin":100, "xmin":0,   "xmax":100}


}



    

