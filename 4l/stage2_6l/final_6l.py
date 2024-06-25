#This file aims to plot the energy of the photons and the missing energy in order to determine the first cuts to apply on this variables next

#Input directory where the files produced at the pre-selection level are
inputDir  = "../outputs/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs"

processList = {#Signal
               'wzp6_ee_mumuH_HZZ_ecm240':{},
               'wzp6_ee_eeH_HZZ_ecm240':{},
               #'wzp6_ee_nunuH_HZZ_ecm240':{},   
               #'wzp6_ee_qqH_HZZ_ecm240':{},
               #'wzp6_ee_ssH_HZZ_ecm240':{},
               #'wzp6_ee_bbH_HZZ_ecm240':{},
               #'wzp6_ee_ccH_HZZ_ecm240':{},
               #Background
               #'wzp6_ee_mumuH_HWW_ecm240':{},
               #'wzp6_ee_mumuH_HZa_ecm240':{},
               #'wzp6_ee_mumuH_Haa_ecm240':{},
               #'wzp6_ee_mumuH_Hbb_ecm240':{},
               #'wzp6_ee_mumuH_Hcc_ecm240':{},
               #'wzp6_ee_mumuH_Hgg_ecm240':{},
               #'wzp6_ee_mumuH_Hmumu_ecm240':{},
               #'wzp6_ee_mumuH_Hss_ecm240':{},
               #'wzp6_ee_mumuH_Htautau_ecm240':{},
               #'wzp6_ee_nunuH_HWW_ecm240':{},
               #'wzp6_ee_nunuH_HZa_ecm240':{},
               #'wzp6_ee_nunuH_Haa_ecm240':{},
               #'wzp6_ee_nunuH_Hbb_ecm240':{},
               #'wzp6_ee_nunuH_Hcc_ecm240':{},
               #'wzp6_ee_nunuH_Hgg_ecm240':{},   
               #'wzp6_ee_nunuH_Hmumu_ecm240':{},
               #'wzp6_ee_nunuH_Hss_ecm240':{},
               #'wzp6_ee_nunuH_Htautau_ecm240':{},
               #'wzp6_ee_eeH_HWW_ecm240':{},
               #'wzp6_ee_eeH_HZa_ecm240':{},
               #'wzp6_ee_eeH_Haa_ecm240':{},
               #'wzp6_ee_eeH_Hbb_ecm240':{},
               #'wzp6_ee_eeH_Hcc_ecm240':{},
               #'wzp6_ee_eeH_Hgg_ecm240':{},
               #'wzp6_ee_eeH_Hmumu_ecm240':{},
               #'wzp6_ee_eeH_Hss_ecm240':{},
               #'wzp6_ee_eeH_Htautau_ecm240':{},
               'p8_ee_ZZ_ecm240':{},
               #'p8_ee_WW_ecm240':{}
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
cutList = {"precuts":"emiss > -10"
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #Photon

    "photon_e":       {"name":"photon_e",          "title":"Energy of the photon [GeV]",                       "bin":100,  "xmin":0,      "xmax":50},
    "photon_theta":   {"name":"photon_theta",      "title":"#theta of the photon",                             "bin":100,  "xmin":0,      "xmax":3.5},
    "photon_phi":     {"name":"photon_phi",        "title":"#varphi of the photon",                            "bin":100,  "xmin":-3.5,   "xmax":3.5},

    #Dilepton

    "ll1a_m":         {"name":"ll1a_m",            "title":"Mass of the 1st Dilepton + Photon [GeV]",          "bin":100,  "xmin":10,     "xmax":150},
    "ll2a_m":         {"name":"ll2a_m",            "title":"Mass of the 2nd Dilepton + Photon [GeV]",          "bin":100,  "xmin":10,     "xmax":150},
    "ll3a_m":         {"name":"ll3a_m",            "title":"Mass of the 3rd Dilepton + Photon [GeV]",          "bin":100,  "xmin":10,     "xmax":150},

    "ll1_theta_diff": {"name":"ll1_theta_diff",    "title":"Angular Difference (#theta) of the 1st Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll1_phi_diff":   {"name":"ll1_phi_diff",      "title":"Angular Difference (#varphi) of the 1st Dilepton", "bin":100,  "xmin":0,      "xmax":7},
    "ll2_theta_diff": {"name":"ll2_theta_diff",    "title":"Angular Difference (#theta) of the 2nd Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll2_phi_diff":   {"name":"ll2_phi_diff",      "title":"Angular Difference (#varphi) of the 2nd Dilepton", "bin":100,  "xmin":0,      "xmax":7},
    "ll3_theta_diff": {"name":"ll3_theta_diff",    "title":"Angular Difference (#theta) of the 3rd Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll3_phi_diff":   {"name":"ll3_phi_diff",      "title":"Angular Difference (#varphi) of the 3rd Dilepton", "bin":100,  "xmin":0,      "xmax":7},

    #Za (1st dilepton) and Zb (2nd dilepton)
    
    "Za_e":           {"name":"Za_e",              "title":"Za_e [GeV]",                         "bin":150,  "xmin":10,     "xmax":180},
    "Za_p":           {"name":"Za_p",              "title":"Za_p [GeV]",                         "bin":100,  "xmin":0,      "xmax":80},
    "Za_px":          {"name":"Za_px",             "title":"Za_px [GeV]",                        "bin":100,  "xmin":-70,    "xmax":70},
    "Za_py":          {"name":"Za_py",             "title":"Za_py [GeV]",                        "bin":100,  "xmin":-70,    "xmax":70},
    "Za_pz":          {"name":"Za_pz",             "title":"Za_pz [GeV]",                        "bin":100,  "xmin":-70,    "xmax":70},
    "Za_theta":       {"name":"Za_theta",          "title":"Za_theta",                           "bin":100,  "xmin":0,      "xmax":3.5},
    "Za_phi":         {"name":"Za_phi",            "title":"Za_phi",                             "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Za_m":           {"name":"Za_m",              "title":"Za_m [GeV]",                         "bin":150,  "xmin":10,     "xmax":130},
    "Za_recoil_m":    {"name":"Za_recoil_m",       "title":"Za_recoil_m [GeV]",                  "bin":100,  "xmin":90,     "xmax":200},

    "Zb_e":           {"name":"Zb_e",              "title":"Zb_e [GeV]",                         "bin":150,  "xmin":10,     "xmax":180},
    "Zb_p":           {"name":"Zb_p",              "title":"Zb_p [GeV]",                         "bin":100,  "xmin":0,      "xmax":80},
    "Zb_px":          {"name":"Zb_px",             "title":"Zb_px [GeV]",                        "bin":100,  "xmin":-60,    "xmax":60},
    "Zb_py":          {"name":"Zb_py",             "title":"Zb_py [GeV]",                        "bin":100,  "xmin":-60,    "xmax":60},
    "Zb_pz":          {"name":"Zb_pz",             "title":"Zb_pz [GeV]",                        "bin":100,  "xmin":-60,    "xmax":60},
    "Zb_theta":       {"name":"Zb_theta",          "title":"Zb_theta",                           "bin":100,  "xmin":0,      "xmax":3.5},
    "Zb_phi":         {"name":"Zb_phi",            "title":"Zb_phi",                             "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Zb_m":           {"name":"Zb_m",              "title":"Zb_m [GeV]",                         "bin":150,  "xmin":10,     "xmax":130},
    "Zb_recoil_m":    {"name":"Zb_recoil_m",       "title":"Zb_recoil_m [GeV]",                  "bin":100,  "xmin":240,    "xmax":170},
    
    "Zc_e":           {"name":"Zc_e",              "title":"Zc_e [GeV]",                         "bin":150,  "xmin":0,      "xmax":180},
    "Zc_p":           {"name":"Zc_p",              "title":"Zc_p [GeV]",                         "bin":100,  "xmin":0,      "xmax":80},
    "Zc_px":          {"name":"Zc_px",             "title":"Zc_px [GeV]",                        "bin":100,  "xmin":-60,    "xmax":60},
    "Zc_py":          {"name":"Zc_py",             "title":"Zc_py [GeV]",                        "bin":100,  "xmin":-60,    "xmax":60},
    "Zc_pz":          {"name":"Zc_pz",             "title":"Zc_pz [GeV]",                        "bin":100,  "xmin":-60,    "xmax":60},
    "Zc_theta":       {"name":"Zc_theta",          "title":"Zc_theta",                           "bin":100,  "xmin":0,      "xmax":3.5},
    "Zc_phi":         {"name":"Zc_phi",            "title":"Zc_phi",                             "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Zc_m":           {"name":"Zc_m",              "title":"Zc_m [GeV]",                         "bin":150,  "xmin":10,     "xmax":130},
    "Zc_recoil_m":    {"name":"Zc_recoil_m",       "title":"Zc_recoil_m [GeV]",                  "bin":150,  "xmin":120,    "xmax":240},

    #Dijet

    "jj_e":           {"name":"jj_e",          "title":"jj_e [GeV]",                         "bin":100,  "xmin":0,     "xmax":150},
    "jj_p":           {"name":"jj_p",          "title":"jj_p [GeV]",                         "bin":100,  "xmin":0,     "xmax":100},
    "jj_px":          {"name":"jj_px",         "title":"jj_px [GeV]",                        "bin":100,  "xmin":-40,   "xmax":40},
    "jj_py":          {"name":"jj_py",         "title":"jj_py [GeV]",                        "bin":100,  "xmin":-40,   "xmax":40},
    "jj_pz":          {"name":"jj_pz",         "title":"jj_pz [GeV]",                        "bin":100,  "xmin":-40,   "xmax":40},
    "jj_theta":       {"name":"jj_theta",      "title":"jj_theta",                           "bin":100,  "xmin":0,     "xmax":3.5},
    "jj_phi":         {"name":"jj_phi",        "title":"jj_phi",                             "bin":100,  "xmin":-3.5,  "xmax":3.5},
    "jj_m":           {"name":"jj_m",          "title":"jj_m [GeV]",                         "bin":100,  "xmin":0,     "xmax":150},

    #Missing Energy

    "emiss":          {"name":"emiss",          "title":"Missing Energy [GeV]",                          "bin":100,  "xmin":0,     "xmax":200},
    "pxmiss":         {"name":"pxmiss",         "title":"Missing p_{x} [GeV]",                           "bin":100,  "xmin":-40,   "xmax":40},
    "pymiss":         {"name":"pymiss",         "title":"Missing p_{y} [GeV]",                           "bin":100,  "xmin":-40,   "xmax":40},
    "pzmiss":         {"name":"pzmiss",         "title":"Missing p_{z} [GeV]",                           "bin":100,  "xmin":-40,   "xmax":40},

    #Visible Mass

    "visible_m":      {"name":"visible_m",      "title":"Visible Mass [GeV]",                            "bin":100,  "xmin":170,   "xmax":250},
    "missing_m":      {"name":"missing_m",      "title":"Missing Mass [GeV]",                            "bin":100,  "xmin":0,     "xmax":250},
    "missing_theta":  {"name":"missing_theta",  "title":"Missing #theta",                                "bin":100,  "xmin":0,     "xmax":3.5}
}




    
