#This file aims to plot the energy of the photons and the missing energy in order to determine the first cuts to apply on this variables next

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
               #'wzp6_ee_nunuH_HWW_ecm240':{},
               #'wzp6_ee_nunuH_HZa_ecm240':{},
               #'wzp6_ee_nunuH_Haa_ecm240':{},
               #'wzp6_ee_nunuH_Hbb_ecm240':{},
               #'wzp6_ee_nunuH_Hcc_ecm240':{},
               #'wzp6_ee_nunuH_Hgg_ecm240':{},   
               #'wzp6_ee_nunuH_Hmumu_ecm240':{},
               #'wzp6_ee_nunuH_Hss_ecm240':{},
               #'wzp6_ee_nunuH_Htautau_ecm240':{},
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
cutList = {"precuts": 				               "emiss > -10",
    	   "precuts_Za_m":			               "Za_m < 110 && Za_m > 80",
	       "precuts_Za_m_Zb_m":			           "Za_m < 110 && Za_m > 80 && Zb_m < 110 && Zb_m > 80",
           "precuts_Za_m_Zb_m_emiss":              "Za_m < 110 && Za_m > 80 && Zb_m < 110 && Zb_m > 80 && emiss < 8",     
           "precuts_Za_m_Zb_m_emiss_photon_e":     "Za_m < 110 && Za_m > 80 && Zb_m < 110 && Zb_m > 80 && emiss < 8 && photon_e < 20",
           "precuts_Za_m_Zb_m_emiss_photon_e_jj_m":"Za_m < 110 && Za_m > 80 && Zb_m < 110 && Zb_m > 80 && emiss < 8 && photon_e < 20 && jj_m > 10"
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #Photon
    
    "photon_e":       {"name":"photon_e",          "title":"Energy of the photon [GeV]",                       "bin":100,  "xmin":0,      "xmax":50},
    "photon_theta":   {"name":"photon_theta",      "title":"#theta of the photon",               		       "bin":100,  "xmin":0,      "xmax":3.5}, 
    "photon_phi":     {"name":"photon_phi",        "title":"#varphi of the photon",             	      	   "bin":100,  "xmin":-3.5,   "xmax":3.5},
   
    #Dilepton
    
    "ll1a_m":         {"name":"ll1a_m",            "title":"Mass of the 1st Dilepton + Photon [GeV]",          "bin":100,  "xmin":0,      "xmax":200},
    "ll1a_recoil_m":  {"name":"ll1a_recoil_m",     "title":"Recoil mass of the 1st Dilepton + Photon [GeV]",   "bin":100,  "xmin":50,     "xmax":210},
    "ll2a_m":         {"name":"ll2a_m",            "title":"Mass of the 2nd Dilepton + Photon [GeV]",          "bin":100,  "xmin":10,     "xmax":150},
    "ll2a_recoil_m":  {"name":"ll2a_recoil_m",     "title":"Recoil mass of the 2nd Dilepton + Photon [GeV]",   "bin":100,  "xmin":50,     "xmax":210},

    "ll1jj_m":        {"name":"ll1jj_m",           "title":"Mass of the 1st Dilepton + Dijet [GeV]",           "bin":150,  "xmin":10,     "xmax":180},
    "ll2jj_m":        {"name":"ll2jj_m",           "title":"Mass of the 2nd Dilepton + Dijet [GeV]",           "bin":150,  "xmin":10,     "xmax":180},
    
    "ll1miss_m":      {"name":"ll1miss_m",         "title":"Mass of the 1st Dilepton + Missing tlv [GeV]",     "bin":100,  "xmin":0,      "xmax":200},
    "ll2miss_m":      {"name":"ll2miss_m",         "title":"Mass of the 2nd Dilepton + Missing tlv [GeV]",     "bin":100,  "xmin":10,     "xmax":180},

    "ll1_theta_diff": {"name":"ll1_theta_diff",    "title":"Angular Difference (#theta) of the 1st Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll1_phi_diff":   {"name":"ll1_phi_diff",      "title":"Angular Difference (#varphi) of the 1st Dilepton", "bin":100,  "xmin":0,      "xmax":7},
    "ll2_theta_diff": {"name":"ll2_theta_diff",    "title":"Angular Difference (#theta) of the 2nd Dilepton",  "bin":100,  "xmin":0,      "xmax":3.5},
    "ll2_phi_diff":   {"name":"ll2_phi_diff",      "title":"Angular Difference (#varphi) of the 2nd Dilepton", "bin":100,  "xmin":0,      "xmax":7},

    "ll1a_ll1_m":     {"cols":["Za_m", "ll1a_m"],  "title":"1st Dilepton Mass - 1st Dilepton + Photon Mass [GeV]",  "bins": [(40,80,100), (40,80,100)]},
    "ll2a_ll2_m":     {"cols":["Zb_m", "ll2a_m"],  "title":"2nd Dilepton Mass - 2nd Dilepton + Photon Mass [GeV]",  "bins": [(40,80,100), (40,80,100)]},
    
    #Za (1st dilepton) and Zb (2nd dilepton)
    
    "Za_e":           {"name":"Za_e",              "title":"E(Z_{a}) [GeV]",           	         "bin":150,  "xmin":10,     "xmax":180},
    "Za_p":           {"name":"Za_p",              "title":"p(Z_{a]) [GeV]",          			 "bin":100,  "xmin":0,      "xmax":80},
    "Za_px":          {"name":"Za_px",             "title":"p_{x}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_py":          {"name":"Za_py",             "title":"p_{y}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_pz":          {"name":"Za_pz",             "title":"p_{z}(Z_{a}) [GeV]",           		 "bin":100,  "xmin":-70,    "xmax":70},
    "Za_theta":       {"name":"Za_theta",          "title":"#theta(Z_{a})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Za_phi":         {"name":"Za_phi",            "title":"#phi(Z_{a})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Za_m":           {"name":"Za_m",              "title":"m(Z_{a}) [GeV]",            		 "bin":100,  "xmin":0,      "xmax":130},
    "Za_recoil_m":    {"name":"Za_recoil_m",       "title":"m_{recoil}(Z_{a})  [GeV]",           "bin":100,  "xmin":50,     "xmax":210},
    
    "Zb_e":           {"name":"Zb_e",              "title":"E(Z_{b}) [GeV]",           			 "bin":150,  "xmin":10,     "xmax":180},
    "Zb_p":           {"name":"Zb_p",              "title":"p(Z_{b}) [GeV]",           			 "bin":100,  "xmin":0,      "xmax":80},
    "Zb_px":          {"name":"Zb_px",             "title":"p_{x}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-60,    "xmax":60},
    "Zb_py":          {"name":"Zb_py",             "title":"p_{y}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-60,    "xmax":60},
    "Zb_pz":          {"name":"Zb_pz",             "title":"p_{z}(Z_{b}) [GeV]",           		 "bin":100,  "xmin":-60,    "xmax":60},
    "Zb_theta":       {"name":"Zb_theta",          "title":"#theta(Z_{b})",            			 "bin":100,  "xmin":0,      "xmax":3.5},
    "Zb_phi":         {"name":"Zb_phi",            "title":"#phi(Z_{b})",          			     "bin":100,  "xmin":-3.5,   "xmax":3.5},
    "Zb_m":           {"name":"Zb_m",              "title":"m(Z_{b}) [GeV]",            		 "bin":100,  "xmin":0,      "xmax":130},
    "Zb_recoil_m":    {"name":"Zb_recoil_m",       "title":"m_{recoil}(Z_{b}) [GeV]",            "bin":150,  "xmin":50,     "xmax":210},
    
    #Dijet
  
    "jj_e":           {"name":"jj_e",          "title":"E(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":130},
    "jj_p":           {"name":"jj_p",          "title":"p(jj) [GeV]",             			 "bin":100,  "xmin":0,     "xmax":100},
    "jj_px":          {"name":"jj_px",         "title":"p_{x}(jj) [GeV]",              		 "bin":100,  "xmin":-40,   "xmax":40},
    "jj_py":          {"name":"jj_py",         "title":"p_{y}(jj) [GeV]",              		 "bin":100,  "xmin":-40,   "xmax":40},
    "jj_pz":          {"name":"jj_pz",         "title":"p_{z}(jj) [GeV]",              		 "bin":100,  "xmin":-40,   "xmax":40},
    "jj_theta":       {"name":"jj_theta",      "title":"#theta(jj)",               			 "bin":100,  "xmin":0,     "xmax":3.5},
    "jj_phi":         {"name":"jj_phi",        "title":"#phi(jj)",             			     "bin":100,  "xmin":-3.5,  "xmax":3.5},
    "jj_m":           {"name":"jj_m",          "title":"m(jj) [GeV]",              			 "bin":100,  "xmin":0,     "xmax":130},
    
    "diffthetajets_56": {"name":"diffthetajets_56",   "title":"diffthetajets_56",               "bin":100,  "xmin":0,     "xmax":3.5},
    "diffphijets_56":   {"name":"diffphijets_56",     "title":"diffphijets_56",                 "bin":100,  "xmin":0,     "xmax":7},
    
    #Missing Energy
        
    "emiss":          {"name":"emiss",          "title":"Missing Energy [GeV]",                  		 "bin":100,  "xmin":0,     "xmax":130},
    "pxmiss":         {"name":"pxmiss",         "title":"Missing p_{x} [GeV]",               			 "bin":100,  "xmin":-40,   "xmax":40},
    "pymiss":         {"name":"pymiss",         "title":"Missing p_{y} [GeV]",               			 "bin":100,  "xmin":-40,   "xmax":40},
    "pzmiss":         {"name":"pzmiss",         "title":"Missing p_{z} [GeV]",               			 "bin":100,  "xmin":-40,   "xmax":40},

    #Visible Mass

    "visible_m":      {"name":"visible_m",      "title":"Visible Mass [GeV]",                            "bin":200,  "xmin":100,   "xmax":250},
    "missing_m":      {"name":"missing_m",      "title":"Missing Mass [GeV]",                            "bin":100,  "xmin":0,     "xmax":250}
}



    
