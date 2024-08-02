#In this stahe we define new variables

#takes as input the output of stage1quater

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
               #'wzp6_ee_mumuH_Haa_ecm240':{},   #Empty after stage1quater
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               #'wzp6_ee_eeH_Haa_ecm240':{},   #Empty after stage1quater
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
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

            #Phi for the jets happen to be defined in [0,2pi] instead of [-pi,pi]
            #We substract pi to have the same interval definition as for the rest of the particles
            .Redefine("j1_phi",          "j1_phi - 3.141592653589793")
            .Redefine("j2_phi",          "j2_phi - 3.141592653589793")
            
            .Redefine("on_l1j1_phi_diff",     "abs(on_l1_phi - j1_phi)")
            .Redefine("on_l1j2_phi_diff",     "abs(on_l1_phi - j2_phi)")
            .Redefine("on_l2j1_phi_diff",     "abs(on_l2_phi - j1_phi)")
            .Redefine("on_l2j2_phi_diff",     "abs(on_l2_phi - j2_phi)")
            .Redefine("other_l1j1_phi_diff",     "abs(other_l1_phi - j1_phi)")
            .Redefine("other_l1j2_phi_diff",     "abs(other_l1_phi - j2_phi)")
            .Redefine("other_l2j1_phi_diff",     "abs(other_l2_phi - j1_phi)")
            .Redefine("other_l2j2_phi_diff",     "abs(other_l2_phi - j2_phi)")

            .Redefine("on_l1j1_delta_R",      "sqrt(on_l1j1_phi_diff*on_l1j1_phi_diff + on_l1j1_eta_diff*on_l1j1_eta_diff)")
            .Redefine("on_l1j2_delta_R",      "sqrt(on_l1j2_phi_diff*on_l1j2_phi_diff + on_l1j2_eta_diff*on_l1j2_eta_diff)")
            .Redefine("on_l2j1_delta_R",      "sqrt(on_l2j1_phi_diff*on_l2j1_phi_diff + on_l2j1_eta_diff*on_l2j1_eta_diff)")
            .Redefine("on_l2j2_delta_R",      "sqrt(on_l2j2_phi_diff*on_l2j2_phi_diff + on_l2j2_eta_diff*on_l2j2_eta_diff)")

            .Redefine("other_l1j1_delta_R",      "sqrt(other_l1j1_phi_diff*other_l1j1_phi_diff + other_l1j1_eta_diff*other_l1j1_eta_diff)")
            .Redefine("other_l1j2_delta_R",      "sqrt(other_l1j2_phi_diff*other_l1j2_phi_diff + other_l1j2_eta_diff*other_l1j2_eta_diff)")
            .Redefine("other_l2j1_delta_R",      "sqrt(other_l2j1_phi_diff*other_l2j1_phi_diff + other_l2j1_eta_diff*other_l2j1_eta_diff)")
            .Redefine("other_l2j2_delta_R",      "sqrt(other_l2j2_phi_diff*other_l2j2_phi_diff + other_l2j2_eta_diff*other_l2j2_eta_diff)")


            .Define("jj_recoil_m",       "sqrt((240 - jj_e)*(240 - jj_e) - jj_p*jj_p)")

            #Discriminant used to tistinguish lljjll and jjllll
            .Define("disc",              "abs(125 - jj_recoil_m) - abs(125 - Za_recoil_m)")
            #Discriminant used to distinguish llvvll and vvllll
            .Define("disc2",             "abs(125 - ZZ_m) - abs(125 - ll2miss_m_forced)")

            .Define("ZZ_recoil_max",     "max(Za_recoil_m, Zb_recoil_m)")
            .Define("ZZ_p",              "sqrt((Za_px+Zb_px)*(Za_px+Zb_px)+(Za_py+Zb_py)*(Za_py+Zb_py)+(Za_pz+Zb_pz)*(Za_pz+Zb_pz))")
            .Define("ZZ_recoil_min",     "min(Za_recoil_m, Zb_recoil_m)")
            .Define("ZZ_angle",          "acos((Za_px*Zb_px+Za_py*Zb_py+Za_pz*Zb_pz)/(sqrt(Za_p*Zb_p*Za_p*Zb_p)))")
            .Define("ZZ_angle_general",  "acos((Za_e*Zb_e-Za_px*Zb_px-Za_py*Zb_py-Za_pz*Zb_pz)/(sqrt(Za_m*Zb_m*Za_m*Zb_m)))")

            .Define("lj1_theta_diff_min","min(on_l1j1_theta_diff, on_l1j2_theta_diff)")
            .Redefine("lj1_theta_diff_min","min(lj1_theta_diff_min, on_l2j1_theta_diff)")
            .Redefine("lj1_theta_diff_min","min(lj1_theta_diff_min, on_l2j2_theta_diff)")

            .Define("lj1_phi_diff_min","min(on_l1j1_phi_diff, on_l1j2_phi_diff)")
            .Redefine("lj1_phi_diff_min","min(lj1_phi_diff_min, on_l2j1_phi_diff)")
            .Redefine("lj1_phi_diff_min","min(lj1_phi_diff_min, on_l2j2_phi_diff)")

            .Define("lj1_delta_R_min","min(on_l1j1_delta_R, on_l1j2_delta_R)")
            .Redefine("lj1_delta_R_min","min(lj1_delta_R_min, on_l2j1_delta_R)")
            .Redefine("lj1_delta_R_min","min(lj1_delta_R_min, on_l2j2_delta_R)")

            .Define("lj2_theta_diff_min","min(other_l1j1_theta_diff, other_l1j2_theta_diff)")
            .Redefine("lj2_theta_diff_min","min(lj2_theta_diff_min, other_l2j1_theta_diff)")
            .Redefine("lj2_theta_diff_min","min(lj2_theta_diff_min, other_l2j2_theta_diff)")

            .Define("lj2_phi_diff_min","min(other_l1j1_phi_diff, other_l1j2_phi_diff)")
            .Redefine("lj2_phi_diff_min","min(lj2_phi_diff_min, other_l2j1_phi_diff)")
            .Redefine("lj2_phi_diff_min","min(lj2_phi_diff_min, other_l2j2_phi_diff)")

            .Define("lj2_delta_R_min","min(other_l1j1_delta_R, other_l1j2_delta_R)")
            .Redefine("lj2_delta_R_min","min(lj2_delta_R_min, other_l2j1_delta_R)")
            .Redefine("lj2_delta_R_min","min(lj2_delta_R_min, other_l2j2_delta_R)")

            .Define("Zbmiss_e",   "Zb_e + emiss")
            .Define("Zbmiss_px",  "Zb_px + pxmiss")
            .Define("Zbmiss_py",  "Zb_py + pymiss")
            .Define("Zbmiss_pz",  "Zb_pz + pzmiss")
            .Define("Zbmiss_m",   "sqrt(Zbmiss_e*Zbmiss_e - Zbmiss_px*Zbmiss_px - Zbmiss_py*Zbmiss_py - Zbmiss_pz*Zbmiss_pz)")

            )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
                
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
                "jj_recoil_m",
                #---------------------------------Za
                "Za_m",
                "Za_recoil_m",
                "Za_theta",
                "Za_phi",
                "Za_eta",
                "Za_e",
                "Za_p",
                "Za_px",
                "Za_py",
                "Za_pz",
                "ll1a_recoil_m",
                "ll1jj_m",
                "ll1miss_m",
                #---------------------------------Zb
                "Zb_m",
                "Zb_recoil_m",
                "Zb_theta",
                "Zb_phi",
                "Zb_eta",
                "Zb_e",
                "Zb_p",
                "Zb_px",
                "Zb_py",
                "Zb_pz",
                "ll2a_recoil_m",
                "ll2jj_m",
                "ll2jj_recoil_m",
                "ll2miss_m",
                "ll2miss_m_forced",
                #--------------------------------ZZ
                "ZZ_m",
                "ZZ_recoil_m",
                "ZZ_recoil_max",
                "ZZ_recoil_min",
                "ZZ_angle",
                "ZZ_angle_general",
                "ZZ_p",
                "Zbmiss_m",
                "disc",
                "disc2",
                #--------------------------------Leptons
                "on_l1_theta",
                "on_l1_phi",
                "on_l1_eta",
                "on_l2_theta",
                "on_l2_phi",
                "on_l2_eta",
                "other_l1_theta",
                "other_l1_phi",
                "other_l1_eta",
                "other_l2_theta",
                "other_l2_phi",
                "other_l2_eta",
                "ll1_angle",
                "ll1_theta_diff",
                "ll1_phi_diff",
                "ll1_eta_diff",
                "ll1_delta_R",
                "ll2_angle",
                "ll2_theta_diff",
                "ll2_phi_diff",
                "ll2_eta_diff",
                "ll2_delta_R",
                "on_l1j1_theta_diff",
                "on_l1j1_phi_diff",
                "on_l1j1_eta_diff",
                "on_l1j1_delta_R",
                "on_l1j2_theta_diff",
                "on_l1j2_phi_diff",
                "on_l1j2_eta_diff",
                "on_l1j2_delta_R",
                "on_l2j1_theta_diff",
                "on_l2j1_phi_diff",
                "on_l2j1_eta_diff",
                "on_l2j1_delta_R",
                "on_l2j2_theta_diff",
                "on_l2j2_phi_diff",
                "on_l2j2_eta_diff",
                "on_l2j2_delta_R",
                "other_l1j1_theta_diff",
                "other_l1j1_phi_diff",
                "other_l1j1_eta_diff",
                "other_l1j1_delta_R",
                "other_l1j2_theta_diff",
                "other_l1j2_phi_diff",
                "other_l1j2_eta_diff",
                "other_l1j2_delta_R",
                "other_l2j1_theta_diff",
                "other_l2j1_phi_diff",
                "other_l2j1_eta_diff",
                "other_l2j1_delta_R",
                "other_l2j2_theta_diff",
                "other_l2j2_phi_diff",
                "other_l2j2_eta_diff",
                "other_l2j2_delta_R",
                "lj1_theta_diff_min",
                "lj1_phi_diff_min",
                "lj1_delta_R_min",
                "lj2_theta_diff_min",
                "lj2_phi_diff_min",
                "lj2_delta_R_min"
                ]
          
                

        return branchList



