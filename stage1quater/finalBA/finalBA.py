#This file aims to plot the energy of the photons and the missing energy in order to determine the first cuts to apply on this variables next

#Input directory where the files produced at the pre-selection level are
#Takes as input the output of stage2
inputDir  = "../stage2/outputs/"

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
               'wzp6_ee_eeH_Hgg_ecm240':{},
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
cutList = {"precuts":	  			    "emiss > -10",
    	   "precuts_Za_m":			    "Za_m < 110 && Za_m > 80",
	       "precuts_Za_m_Zb_m":	   		"Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10",  
           "precuts_Za_m_Zb_m_emiss":	"Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8",

           "lljjll":                    "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc > 0",
           "lljjll_jj_m":               "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc > 0 && jj_m > 80 && jj_m < 110",
           "lljjll_jj_m_Zb_recoil_m":   "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc > 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 190 && Zb_recoil_m < 215",
           "lljjll_jj_m_Zb_recoil_m_ll2jj_recoil_m":"Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc > 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 190 && Zb_recoil_m < 215 && ll2jj_recoil_m > 80 && ll2jj_recoil_m < 110",

           "jjllll":                    "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc < 0",
           "jjllll_jj_m":               "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc < 0 && jj_m > 80 && jj_m < 110",
           "jjllll_jj_m_Zb_recoil_m":   "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc < 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 195 && Zb_recoil_m < 215",
           
           "region1":                   "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc > 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 190 && Zb_recoil_m < 215 && ll2jj_recoil_m > 80 && ll2jj_recoil_m < 110",
           "region2":                   "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc < 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 195 && Zb_recoil_m < 215",

           "fitRegion1":                "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc > 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 190 && Zb_recoil_m < 215 && ll2jj_recoil_m > 80 && ll2jj_recoil_m < 110 && ll2jj_m > 108 && ll2jj_m < 135",
           "fitRegion2":                "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss < 8 && disc < 0 && jj_m > 80 && jj_m < 110 && Zb_recoil_m > 195 && Zb_recoil_m < 215 && ZZ_m > 112 && ZZ_m < 135",
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #Photon
    
    "photon_e":       {"name":"photon_e",          "title":"Energy of the photon [GeV]",                       "bin":100,  "xmin":0,      "xmax":80},
    "photon_px":      {"name":"photon_px",         "title":"p_{x} of the photon [GeV]",                        "bin":100,  "xmin":0,      "xmax":80},
    "photon_py":      {"name":"photon_py",         "title":"p_{y} of the photon [GeV]",                        "bin":100,  "xmin":0,      "xmax":80},
    "photon_pz":      {"name":"photon_pz",         "title":"p_{z} of the photon [GeV]",                        "bin":100,  "xmin":0,      "xmax":80},
    "photon_theta":   {"name":"photon_theta",      "title":"#theta of the photon",               		       "bin":100,  "xmin":0,      "xmax":3.5}, 
    "photon_phi":     {"name":"photon_phi",        "title":"#varphi of the photon",             	      	   "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "photon_eta":     {"name":"photon_eta",        "title":"#eta of the photon",                               "bin":100,  "xmin":-10,    "xmax":10},
   
    #Dilepton
    
    "ll1a_recoil_m":  {"name":"ll1a_recoil_m",     "title":"m^{rec}_{ll+#gamma}",                          "bin":100,  "xmin":0,      "xmax":200},
    "ll2a_recoil_m":  {"name":"ll2a_recoil_m",     "title":"m^{rec}_{ll_{3}+#gamma}",                          "bin":150,  "xmin":0,      "xmax":250},

    "ll1jj_m":        {"name":"ll1jj_m",           "title":"Mass of the 1st Dilepton + Dijet [GeV]",           "bin":100,  "xmin":20,     "xmax":240},
    "ll2jj_m":        {"name":"ll2jj_m",           "title":"m_{jj+ll_{3}} [GeV]",                              "bin":100,  "xmin":0,      "xmax":240},
    "ll2jj_m_zoom":   {"name":"ll2jj_m",           "title":"m_{jj+ll_{3}} [GeV]",                              "bin":100,  "xmin":80,     "xmax":150},
    "ll2jj_recoil_m": {"name":"ll2jj_recoil_m",    "title":"m^{rec}_{jj+ll_{3}} [GeV]",                        "bin":150,  "xmin":0,      "xmax":240},
    
    "ll1miss_m":      {"name":"ll1miss_m",         "title":"Mass of the 1st Dilepton + Missing tlv [GeV]",     "bin":100,  "xmin":0,      "xmax":200},
    "ll2miss_m":      {"name":"ll2miss_m",         "title":"Mass of the 2nd Dilepton + Missing tlv [GeV]",     "bin":100,  "xmin":0,      "xmax":150},

    "ZZ_m":           {"name":"ZZ_m",              "title":"m(Z_{a}+Z_{3})",                                   "bin":100,  "xmin":50,     "xmax":160},
    "ZZ_p":           {"name":"ZZ_p",              "title":"ZZ_p",                                             "bin":100,  "xmin":0,      "xmax":100},
    "ZZ_m_zoom":      {"name":"ZZ_m",              "title":"m_{ll_{2}+ll_{3}}",                                "bin":100,  "xmin":100,    "xmax":150},
    "ZZ_recoil_m":    {"name":"ZZ_recoil_m",       "title":"m_{rec}(Z_{a}+Z_{3})",                             "bin":100,  "xmin":50,     "xmax":160},

    #Za (1st dilepton) and Zb (2nd dilepton)
    
    "Za_e":           {"name":"Za_e",              "title":"E(Z_{a}) [GeV]",           	         "bin":150,  "xmin":0,      "xmax":160},
    "Za_p":           {"name":"Za_p",              "title":"p(Z_{a}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":180},
    "Za_px":          {"name":"Za_px",             "title":"p_{x}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_py":          {"name":"Za_py",             "title":"p_{y}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_pz":          {"name":"Za_pz",             "title":"p_{z}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_theta":       {"name":"Za_theta",          "title":"#theta(Z_{a})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Za_phi":         {"name":"Za_phi",            "title":"#phi(Z_{a})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Za_m":           {"name":"Za_m",              "title":"m_{ll} [GeV]",              		 "bin":150,  "xmin":0,      "xmax":200},
    "Za_recoil_m":    {"name":"Za_recoil_m",       "title":"m^{rec}_{ll}",                       "bin":200,  "xmin":0,      "xmax":210},
    "Za_eta":         {"name":"Za_eta",            "title":"#eta(Z_{a})",                        "bin":100,  "xmin":-10,    "xmax":10},
    
    "Zb_e":           {"name":"Zb_e",              "title":"E(Z_{b}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":200},
    "Zb_p":           {"name":"Zb_p",              "title":"p(Z_{b}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":180},
    "Zb_px":          {"name":"Zb_px",             "title":"p_{x}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-100,   "xmax":100},
    "Zb_py":          {"name":"Zb_py",             "title":"p_{y}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-100,   "xmax":100},
    "Zb_pz":          {"name":"Zb_pz",             "title":"p_{z}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-100,   "xmax":100},
    "Zb_theta":       {"name":"Zb_theta",          "title":"#theta(Z_{b})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Zb_phi":         {"name":"Zb_phi",            "title":"#phi(Z_{b})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Zb_m":           {"name":"Zb_m",              "title":"m_{ll_{3}} [GeV]",         			 "bin":200,  "xmin":0,      "xmax":200},
    "Zbmiss_m":       {"name":"Zbmiss_m",          "title":"Zbmiss_m[GeV]",                      "bin":200,  "xmin":0,      "xmax":200},
    "Zb_recoil_m":    {"name":"Zb_recoil_m",       "title":"m^{rec}_{ll_{3}} [GeV]",             "bin":100,  "xmin":0,      "xmax":250},
    "Zb_eta":         {"name":"Zb_eta",            "title":"#eta(Z_{b})",                        "bin":100,  "xmin":-10,    "xmax":10},
     
    #Dijet
  
    "jj_e":           {"name":"jj_e",          "title":"E(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":200},
    "jj_p":           {"name":"jj_p",          "title":"p(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":200},
    "jj_px":          {"name":"jj_px",         "title":"p_{x}(jj) [GeV]",              		 "bin":100,  "xmin":-80,   "xmax":80},
    "jj_py":          {"name":"jj_py",         "title":"p_{y}(jj) [GeV]",              		 "bin":100,  "xmin":-80,   "xmax":80},
    "jj_pz":          {"name":"jj_pz",         "title":"p_{z}(jj) [GeV]",              		 "bin":100,  "xmin":-80,   "xmax":80},
    "jj_theta":       {"name":"jj_theta",      "title":"#theta(jj)",               			 "bin":100,  "xmin":0,     "xmax":3.5},
    "jj_phi":         {"name":"jj_phi",        "title":"#phi(jj)",             			     "bin":100,  "xmin":-3.5,  "xmax":3.5},
    "jj_m":           {"name":"jj_m",          "title":"m_{jj} [GeV]",             			 "bin":100,  "xmin":0,     "xmax":200},
    "jj_recoil_m":    {"name":"jj_recoil_m",   "title":"m^{rec}_{jj} [GeV]",                 "bin":200,  "xmin":0,     "xmax":200},
    "jj_eta":         {"name":"jj_eta",        "title":"#eta(jj)",                           "bin":100,  "xmin":-10,   "xmax":10},

    #j1 (1st jet) and j2 (2nd jet)

    "j1_e":           {"name":"j1_e",          "title":"E(j_{1}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":120},
    "j1_p":           {"name":"j1_p",          "title":"p(j_{1}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":120},
    "j1_px":          {"name":"j1_px",         "title":"p_{x}(j_{1}) [GeV]",                    "bin":100,  "xmin":-90,   "xmax":90},
    "j1_py":          {"name":"j1_py",         "title":"p_{y}(j_{1}) [GeV]",                    "bin":100,  "xmin":-90,   "xmax":90},
    "j1_pz":          {"name":"j1_pz",         "title":"p_{z}(j_{1}) [GeV]",                    "bin":100,  "xmin":-90,   "xmax":90},
    "j1_theta":       {"name":"j1_theta",      "title":"#theta(j_{1})",                         "bin":100,  "xmin":0,     "xmax":3.5},
    "j1_phi":         {"name":"j1_phi",        "title":"#phi(j_{1})",                           "bin":100,  "xmin":-1,    "xmax":7},
    "j1_m":           {"name":"j1_m",          "title":"m(j_{1}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j1_eta":         {"name":"j1_eta",        "title":"#eta(j_{1}) [GeV]",                     "bin":100,  "xmin":-10,   "xmax":10},

    "j2_e":           {"name":"j2_e",          "title":"E(j_{2}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j2_p":           {"name":"j2_p",          "title":"p(j_{2}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j2_px":          {"name":"j2_px",         "title":"p_{x}(j_{2}) [GeV]",                    "bin":100,  "xmin":-80,   "xmax":80},
    "j2_py":          {"name":"j2_py",         "title":"p_{y}(j_{2}) [GeV]",                    "bin":100,  "xmin":-80,   "xmax":80},
    "j2_pz":          {"name":"j2_pz",         "title":"p_{z}(j_{2}) [GeV]",                    "bin":100,  "xmin":-80,   "xmax":80},
    "j2_theta":       {"name":"j2_theta",      "title":"#theta(j_{2})",                         "bin":100,  "xmin":0,     "xmax":3.5},
    "j2_phi":         {"name":"j2_phi",        "title":"#phi(j_{2})",                           "bin":100,  "xmin":-1,    "xmax":7},
    "j2_m":           {"name":"j2_m",          "title":"m(j_{2}) [GeV]",                        "bin":100,  "xmin":0,     "xmax":80},
    "j2_eta":         {"name":"j2_eta",        "title":"#eta(j_{2}) [GeV]",                     "bin":100,  "xmin":-10,   "xmax":10},
    
    #Missing Energy
        
    "emiss":          {"name":"emiss",          "title":"E^{miss} [GeV]",                       		 "bin":100,  "xmin":0,     "xmax":140},
    "etmiss":         {"name":"etmiss",         "title":"Missing transverse energy [GeV]",               "bin":100,  "xmin":0,     "xmax":150},
    "pxmiss":         {"name":"pxmiss",         "title":"Missing p_{x} [GeV]",               			 "bin":100,  "xmin":-80,   "xmax":80},
    "pymiss":         {"name":"pymiss",         "title":"Missing p_{y} [GeV]",               			 "bin":100,  "xmin":-80,   "xmax":80},
    "pzmiss":         {"name":"pzmiss",         "title":"Missing p_{z} [GeV]",               			 "bin":100,  "xmin":-80,   "xmax":80},

    "visible_m":      {"name":"visible_m",      "title":"Visible Mass [GeV]",                            "bin":200,  "xmin":70,   "xmax":250},
    "missing_theta":  {"name":"missing_theta",  "title":"Missing #theta [GeV]",                          "bin":100,  "xmin":0,    "xmax":3.5},

    "Za_recoil_m_zoom":    {"name":"Za_recoil_m",       "title":"m^{rec}_{ll_{a}} [GeV]",            "bin":100,  "xmin":100,      "xmax":160},
    "Zb_recoil_m_zoom":    {"name":"Zb_recoil_m",       "title":"m^{rec}_{ll_{3}} [GeV]",            "bin":100,  "xmin":150,      "xmax":250},

    #Leptons

    "ll1_angle":    {"name":"ll1_angle",       "title":"ll1_angle",            "bin":100,  "xmin":-1,      "xmax":3.5},
    "ll1_theta_diff": {"name":"ll1_theta_diff",    "title":"Angular Difference (#theta) of the 1st Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll1_phi_diff":   {"name":"ll1_phi_diff",      "title":"Angular Difference (#varphi) of the 1st Dilepton", "bin":100,  "xmin":0,      "xmax":7},
    "ll1_delta_R":    {"name":"ll1_delta_R",       "title":"#Delta R of the 1st Dilepton",                     "bin":100,  "xmin":0,      "xmax":10},

    "ll2_angle":    {"name":"ll2_angle",       "title":"ll2_angle",            "bin":100,  "xmin":-1,      "xmax":3.5},
    "ll2_theta_diff": {"name":"ll2_theta_diff",    "title":"Angular Difference (#theta) of the 2nd Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll2_phi_diff":   {"name":"ll2_phi_diff",      "title":"Angular Difference (#varphi) of the 2nd Dilepton", "bin":100,  "xmin":0,      "xmax":7},
    "ll2_delta_R":    {"name":"ll2_delta_R",       "title":"#Delta R of the 2nd Dilepton",                     "bin":100,  "xmin":0,      "xmax":10},

    "lj1_theta_diff_min":{"name":"lj1_theta_diff_min",       "title":"lj1_theta_diff_min",        "bin":100,  "xmin":0,      "xmax":3.5},
    "lj1_phi_diff_min":{"name":"lj1_phi_diff_min",   "title":"lj1_phi_diff_min",        "bin":100,  "xmin":0,      "xmax":7},
    "lj1_delta_R_min":{"name":"lj1_delta_R_min",       "title":"lj1_delta_R_min",        "bin":100,  "xmin":0,      "xmax":7},

    "lj2_theta_diff_min":{"name":"lj2_theta_diff_min",       "title":"lj2_theta_diff_min",        "bin":100,  "xmin":0,      "xmax":3.5},
    "lj2_phi_diff_min":{"name":"lj2_phi_diff_min",   "title":"lj2_phi_diff_min",        "bin":100,  "xmin":0,      "xmax":7},
    "lj2_delta_R_min":{"name":"lj2_delta_R_min",       "title":"lj2_delta_R_min",        "bin":100,  "xmin":0,      "xmax":7},

    #Combine
    "ll2jj_m_fit":   {"name":"ll2jj_m",           "title":"m_{jj+ll_{3}} [GeV]",                              "bin":27,  "xmin":108,    "xmax":135},
    "ZZ_m_fit":      {"name":"ZZ_m",              "title":"m_{ll_{2}+ll_{3}}",                                "bin":23,  "xmin":112,    "xmax":135},

}

