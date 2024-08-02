#This file aims to plot the energy of the photons and the missing energy in order to determine the first cuts to apply on this variables next

#finalAA takes the output of stage1ter (or stage2) as input

#Input directory where the files produced at the pre-selection level are
inputDir  = "../outputs/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs"

processList = {#Signal
	           'wzp6_ee_mumuH_HZZ_ecm240':{},   
               'wzp6_ee_eeH_HZZ_ecm240':{},     
               'wzp6_ee_nunuH_HZZ_ecm240':{},   
               'wzp6_ee_qqH_HZZ_ecm240':{},
               'wzp6_ee_ssH_HZZ_ecm240':{},
               'wzp6_ee_bbH_HZZ_ecm240':{},
               'wzp6_ee_ccH_HZZ_ecm240':{},
               'wzp6_ee_tautauH_HZZ_ecm240':{},
               #Background
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               #'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               #'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               #'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
               'p8_ee_ZZ_ecm240':{},
               'p8_ee_WW_ecm240':{}
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
cutList = {"precuts": 				                            "emiss > -10",  
    	   "precuts_Z1_m":			                            "Z1_m < 110 && Z1_m > 80",
	       "precuts_Z1_m_Z2_m":			                        "Z1_m < 110 && Z1_m > 80 && Z2_m < 110 && Z2_m > 80",
           "precuts_Z1_m_Z2_m_emiss":                           "Z1_m < 110 && Z1_m > 80 && Z2_m < 110 && Z2_m > 80 && emiss < 8",
           "precuts_Z1_m_Z2_m_emiss_photon_e":                  "Z1_m < 110 && Z1_m > 80 && Z2_m < 110 && Z2_m > 80 && emiss < 8 && photon_e < 20",
           "precuts_Z1_m_Z2_m_emiss_photon_e_Z2a_recoil_m":     "Z1_m < 110 && Z1_m > 80 && Z2_m < 110 && Z2_m > 80 && emiss < 8 && photon_e < 20 && Z2a_recoil_m > 115",
           "region1":                                           "Z1_m < 110 && Z1_m > 80 && Z2_m < 110 && Z2_m > 80 && emiss < 8 && photon_e < 20 && Z2a_recoil_m > 115",
           "fitRegion":                                         "Z1_m < 110 && Z1_m > 80 && Z2_m < 110 && Z2_m > 80 && emiss < 8 && photon_e < 20 && Z2a_recoil_m > 115 && Z1_recoil_m > 115 && Z1_recoil_m < 140",
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    
    #"Name to appear on the file name": {"name of the variable to use", "title of the x axis of the plot", "bin number", "xmin", "xmax"}
    
    #Photon

    "photon_e":       {"name":"photon_e",          "title":"E^{#gamma} [GeV]",                                 "bin":200,  "xmin":0,      "xmax":100},
    "photon_px":      {"name":"photon_px",         "title":"p_{x} of the photon [GeV]",                        "bin":100,  "xmin":0,      "xmax":50},
    "photon_py":      {"name":"photon_py",         "title":"p_{y} of the photon [GeV]",                        "bin":100,  "xmin":0,      "xmax":50},
    "photon_pz":      {"name":"photon_pz",         "title":"p_{z} of the photon [GeV]",                        "bin":100,  "xmin":0,      "xmax":50},
    "photon_theta":   {"name":"photon_theta",      "title":"#theta of the photon",               		       "bin":100,  "xmin":0,      "xmax":3.5}, 
    "photon_phi":     {"name":"photon_phi",        "title":"#varphi of the photon",             	      	   "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "photon_eta":     {"name":"photon_eta",        "title":"#eta of the photon",                               "bin":100,  "xmin":-10,    "xmax":10},
    
    #Missing/Visible

    "emiss":          {"name":"emiss",          "title":"E^{miss} [GeV]",                                "bin":100,  "xmin":0,     "xmax":130},
    "etmiss":         {"name":"etmiss",         "title":"Missing Transverse Energy [GeV]",               "bin":100,  "xmin":0,     "xmax":130},
    "pxmiss":         {"name":"pxmiss",         "title":"Missing p_{x} [GeV]",                           "bin":100,  "xmin":-40,   "xmax":40},
    "pymiss":         {"name":"pymiss",         "title":"Missing p_{y} [GeV]",                           "bin":100,  "xmin":-40,   "xmax":40},
    "pzmiss":         {"name":"pzmiss",         "title":"Missing p_{z} [GeV]",                           "bin":100,  "xmin":-40,   "xmax":40},
    "visible_m":      {"name":"visible_m",      "title":"Visible Mass [GeV]",                            "bin":200,  "xmin":100,   "xmax":250},
    "missing_theta":  {"name":"missing_theta",  "title":"Missing #theta [GeV]",                          "bin":100,  "xmin":0,    "xmax":3.5},

    #Dijet

    "jj_e":           {"name":"jj_e",          "title":"E(jj) [GeV]",                        "bin":100,  "xmin":0,     "xmax":130},
    "jj_p":           {"name":"jj_p",          "title":"p(jj) [GeV]",                        "bin":100,  "xmin":0,     "xmax":100},
    "jj_px":          {"name":"jj_px",         "title":"p_{x}(jj) [GeV]",                    "bin":100,  "xmin":-40,   "xmax":40},
    "jj_py":          {"name":"jj_py",         "title":"p_{y}(jj) [GeV]",                    "bin":100,  "xmin":-40,   "xmax":40},
    "jj_pz":          {"name":"jj_pz",         "title":"p_{z}(jj) [GeV]",                    "bin":100,  "xmin":-40,   "xmax":40},
    "jj_pt":          {"name":"jj_pt",         "title":"p_{t}(jj) [GeV]",                    "bin":100,  "xmin":0,     "xmax":100},
    "jj_theta":       {"name":"jj_theta",      "title":"#theta(jj)",                         "bin":100,  "xmin":0,     "xmax":3.5},
    "jj_phi":         {"name":"jj_phi",        "title":"#phi(jj)",                           "bin":100,  "xmin":-3.5,  "xmax":3.5},
    "jj_eta":         {"name":"jj_eta",        "title":"#eta(jj)",                           "bin":100,  "xmin":-10,   "xmax":10},
    "jj_m":           {"name":"jj_m",          "title":"m(jj) [GeV]",                        "bin":100,  "xmin":0,     "xmax":130},

    #j1 (1st jet) and j2 (2nd jet)

    "j1_e":           {"name":"j1_e",          "title":"E(j_{1}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":120},
    "j1_p":           {"name":"j1_p",          "title":"p(j_{1}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":120},
    "j1_px":          {"name":"j1_px",         "title":"p_{x}(j_{1}) [GeV]",                    "bin":100,  "xmin":-90,   "xmax":90},
    "j1_py":          {"name":"j1_py",         "title":"p_{y}(j_{1}) [GeV]",                    "bin":100,  "xmin":-90,   "xmax":90},
    "j1_pz":          {"name":"j1_pz",         "title":"p_{z}(j_{1}) [GeV]",                    "bin":100,  "xmin":-90,   "xmax":90},
    "j1_pt":          {"name":"j1_pt",         "title":"p_{t}(j_{1}) [GeV]",                    "bin":100,  "xmin":0,     "xmax":150},
    "j1_theta":       {"name":"j1_theta",      "title":"#theta(j_{1})",                         "bin":100,  "xmin":0,     "xmax":3.5},
    "j1_phi":         {"name":"j1_phi",        "title":"#phi(j_{1})",                           "bin":100,  "xmin":-1,    "xmax":7},
    "j1_m":           {"name":"j1_m",          "title":"m(j_{1}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j1_eta":         {"name":"j1_eta",        "title":"#eta(j_{1}) [GeV]",                     "bin":100,  "xmin":-10,   "xmax":10},

    "j2_e":           {"name":"j2_e",          "title":"E(j_{2}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j2_p":           {"name":"j2_p",          "title":"p(j_{2}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j2_px":          {"name":"j2_px",         "title":"p_{x}(j_{2}) [GeV]",                    "bin":100,  "xmin":-80,   "xmax":80},
    "j2_py":          {"name":"j2_py",         "title":"p_{y}(j_{2}) [GeV]",                    "bin":100,  "xmin":-80,   "xmax":80},
    "j2_pz":          {"name":"j2_pz",         "title":"p_{z}(j_{2}) [GeV]",                    "bin":100,  "xmin":-80,   "xmax":80},
    "j2_pt":          {"name":"j2_pt",         "title":"p_{t}(j_{2}) [GeV]",                    "bin":100,  "xmin":0,     "xmax":150},
    "j2_theta":       {"name":"j2_theta",      "title":"#theta(j_{2})",                         "bin":100,  "xmin":0,     "xmax":3.5},
    "j2_phi":         {"name":"j2_phi",        "title":"#phi(j_{2})",                           "bin":100,  "xmin":-1,    "xmax":7},
    "j2_m":           {"name":"j2_m",          "title":"m(j_{2}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j2_eta":         {"name":"j2_eta",        "title":"#eta(j_{2}) [GeV]",                     "bin":100,  "xmin":-10,   "xmax":10},
    
    #Z1 (1st dilepton) and Z2 (2nd dilepton)
    
    "Z1_e":           {"name":"Z1_e",              "title":"E(Z_{1}) [GeV]",           	         "bin":150,  "xmin":10,     "xmax":180},
    "Z1_p":           {"name":"Z1_p",              "title":"p(Z_{1}) [GeV]",          			 "bin":100,  "xmin":0,      "xmax":160},
    "Z1_px":          {"name":"Z1_px",             "title":"p_{x}(Z_{1}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Z1_py":          {"name":"Z1_py",             "title":"p_{y}(Z_{1}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Z1_pz":          {"name":"Z1_pz",             "title":"p_{z}(Z_{1}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Z1_theta":       {"name":"Z1_theta",          "title":"#theta(Z_{1})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Z1_phi":         {"name":"Z1_phi",            "title":"#phi(Z_{1})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Z1_m":           {"name":"Z1_m",              "title":"m_{ll_{1}} [GeV]",            		 "bin":150,  "xmin":0,      "xmax":150},
    "Z1_recoil_m":    {"name":"Z1_recoil_m",       "title":"m^{rec}_{ll_{1}} [GeV]",             "bin":150,  "xmin":20,     "xmax":200},
    "Z1_eta":         {"name":"Z1_eta",            "title":"#eta(Z_{1})",                        "bin":100,  "xmin":-10,    "xmax":10},
    "Z1a_recoil_m":   {"name":"Z1a_recoil_m",      "title":"m^{rec}_{ll_{1} + #gamma} [GeV]",    "bin":150,  "xmin":20,     "xmax":190},
    
    "Z2_e":           {"name":"Z2_e",              "title":"E(Z_{2}) [GeV]",           			 "bin":150,  "xmin":10,     "xmax":180},
    "Z2_p":           {"name":"Z2_p",              "title":"p(Z_{2}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":80},
    "Z2_px":          {"name":"Z2_px",             "title":"p_{x}(Z_{2}) [GeV]",           		 "bin":100,  "xmin":-60,    "xmax":60},
    "Z2_py":          {"name":"Z2_py",             "title":"p_{y}(Z_{2}) [GeV]",           		 "bin":100,  "xmin":-60,    "xmax":60},
    "Z2_pz":          {"name":"Z2_pz",             "title":"p_{z}(Z_{2}) [GeV]",           		 "bin":100,  "xmin":-60,    "xmax":60},
    "Z2_theta":       {"name":"Z2_theta",          "title":"#theta(Z_{2})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Z2_phi":         {"name":"Z2_phi",            "title":"#phi(Z_{2})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Z2_m":           {"name":"Z2_m",              "title":"m_{ll_{2}} [GeV]",            		 "bin":150,  "xmin":0,      "xmax":180},
    "Z2_recoil_m":    {"name":"Z2_recoil_m",       "title":"m^{rec}_{ll_{2}} [GeV]",             "bin":200,  "xmin":0,      "xmax":210},
    "Z2_eta":         {"name":"Z2_eta",            "title":"#eta(Z_{2})",                        "bin":100,  "xmin":-10,    "xmax":10},
    "Z2a_recoil_m":   {"name":"Z2a_recoil_m",      "title":"m^{rec}_{ll_{2} + #gamma} [GeV]",    "bin":200,  "xmin":0,      "xmax":200},
    "Z2jj_m":         {"name":"Z2jj_m",            "title":"m(Z_{2} + jj) [GeV]",                "bin":100,  "xmin":50,     "xmax":210},
    "Z2miss_m":       {"name":"Z2miss_m",          "title":"m(Z_{2} + #nu#nu) [GeV]",            "bin":100,  "xmin":50,     "xmax":210},

    "Z1_recoil_m_zoom":    {"name":"Z1_recoil_m",       "title":"m^{rec}_{ll_{1}} [GeV]",             "bin":150,  "xmin":100,     "xmax":160},
    "Z2_recoil_m_zoom":    {"name":"Z2_recoil_m",       "title":"m^{rec}_{ll_{2}} [GeV]",             "bin":150,  "xmin":100,     "xmax":180},

    #To use for combine
    "Z1_recoil_m_fit":     {"name":"Z1_recoil_m",       "title":"m^{rec}_{ll_{1}} [GeV]",             "bin":25,   "xmin":115,     "xmax":140},
    

}



    
