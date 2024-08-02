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
cutList = {"precuts":	  			 "emiss > -10",
    	   "precuts_Za_m":			 "Za_m < 110 && Za_m > 80",
	       "precuts_Za_m_Zb_m":	   	 "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10",  
           "precuts_Za_m_Zb_m_emiss":"Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8", 

           "llvvll":                 "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && Za_recoil_m > 123 && Za_recoil_m < 127",
            
           #Alternative llvvll discrimination
           #"llvvll":                          "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && disc2 > 0",
           #"llvvll_visible_m":                "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && disc2 > 0 && visible_m < 150",
           #"llvvll_visible_m_Za_recoil_m":    "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && disc2 > 0 && visible_m < 150 && Za_recoil_m > 120 && Za_recoil_m < 130",

           "vvllll":                 "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && (Za_recoil_m < 123 || Za_recoil_m > 127)",
           "vvllll_emiss":           "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && (Za_recoil_m < 123 || Za_recoil_m > 127) && emiss > 45 && emiss < 55",
           "vvllll_emiss_visible_m": "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && (Za_recoil_m < 123 || Za_recoil_m > 127) && emiss > 45 && emiss < 55 && visible_m < 135",
           
           "region2":                "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && (Za_recoil_m < 123 || Za_recoil_m > 127) && emiss > 45 && emiss < 55 && visible_m < 135",
           "fitRegion2":             "Za_m < 110 && Za_m > 80 && Zb_m < 40 && Zb_m > 10 && emiss > 8 && (Za_recoil_m < 123 || Za_recoil_m > 127) && emiss > 45 && emiss < 55 && visible_m < 135 && ZZ_m < 135 && ZZ_m > 115",
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
    
    "ll1a_recoil_m":  {"name":"ll1a_recoil_m",     "title":"Recoil Mass of the 1st Dilepton + Photon [GeV]",   "bin":100,  "xmin":20,     "xmax":250},
    "ll2a_recoil_m":  {"name":"ll2a_recoil_m",     "title":"Recoil Mass of the 2nd Dilepton + Photon [GeV]",   "bin":100,  "xmin":100,    "xmax":250},

    "ll1jj_m":        {"name":"ll1jj_m",           "title":"Mass of the 1st Dilepton + Dijet [GeV]",           "bin":100,  "xmin":20,     "xmax":240},
    "ll2jj_m":        {"name":"ll2jj_m",           "title":"Mass of the 2nd Dilepton + Dijet [GeV]",           "bin":100,  "xmin":0,      "xmax":240},
    
    "ll1miss_m":      {"name":"ll1miss_m",         "title":"Mass of the 1st Dilepton + Missing tlv [GeV]",     "bin":100,  "xmin":0,     "xmax":200},
    "ll2miss_m":      {"name":"ll2miss_m",         "title":"Mass of the 2nd Dilepton + Missing tlv [GeV]",     "bin":100,  "xmin":0,     "xmax":150},
    "ll2miss_m_forced": {"name":"ll2miss_m_forced","title":"m_{vv+ll_{3}} [GeV]",                    "bin":50,  "xmin":100,   "xmax":150},

    "ZZ_m":           {"name":"ZZ_m",              "title":"m(Z_{a}+Z_{3})",                                   "bin":200,  "xmin":80,     "xmax":200},
    "ZZ_m_zoom":      {"name":"ZZ_m",              "title":"m_{ll_{2}+ll_{3}}",                                "bin":40,   "xmin":100,    "xmax":140},
    "ZZ_m_fit":       {"name":"ZZ_m",              "title":"m_{ll_{2}+ll_{3}}",                                "bin":20,   "xmin":115,    "xmax":135},
    "ZZ_recoil_m":    {"name":"ZZ_recoil_m",       "title":"m_{recoil}(Z_{a}+Z_{3})",                          "bin":200,  "xmin":20,     "xmax":140},
    "ZZ_recoil_max":  {"name":"ZZ_recoil_max",     "title":"max_recoil",                                       "bin":100,  "xmin":150,    "xmax":240},
    "ZZ_recoil_min":  {"name":"ZZ_recoil_min",     "title":"min_recoil",                                       "bin":100,  "xmin":20,     "xmax":210},
    "ZZ_angle":       {"name":"ZZ_angle",          "title":"ZZ_angle",                                         "bin":100,  "xmin":-1,     "xmax":3.5},
    "ZZ_angle_general":       {"name":"ZZ_angle_general",          "title":"ZZ_angle_general",                 "bin":100,  "xmin":-1,     "xmax":3.5},

    #Za (1st dilepton) and Zb (2nd dilepton)
    
    "Za_e":           {"name":"Za_e",              "title":"E(Z_{a}) [GeV]",           	         "bin":150,  "xmin":0,      "xmax":160},
    "Za_p":           {"name":"Za_p",              "title":"p(Z_{a}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":180},
    "Za_px":          {"name":"Za_px",             "title":"p_{x}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_py":          {"name":"Za_py",             "title":"p_{y}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_pz":          {"name":"Za_pz",             "title":"p_{z}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_theta":       {"name":"Za_theta",          "title":"#theta(Z_{a})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Za_phi":         {"name":"Za_phi",            "title":"#phi(Z_{a})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Za_m":           {"name":"Za_m",              "title":"m(Z_{a}) [GeV]",           			 "bin":150,  "xmin":10,     "xmax":140},
    "Za_recoil_m":    {"name":"Za_recoil_m",       "title":"m_{recoil}(Z_{a})",                  "bin":100,  "xmin":20,     "xmax":210},
    "Za_eta":         {"name":"Za_eta",            "title":"#eta(Z_{a})",                        "bin":100,  "xmin":-10,    "xmax":10},
    
    "Zb_e":           {"name":"Zb_e",              "title":"E(Z_{b}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":200},
    "Zb_p":           {"name":"Zb_p",              "title":"p(Z_{b}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":180},
    "Zb_px":          {"name":"Zb_px",             "title":"p_{x}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-100,   "xmax":100},
    "Zb_py":          {"name":"Zb_py",             "title":"p_{y}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-100,   "xmax":100},
    "Zb_pz":          {"name":"Zb_pz",             "title":"p_{z}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-100,   "xmax":100},
    "Zb_theta":       {"name":"Zb_theta",          "title":"#theta(Z_{b})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Zb_phi":         {"name":"Zb_phi",            "title":"#phi(Z_{b})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Zb_m":           {"name":"Zb_m",              "title":"m(Z_{b}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":180},
    "Zb_recoil_m":    {"name":"Zb_recoil_m",       "title":"m_{recoil}(Z_{b}) [GeV]",            "bin":100,  "xmin":20,     "xmax":250},
    "Zb_eta":         {"name":"Zb_eta",            "title":"#eta(Z_{b})",                        "bin":100,  "xmin":-10,    "xmax":10},
     
    #Dijet
  
    "jj_e":           {"name":"jj_e",          "title":"E(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":200},
    "jj_p":           {"name":"jj_p",          "title":"p(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":200},
    "jj_px":          {"name":"jj_px",         "title":"p_{x}(jj) [GeV]",              		 "bin":100,  "xmin":-80,   "xmax":80},
    "jj_py":          {"name":"jj_py",         "title":"p_{y}(jj) [GeV]",              		 "bin":100,  "xmin":-80,   "xmax":80},
    "jj_pz":          {"name":"jj_pz",         "title":"p_{z}(jj) [GeV]",              		 "bin":100,  "xmin":-80,   "xmax":80},
    "jj_theta":       {"name":"jj_theta",      "title":"#theta(jj)",               			 "bin":100,  "xmin":0,     "xmax":3.5},
    "jj_phi":         {"name":"jj_phi",        "title":"#phi(jj)",             			     "bin":100,  "xmin":-3.5,  "xmax":3.5},
    "jj_m":           {"name":"jj_m",          "title":"m(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":200},
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
        
    "emiss":          {"name":"emiss",          "title":"Missing energy [GeV]",                  		 "bin":100,  "xmin":0,     "xmax":150},
    "etmiss":         {"name":"etmiss",         "title":"Missing transverse energy [GeV]",               "bin":100,  "xmin":0,     "xmax":150},
    "pxmiss":         {"name":"pxmiss",         "title":"Missing p_{x} [GeV]",               			 "bin":100,  "xmin":-80,   "xmax":80},
    "pymiss":         {"name":"pymiss",         "title":"Missing p_{y} [GeV]",               			 "bin":100,  "xmin":-80,   "xmax":80},
    "pzmiss":         {"name":"pzmiss",         "title":"Missing p_{z} [GeV]",               			 "bin":100,  "xmin":-80,   "xmax":80},

    "visible_m":      {"name":"visible_m",      "title":"m_{vis} [GeV]",                                 "bin":200,  "xmin":0,    "xmax":250},
    "missing_theta":  {"name":"missing_theta",  "title":"Missing #theta [GeV]",                          "bin":100,  "xmin":0,    "xmax":3.5},

    "Za_recoil_m_zoom":    {"name":"Za_recoil_m",       "title":"m^{rec}_{ll_{a}} [GeV]",            "bin":150,  "xmin":100,     "xmax":160},
    "Zb_recoil_m_zoom":    {"name":"Zb_recoil_m",       "title":"m^{rec}_{ll_{3}} [GeV]",            "bin":150,  "xmin":150,     "xmax":250},
    
    #Angular difference

    "ll2_phi_diff":        {"name":"ll2_phi_diff",       "title":"#Delta#varphi_{ll_{3}}",            "bin":100,  "xmin":0,     "xmax":7},
    "ll2_theta_diff":        {"name":"ll2_theta_diff",       "title":"#Delta#theta_{ll_{3}}",            "bin":100,  "xmin":0,     "xmax":3.5},
    "ll2_delta_R":        {"name":"ll2_delta_R",       "title":"#DeltaR_{ll_{3}}",            "bin":100,  "xmin":0,     "xmax":7},

    "ll1_phi_diff":        {"name":"ll1_phi_diff",       "title":"#Delta#varphi_{ll_{1}}",            "bin":100,  "xmin":0,     "xmax":7},
    "ll1_theta_diff":        {"name":"ll1_theta_diff",       "title":"#Delta#theta_{ll_{1}}",            "bin":100,  "xmin":0,     "xmax":3.5},
    "ll1_delta_R":        {"name":"ll1_delta_R",       "title":"#DeltaR_{ll_{1}}",            "bin":100,  "xmin":0,     "xmax":7},

}

