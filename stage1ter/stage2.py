#In this stahe we define new variables

#This stage takes as input the output of stage1ter
#stage2 is used ti define new variables if need be. As stage1ter takes a lot of time de execute, we do so in stage2
inputDir    = "../outputs"

#Optional: output directory, default is local dir
outputDir   = "outputs"

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
               #'wzp6_ee_mumuH_Haa_ecm240':{},   #Empty after stage1ter
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               #'wzp6_ee_eeH_Haa_ecm240':{},   #Empty after stage1ter
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               #'wzp6_ee_eeH_Hgg_ecm240':{},   #Empty after stage1ter
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
               'p8_ee_ZZ_ecm240':{},
               'p8_ee_WW_ecm240':{},
               #Useless Background
               #'wzp6_ee_nunuH_HWW_ecm240':{},
               #'wzp6_ee_nunuH_HZa_ecm240':{},
               #'wzp6_ee_nunuH_Haa_ecm240':{},
               #'wzp6_ee_nunuH_Hbb_ecm240':{},
               #'wzp6_ee_nunuH_Hcc_ecm240':{},
               #'wzp6_ee_nunuH_Hgg_ecm240':{},
               #'wzp6_ee_nunuH_Hmumu_ecm240':{},
               #'wzp6_ee_nunuH_Hss_ecm240':{},
               #'wzp6_ee_nunuH_Htautau_ecm240':{},
               }


#Optional: ncpus, default is 4
nCPUS = 128

#Optional running on HTCondor, default is False
#runBatch = False

#USER DEFINED CODE
import ROOT
ROOT.gInterpreter.Declare("""
bool myFilter(ROOT::VecOps::RVec<float> mass) {
    for (size_t i = 0; i < mass.size(); ++i) {
        if (mass.at(i)>80. && mass.at(i)<100.)
            return true;
    }
    return false;
}
""")
#END USER DEFINED CODE

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():    
    #__________________________________________________________________________________________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (
            df
            .Define("Z2miss_m_frac",            "Z2_m/Z2miss_m")
            .Define("Z2miss_m_frac_forced",     "Z2_m/Z2miss_m_forced")
            .Define("Z2jj_m_frac",              "Z2_m/Z2jj_m")
            .Define("ZZ_angle",                 "acos((Z1_px*Z2_px+Z1_py*Z2_py+Z1_pz*Z2_pz)/(sqrt(Z1_p*Z1_p*Z2_p*Z2_p)))")
            )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [

                #Variables already returned by stage1ter
                
                #---------------------------------Photons
                "photon_e",
                "photon_px",
                "photon_py",
                "photon_pz",
                "photon_theta",
                "photon_phi",
                "photon_eta",
                #---------------------------------Missing/Visible
                "emiss",
                "emiss_forced",
                "pxmiss",
                "pymiss",
                "pzmiss",
                "etmiss",
                "missing_theta",
                "visible_m",
                #---------------------------------Dijet
                "jj_e",
                "jj_p",
                "jj_px",
                "jj_py",
                "jj_pz",
                "jj_pt",
                "jj_theta",
                "jj_phi",
                "jj_eta",
                "jj_m",
                #---------------------------------j1
                "j1_e",
                "j1_p",
                "j1_px",
                "j1_py",
                "j1_pz",
                "j1_pt",
                "j1_theta",
                "j1_phi",
                "j1_eta",
                "j1_m",
                #---------------------------------j2
                "j2_e",
                "j2_p",
                "j2_px",
                "j2_py",
                "j2_pz",
                "j2_pt",
                "j2_theta",
                "j2_phi",
                "j2_eta",
                "j2_m",
                #---------------------------------Z1
                "Z1_m",
                "Z1_recoil_m",
                "Z1_theta",
                "Z1_phi",
                "Z1_eta",
                "Z1_e",
                "Z1_p",
                "Z1_px",
                "Z1_py",
                "Z1_pz",
                "Z1a_recoil_m",
                "Z1jj_m",
                #---------------------------------Z2
                "Z2_m",
                "Z2_recoil_m",
                "Z2_theta",
                "Z2_phi",
                "Z2_eta",
                "Z2_e",
                "Z2_p",
                "Z2_px",
                "Z2_py",
                "Z2_pz",
                "Z2a_recoil_m",
                "Z2jj_m",
                "Z2miss_m",
                "Z2miss_m_forced",

                #New variables introduced in stage2

                "Z2miss_m_frac",
                "Z2miss_m_frac_forced",
                "Z2jj_m_frac",
                "ZZ_angle"
                
                ]

        return branchList



