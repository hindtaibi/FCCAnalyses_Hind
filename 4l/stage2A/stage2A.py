#Here, we are looking at the events where the second Z leptonic is on shell

inputDir    = "../stage1bis/outputs"

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
               #Background
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_nunuH_HWW_ecm240':{},
               'wzp6_ee_nunuH_HZa_ecm240':{},
               'wzp6_ee_nunuH_Haa_ecm240':{},
               'wzp6_ee_nunuH_Hbb_ecm240':{},
               'wzp6_ee_nunuH_Hcc_ecm240':{},
               'wzp6_ee_nunuH_Hgg_ecm240':{},   
               'wzp6_ee_nunuH_Hmumu_ecm240':{},
               'wzp6_ee_nunuH_Hss_ecm240':{},
               'wzp6_ee_nunuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
               'p8_ee_ZZ_ecm240':{},
               'p8_ee_WW_ecm240':{}
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
               
               #Filter to have two leptonic on shell Z bosons               
               .Filter("N_other_Z_leptonic == 0 && N_on_Z_leptonic == 2")

               .Define("Za_tlv",            "on_Z_leptonic_tlv[0]")
               .Define("Za_m",              "Za_tlv.M()")
               .Define("Zb_tlv",            "on_Z_leptonic_tlv[1]")
               .Define("Zb_m",              "Zb_tlv.M()")

               #We filter to have the invariant masses that correspond to on shell Z
               ##.Filter("Za_m < 110 && Za_m > 80 && Zb_m < 110 && Zb_m > 80")   #I don't filter the mass after all, not yet

               #Dileptons
		
	           #Dileptons tlv
               .Define("ll1_tlv",           "on_Z_leptons_tlv[0] + on_Z_leptons_tlv[1]")
               .Define("ll2_tlv",           "on_Z_leptons_tlv[2] + on_Z_leptons_tlv[3]")
		
	           #Dileptons angular difference	
               .Define("ll1_theta_diff",    "abs(on_Z_leptons_tlv[0].Theta() - on_Z_leptons_tlv[1].Theta())")
               .Define("ll1_phi_diff",      "abs(on_Z_leptons_tlv[0].Phi() - on_Z_leptons_tlv[1].Phi())")
               
               .Define("ll2_theta_diff",    "abs(on_Z_leptons_tlv[2].Theta() - on_Z_leptons_tlv[3].Theta())")
               .Define("ll2_phi_diff",      "abs(on_Z_leptons_tlv[2].Phi() - on_Z_leptons_tlv[3].Phi())")
               
               #Dileptons recoil mass
               .Define("ll1_recoil_m",      "sqrt((240-ll1_tlv.E())*(240-ll1_tlv.E())-(ll1_tlv.P())*(ll1_tlv.P()))")
               .Define("ll2_recoil_m",      "sqrt((240-ll2_tlv.E())*(240-ll2_tlv.E())-(ll2_tlv.P())*(ll2_tlv.P()))")

               #We take the photon with highest energy, which is the 1st photon

               .Define("photon_tlv",        "photons_tlv[0]")
               .Define("photon_e",          "photon_tlv.E()")
               .Define("photon_p",          "photon_tlv.P()")
               .Define("photon_px",         "photon_tlv.Px()")
               .Define("photon_py",         "photon_tlv.Py()")
               .Define("photon_pz",         "photon_tlv.Pz()")
               .Define("photon_theta",      "photon_tlv.Theta()")
               .Define("photon_phi",        "photon_tlv.Phi()")
               .Define("photon_m",          "photon_tlv.M()")
                                             
               #1st dilepton + photon

               .Define("ll1a_tlv",          "ll1_tlv + photon_tlv")
               .Define("ll1a_m",            "ll1a_tlv.M()")
               .Define("ll1a_recoil_m",     "sqrt((240-ll1a_tlv.E())*(240-ll1a_tlv.E())-(ll1a_tlv.P())*(ll1a_tlv.P()))")
               
               #2nd dilepton + photon

               .Define("ll2a_tlv",          "ll2_tlv + photon_tlv")
               .Define("ll2a_m",            "ll2a_tlv.M()")
               .Define("ll2a_recoil_m",     "sqrt((240-ll2a_tlv.E())*(240-ll2a_tlv.E())-(ll2a_tlv.P())*(ll2a_tlv.P()))")
               
               #1st dilepton + missing tlv
               
               .Define("ll1miss_tlv",       "ll1_tlv + missing_tlv[0]")
               .Define("ll1miss_m",         "ll1miss_tlv.M()")
               
               #2nd dilepton + missing tlv
               
               .Define("ll2miss_tlv",       "ll2_tlv + missing_tlv[0]")
               .Define("ll2miss_m",         "ll2miss_tlv.M()")
               
               #Za (the on shell Z) decays into 2 leptons

               .Define("Za_e",              "Za_tlv.E()")
               .Define("Za_p",              "Za_tlv.P()")
               .Define("Za_px",             "Za_tlv.Px()")
               .Define("Za_py",             "Za_tlv.Py()")
               .Define("Za_pz",             "Za_tlv.Pz()")
               .Define("Za_theta",          "Za_tlv.Theta()")
               .Define("Za_phi",            "Za_tlv.Phi()")
               .Define("Za_recoil_m",       "sqrt((240-Za_e)*(240-Za_e)-(Za_p)*(Za_p))")
               
               #Zb (the other leptonic Z) decays into 2 leptons and is considered on shell here
               
               .Define("Zb_e",              "Zb_tlv.E()")
               .Define("Zb_p",              "Zb_tlv.P()")
               .Define("Zb_px",             "Zb_tlv.Px()")
               .Define("Zb_py",             "Zb_tlv.Py()")
               .Define("Zb_pz",             "Zb_tlv.Pz()")
               .Define("Zb_theta",          "Zb_tlv.Theta()")
               .Define("Zb_phi",            "Zb_tlv.Phi()")
               .Define("Zb_recoil_m",       "sqrt((240-Zb_e)*(240-Zb_e)-(Zb_p)*(Zb_p))")
               
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

               #1st dilepton + dijet

               .Define("ll1jj_tlv",         "ll1_tlv + jj")
               .Define("ll1jj_m",           "ll1jj_tlv.M()")
               
               #2nd dilepton + photon

               .Define("ll2jj_tlv",         "ll2_tlv + jj")
               .Define("ll2jj_m",           "ll2jj_tlv.M()")
               
               #Information about each jet (Durham N = 2)
               
               .Define("j5_e",              "jets_e2[0]")
               .Define("j5_p",              "jets_p2[0]")              
               .Define("j5_px",             "jets_px2[0]")
               .Define("j5_py",             "jets_py2[0]")
               .Define("j5_pz",             "jets_pz2[0]")
               .Define("j5_pt",             "jets_pt2[0]")
               .Define("j5_theta",          "jets_theta2[0]")
               .Define("j5_phi",            "jets_phi2[0]")
               .Define("j5_m",              "jets_m2[0]")
               
               .Define("j6_e",              "jets_e2[1]")
               .Define("j6_p",              "jets_p2[1]")                                           
               .Define("j6_px",             "jets_px2[1]")           
               .Define("j6_py",             "jets_py2[1]")               
               .Define("j6_pz",             "jets_pz2[1]")
               .Define("j6_pt",             "jets_pt2[1]")                
               .Define("j6_theta",          "jets_theta2[1]")          
               .Define("j6_phi",            "jets_phi2[1]")
               .Define("j6_m",              "jets_m2[1]")
               
               .Define("diffthetajets_56",  "abs(j5_theta - j6_theta)")
               .Define("diffphijets_56",    "abs(j5_phi - j6_phi)")

               .Define("missing_theta",     "missing_tlv[0].Theta()")

               .Define("angle_miss_jet",    "ReconstructedParticle::get_angle(missing_tlv[0], jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("angle_miss_j5",     "angle_miss_jet[0]")
               .Define("angle_miss_j6",     "angle_miss_jet[1]")

               #Visible/Missing mass

               .Define("visible_m",         "visible_4vector.M()")
               .Define("missing_m",         "sqrt(emiss*emiss-pxmiss*pxmiss-pymiss*pymiss-pzmiss*pzmiss)")

                     
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
            "photon_m",
            "photon_tlv",

            #----------------------------------------------------------------------------------Dileptons

            "ll1_theta_diff",
            "ll1_phi_diff",
            "ll1_tlv",
          
            "ll2_theta_diff",
            "ll2_phi_diff",
            "ll2_tlv",
            
            "ll1_recoil_m",
            "ll2_recoil_m",

            "ll1a_m",
            "ll1a_recoil_m",
            "ll1a_tlv",
            "ll2a_m",
            "ll2a_recoil_m",
            "ll2a_tlv",

            "ll1jj_m",
            "ll1jj_tlv",
            "ll2jj_m",
            "ll2jj_tlv",
            
            "ll1miss_m",
            "ll1miss_tlv",
            "ll2miss_m",
            "ll2miss_tlv",

            #-------------------------------------------------------------------------------------Extra leptons

            "N_on_extra_leptons",
            "N_other_extra_leptons",
            
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
            
            "j5_e",
            "j5_p",
            "j5_px",
            "j5_py",
            "j5_pz",
            "j5_pt",
            "j5_theta",
            "j5_phi",
            "j5_m",
            "angle_miss_j5",     #The missing theta
            
            "j6_e",
            "j6_p",
            "j6_px",
            "j6_py",
            "j6_pz",
            "j6_pt",
            "j6_theta",
            "j6_phi",
            "j6_m",
            "angle_miss_j6",     #The missing theta
            
            "diffthetajets_56",
            "diffphijets_56",
            
            #----------------------------------------------------------------------------Missing/Visible stuff

            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss",

            "visible_m",
            "missing_m"
          
        ]        

        return branchList
