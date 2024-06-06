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
cutList = {"sel0":"Z1_theta < 10"   #No cut
           #"sel1":"emiss < 20",
           #"sel2":"emiss < 10",
           #"sel3":"Z1_m > 81 && Z1_m < 101",
           #"sel4":"Z2_m > 81 && Z2_m < 101",
           #"sel5":"Z3_m > 10 && Z3_m < 50",
           #"sel6":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50",
           #"sel7":"Z1_m > 81 && Z1_m < 101 && Z2_m > 81 && Z2_m < 101 && Z3_m > 10 && Z3_m < 50 && emiss < 10"
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #--------------------------------------------------------------------------------------------------------------------------------------------------Photons

    "N_photons":   {"name":"N_photons",  "title":"Number of photons",                                    "bin":10, "xmin":0, "xmax":10},
    "photons_e":   {"name":"photons_e",  "title":"Energy of the photons [GeV]",                          "bin":125,"xmin":0, "xmax":300},
    "photons_p":   {"name":"photons_p",  "title":"Momentum of the photons [GeV]",                        "bin":125,"xmin":0, "xmax":300},
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------Z bosons
    
    "Z1_e":        {"name":"Z1_e",       "title":"1st dilepton energy [GeV]",                            "bin":125,"xmin":0,"xmax":200},
    "Z1_m":        {"name":"Z1_m",       "title":"1st dilepton mass [GeV]",                              "bin":125,"xmin":0,"xmax":200},
    "Z1_p":        {"name":"Z1_p",       "title":"1st dilepton momentum [GeV]",                          "bin":125,"xmin":0,"xmax":200},
    "Z1_theta":    {"name":"Z1_theta",   "title":"#theta of the 1st lepton pair",                        "bin":100,"xmin":-7,"xmax":7},
    "Z1_phi":      {"name":"Z1_phi",     "title":"#phi of the 1st lepton pair",                          "bin":100,"xmin":-7,"xmax":7},
    "Z1_eta":      {"name":"Z1_eta",     "title":"Pseudo-rapidity #eta of the 1st lepton pair",          "bin":100,"xmin":-10,"xmax":10},
    "Z1_y":        {"name":"Z1_y",       "title":"Rapidity y of the 1st lepton pair",                    "bin":100,"xmin":-3,"xmax":3},
    "Z1_recoil_m": {"name":"Z1_recoil_m","title":"Leptonic recoil mass of the 1st lepton pair [GeV]",    "bin":100,"xmin":0,"xmax":200},
   
    "Z2_e":        {"name":"Z2_e",       "title":"2nd dilepton energy [GeV]",                            "bin":125,"xmin":0,"xmax":200},
    "Z2_m":        {"name":"Z2_m",       "title":"2nd dilepton mass [GeV]",                              "bin":125,"xmin":0, "xmax":160},
    "Z2_p":        {"name":"Z2_p",       "title":"2nd dilepton momentum [GeV]",                          "bin":125,"xmin":0, "xmax":120},
    "Z2_theta":    {"name":"Z2_theta",   "title":"#theta of the 2nd lepton pair ",                       "bin":100,"xmin":0, "xmax":4},
    "Z2_phi":      {"name":"Z2_phi",     "title":"#phi of the 2nd lepton pair",                          "bin":100,"xmin":-4,"xmax":4},
    "Z2_eta":      {"name":"Z2_eta",     "title":"Pseudo-rapidity #eta of the 2nd lepton pair",          "bin":100,"xmin":-6,"xmax":6},
    "Z2_y":        {"name":"Z2_y",       "title":"Rapidity y of the 2nd lepton pair",                    "bin":100,"xmin":-3,"xmax":3},
    "Z2_recoil_m": {"name":"Z2_recoil_m","title":"Leptonic recoil mass of the 2nd lepton pair [GeV]",    "bin":100,"xmin":0,"xmax":10},

    #--------------------------------------------------------------------------------------------------------------------------------------------------Leptons

    "N_on_taken_leptons":    {"name":"N_on_taken_leptons",  "title":"Number of selected high momentum leptons",    "bin":10, "xmin":0, "xmax":10},
    "N_off_taken_leptons":   {"name":"N_off_taken_leptons", "title":"Number of selected low momentum leptons",     "bin":10, "xmin":0, "xmax":10},

    "on_taken_leptons_e":        {"name":"on_taken_leptons_e",        "title":"Energy of selected high momentum leptons [GeV]",      "bin":100, "xmin":0, "xmax":100},
    "on_taken_leptons_p":        {"name":"on_taken_leptons_p",        "title":"Momentum of selected high momentum leptons [GeV]",    "bin":100, "xmin":0, "xmax":100},
    "on_taken_leptons_phi":      {"name":"on_taken_leptons_phi",      "title":"#phi of selected high momentum leptons",              "bin":100, "xmin":0, "xmax":100},
    "on_taken_leptons_theta":    {"name":"on_taken_leptons_theta",    "title":"#theta of selected high momentum leptons",            "bin":100, "xmin":0, "xmax":100},
    "on_taken_leptons_m":        {"name":"on_taken_leptons_m",        "title":"Mass of selected high momentum leptons [GeV]",        "bin":100, "xmin":0, "xmax":100},
    "on_taken_leptons_recoil_m": {"name":"on_taken_leptons_recoil_m", "title":"Recoil mass of selected high momentum leptons [GeV]", "bin":100, "xmin":0, "xmax":100},
    
    "off_taken_leptons_e":        {"name":"off_taken_leptons_e",        "title":"Energy of selected low momentum leptons [GeV]",      "bin":100, "xmin":0, "xmax":100},
    "off_taken_leptons_p":        {"name":"off_taken_leptons_p",        "title":"Momentum of selected low momentum leptons [GeV]",    "bin":100, "xmin":0, "xmax":100},
    "off_taken_leptons_phi":      {"name":"off_taken_leptons_phi",      "title":"#phi of selected low momentum leptons",              "bin":100, "xmin":0, "xmax":100},
    "off_taken_leptons_theta":    {"name":"off_taken_leptons_theta",    "title":"#theta of selected low momentum leptons",            "bin":100, "xmin":0, "xmax":100},
    "off_taken_leptons_m":        {"name":"off_taken_leptons_m",        "title":"Mass of selected low momentum leptons [GeV]",        "bin":100, "xmin":0, "xmax":100},
    "off_taken_leptons_recoil_m": {"name":"off_taken_leptons_recoil_m", "title":"Recoil mass of selected low momentum leptons [GeV]", "bin":100, "xmin":0, "xmax":100},

    "N_LooseLeptons_10":    {"name":"N_LooseLeptons_10",    "title":"Number of leptons with p>10 GeV",                   "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_2":     {"name":"N_LooseLeptons_2",     "title":"Number of leptons with p>2 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "N_LooseLeptons_1":     {"name":"N_LooseLeptons_1",     "title":"Number of leptons with p>1 GeV",                    "bin":20,  "xmin":0, "xmax":20},
    "LooseLeptons_10_pt":   {"name":"LooseLeptons_10_pt",   "title":"#p_t of leptons with p>10GeV [GeV]",                "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_p":    {"name":"LooseLeptons_10_p",    "title":"p of leptons with p>10GeV [GeV]",                   "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_10_theta":{"name":"LooseLeptons_10_theta","title":"#theta of leptons with p>10GeV [GeV]",              "bin":100, "xmin":0, "xmax":4},
    "LooseLeptons_10_phi":  {"name":"LooseLeptons_10_phi",  "title":"#phi of leptons with p>10 GeV [GeV]",               "bin":100, "xmin":-7,"xmax":7},
    
    "on_difftheta1_muons":      {"name":"on_difftheta1_muons",      "title":"on_difftheta1_muons",          "bin":100, "xmin":-7, "xmax":7},
    "on_difftheta2_muons":      {"name":"on_difftheta2_muons",      "title":"on_difftheta2_muons",          "bin":100, "xmin":-7, "xmax":7},
    "on_difftheta1_electrons":  {"name":"on_difftheta1_electrons",  "title":"on_difftheta1_electrons",      "bin":100, "xmin":-7, "xmax":7},
    "on_difftheta2_electrons":  {"name":"on_difftheta2_electrons",  "title":"on_difftheta2_electrons",      "bin":100, "xmin":-7, "xmax":7},

    "on_diffphi1_muons":        {"name":"on_diffphi1_muons",        "title":"on_diffphi1_muons",            "bin":100, "xmin":-7, "xmax":7},
    "on_diffphi2_muons":        {"name":"on_diffphi2_muons",        "title":"on_diffphi2_muons",            "bin":100, "xmin":-7, "xmax":7},
    "on_diffphi1_electrons":    {"name":"on_diffphi1_electrons",    "title":"on_diffphi1_electrons",        "bin":100, "xmin":-7, "xmax":7},
    "on_diffphi2_electrons":    {"name":"on_diffphi2_electrons",    "title":"on_diffphi2_electrons",        "bin":100, "xmin":-7, "xmax":7},

    "off_difftheta_muons":      {"name":"off_difftheta_muons",      "title":"off_difftheta_muons",          "bin":100, "xmin":-7, "xmax":7},
    "off_difftheta_electrons":  {"name":"off_difftheta_electrons",  "title":"off_difftheta_electrons",      "bin":100, "xmin":-7, "xmax":7},

    "off_diffphi_muons":        {"name":"off_diffphi_muons",        "title":"off_diffphi_muons",            "bin":100, "xmin":-7, "xmax":7},
    "off_diffphi_electrons":    {"name":"off_diffphi_electrons",    "title":"off_diffphi_electrons",        "bin":100, "xmin":-7, "xmax":7},

    #--------------------------------------------------------------------------------------------------------------------------------------------------Missing/Visible stuff

    "visible_mass_predef":      {"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":100, "xmax":300},
    
    "emiss":        {"name":"emiss",  "title":"Missing energy [GeV]",             "bin":100, "xmin":0,   "xmax":100},
    "pxmiss":       {"name":"pxmiss", "title":"Missing p_x [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pymiss":       {"name":"pymiss", "title":"Missing p_y [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "pzmiss":       {"name":"pzmiss", "title":"Missing p_z [GeV]",                "bin":100, "xmin":-80, "xmax":80},
    "etmiss":       {"name":"etmiss", "title":"Missing transverse energy [GeV]",  "bin":100, "xmin":0,   "xmax":100}


}



    

