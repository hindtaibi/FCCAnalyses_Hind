#Here, we are looking at the events where the second Z leptonic is on shell

inputDir    = "../stage1ter/outputs"

#Optional: output directory, default is local dir
outputDir   = "outputs"

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},       #Signal
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_nunuH_HZZ_ecm240':{},
               'wzp6_ee_nunuH_HWW_ecm240':{},
               'wzp6_ee_nunuH_HZa_ecm240':{},
               'wzp6_ee_nunuH_Haa_ecm240':{},
               'wzp6_ee_nunuH_Hbb_ecm240':{},
               'wzp6_ee_nunuH_Hcc_ecm240':{},
               'wzp6_ee_nunuH_Hgg_ecm240':{},   
               'wzp6_ee_nunuH_Hmumu_ecm240':{},
               'wzp6_ee_nunuH_Hss_ecm240':{},
               'wzp6_ee_nunuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HZZ_ecm240':{},         #Signal
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{}, 
               #'p8_ee_ZZ_ecm240':{},
               #'p8_ee_WW_ecm240':{}
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

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (df 
               
               #Filter to have two leptonic Z bosons               
               .Filter("N_other_Z_leptons == 2 && N_on_Z_leptons ==2")

               .Define("other_ll_tlv",      "other_Z_leptons_tlv[0] + other_Z_leptons_tlv[1]")
               .Define("other_ll_inv_m",    "other_ll_tlv.M()")
               .Filter("other_ll_inv_m < 80 && other_ll_inv_m > 20")

               #On shell dilepton

               .Define("on_ll_tlv",         "on_Z_leptons_tlv[0] + on_Z_leptons_tlv[1]")
               .Define("on_ll_e",           "on_ll_tlv.E()")
               .Define("on_ll_p",           "on_ll_tlv.P()")
               .Define("on_ll_px",          "on_ll_tlv.Px()")
               .Define("on_ll_py",          "on_ll_tlv.Py()")
               .Define("on_ll_pz",          "on_ll_tlv.Pz()")
               .Define("on_ll_theta_diff",  "abs(on_Z_leptons_theta[0] - on_Z_leptons_theta[1])")
               .Define("on_ll_phi_diff",    "abs(on_Z_leptons_phi[0] - on_Z_leptons_phi[1])")
               .Define("on_ll_inv_m",       "on_ll_tlv.M()")
               
               #Other dilepton
               
               .Define("other_ll_e",           "other_ll_tlv.E()")
               .Define("other_ll_p",           "other_ll_tlv.P()")
               .Define("other_ll_px",          "other_ll_tlv.Px()")
               .Define("other_ll_py",          "other_ll_tlv.Py()")
               .Define("other_ll_pz",          "other_ll_tlv.Pz()")
               .Define("other_ll_theta_diff",  "abs(other_Z_leptons_theta[0] - other_Z_leptons_theta[1])")
               .Define("other_ll_phi_diff",    "abs(other_Z_leptons_phi[0] - other_Z_leptons_phi[1])")

               #We take the photon with highest energy, which is the 1st photon

               .Define("photon_tlv",        "photons_tlv[0]")
               .Define("photon_e",          "photon_tlv.E()")
               .Define("photon_p",          "photons_p[0]")
               .Define("photon_px",         "photons_px[0]")
               .Define("photon_py",         "photons_py[0]")
               .Define("photon_pz",         "photons_pz[0]")
               .Define("photon_theta",      "photons_theta[0]")
               .Define("photon_phi",        "photons_phi[0]")
               .Define("photon_inv_m",      "photon_tlv.M()")
               .Define("photon_recoil_m",   "photons_recoil_m[0]")
               
               #On shell dilepton + photon

               .Define("on_lla_tlv",        "on_ll_tlv + photon_tlv")
               .Define("on_lla_inv_m",      "on_lla_tlv.M()")
               
               #Other dilepton + photon

               .Define("other_lla_tlv",     "other_ll_tlv + photon_tlv")
               .Define("other_lla_inv_m",   "other_lla_tlv.M()")
               
               #Za (the on shell Z) decays into 2 leptons

               .Define("Za_tlv",            "on_Z_leptonic_tlv[0]")
               .Define("Za_e",              "Za_tlv.E()")
               .Define("Za_p",              "Za_tlv.P()")
               .Define("Za_px",             "on_Z_leptonic_px[0]")
               .Define("Za_py",             "on_Z_leptonic_py[0]")
               .Define("Za_pz",             "on_Z_leptonic_pz[0]")
               .Define("Za_theta",          "on_Z_leptonic_theta[0]")
               .Define("Za_phi",            "on_Z_leptonic_phi[0]")
               .Define("Za_m",              "on_Z_leptonic_m[0]")   #On shell dilepton mass
               .Define("Za_recoil_m",       "on_Z_leptonic_recoil_m[0]")
               
               #Zb (the other leptonic Z) decays into 2 leptons and is considered on shell here

               .Define("Zb_tlv",            "other_Z_leptonic_tlv[0]")
               .Define("Zb_e",              "Zb_tlv.E()")
               .Define("Zb_p",              "Zb_tlv.P()")
               .Define("Zb_px",             "other_Z_leptonic_px[0]")
               .Define("Zb_py",             "other_Z_leptonic_py[0]")
               .Define("Zb_pz",             "other_Z_leptonic_pz[0]")
               .Define("Zb_theta",          "other_Z_leptonic_theta[0]")
               .Define("Zb_phi",            "other_Z_leptonic_phi[0]")
               .Define("Zb_m",              "other_Z_leptonic_m[0]")   #Other dilepton mass
               .Define("Zb_recoil_m",       "other_Z_leptonic_recoil_m[0]")
               
               #Dijet

               .Define("jj",             "ReconstructedParticle::jetsum(jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("jj_e",           "jj.E()")
               .Define("jj_p",           "jj.P()")
               .Define("jj_px",          "jj.Px()")
               .Define("jj_py",          "jj.Py()")
               .Define("jj_pz",          "jj.Pz()")
               .Define("jj_pt",          "jj.Pt()")
               .Define("jj_theta",       "jj.Theta()")
               .Define("jj_phi",         "jj.Phi()")
               .Define("jj_m",           "jj.M()")
               
               #Information about each jet (Durham N = 2)
               
               .Define("j3_e",              "jets_e2[0]")
               .Define("j3_p",              "jets_p2[0]")              
               .Define("j3_px",             "jets_px2[0]")
               .Define("j3_py",             "jets_py2[0]")
               .Define("j3_pz",             "jets_pz2[0]")
               .Define("j3_pt",             "jets_pt2[0]")
               .Define("j3_theta",          "jets_theta2[0]")
               .Define("j3_phi",            "jets_phi2[0]")
               #.Define("j3_m",              "jets_m2[0]")
               
               .Define("j4_e",              "jets_e2[1]")
               .Define("j4_p",              "jets_p2[1]")                                           
               .Define("j4_px",             "jets_px2[1]")           
               .Define("j4_py",             "jets_py2[1]")               
               .Define("j4_pz",             "jets_pz2[1]")
               .Define("j4_pt",             "jets_pt2[1]")                
               .Define("j4_theta",          "jets_theta2[1]")          
               .Define("j4_phi",            "jets_phi2[1]")
               #.Define("j4_m",              "jets_m2[1]")
               
               .Define("diffthetajets_34",  "abs(j3_theta - j4_theta)")
               .Define("diffphijets_34",    "abs(j3_phi - j4_phi)")

               .Define("missing_theta",     "missing_tlv[0].Theta()")

               .Define("angle_miss_jet",    "ReconstructedParticle::get_angle(missing_tlv[0], jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("angle_miss_j3",     "angle_miss_jet[0]")
               .Define("angle_miss_j4",     "angle_miss_jet[1]")
       
               )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list.
    def output():
        branchList = [

            #---------------------------------------------------------------------------------------------Photon
          
            "photon_e",
            "photon_p",
            "photon_px",
            "photon_py",
            "photon_pz",
            "photon_theta",
            "photon_phi",
            "photon_inv_m",
            "photon_recoil_m",
            "photon_tlv",

            #----------------------------------------------------------------------------------On shell dilepton

            "on_ll_e",
            "on_ll_p",
            "on_ll_px",
            "on_ll_py",
            "on_ll_pz",
            "on_ll_theta_diff",
            "on_ll_phi_diff",
            "on_ll_inv_m",
            "on_ll_tlv",
            
            #--------------------------------------------------------------------------------------Other dilepton

            "other_ll_e",
            "other_ll_p",
            "other_ll_px",
            "other_ll_py",
            "other_ll_pz",
            "other_ll_theta_diff",
            "other_ll_phi_diff",
            "other_ll_inv_m",
            "other_ll_tlv",

            #---------------------------------------------------------------------------------------------on lla

            "on_lla_inv_m",  
            "on_lla_tlv",
            
            #------------------------------------------------------------------------------------------other lla

            "other_lla_inv_m",  
            "other_lla_tlv",

            #-----------------------------------------------------------------------------------------On shell Z

            "Za_e",
            "Za_p",
            "Za_px",
            "Za_py",
            "Za_pz",
            "Za_theta",
            "Za_phi",
            "Za_m",
            "Za_recoil_m",
            "Za_tlv",
            
            #-------------------------------------------------------------------------------------------Other Z

            "Zb_e",
            "Zb_p",
            "Zb_px",
            "Zb_py",
            "Zb_pz",
            "Zb_theta",
            "Zb_phi",
            "Zb_m",
            "Zb_recoil_m",
            "Zb_tlv",
            
            #---------------------------------------------------------------------------------------------Jets

            "jj_e",
            "jj_p",
            "jj_px",
            "jj_py",
            "jj_pz",
            "jj_pt",
            "jj_theta",
            "jj_phi",
            "jj_m",
            
            "j3_e",
            "j3_p",
            "j3_px",
            "j3_py",
            "j3_pz",
            "j3_pt",
            "j3_theta",
            "j3_phi",
            "j3_m",
            "angle_miss_j3",     #The missing theta
            
            "j4_e",
            "j4_p",
            "j4_px",
            "j4_py",
            "j4_pz",
            "j4_pt",
            "j4_theta",
            "j4_phi",
            "j4_m",
            "angle_miss_j4",     #The missing theta
            
            "diffthetajets_34",
            "diffphijets_34",
            
            #----------------------------------------------------------------------------Missing/Visible stuff

            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss"       
          
        ]        

        return branchList

