inputDir    = "../stage1ter/outputs"



#Optional: output directory, default is local dir
outputDir   = "outputs"

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},       #Signal
               #'wzp6_ee_mumuH_HWW_ecm240':{},
               #'wzp6_ee_mumuH_HZa_ecm240':{},
               #'wzp6_ee_mumuH_Haa_ecm240':{},
               #'wzp6_ee_mumuH_Hbb_ecm240':{},
               #'wzp6_ee_mumuH_Hcc_ecm240':{},
               #'wzp6_ee_mumuH_Hgg_ecm240':{},
               #'wzp6_ee_mumuH_Hmumu_ecm240':{},
               #'wzp6_ee_mumuH_Hss_ecm240':{},
               #'wzp6_ee_mumuH_Htautau_ecm240':{},
               #'wzp6_ee_nunuH_HZZ_ecm240':{},
               #'wzp6_ee_nunuH_HWW_ecm240':{},
               #'wzp6_ee_nunuH_HZa_ecm240':{},
               #'wzp6_ee_nunuH_Haa_ecm240':{},
               #'wzp6_ee_nunuH_Hbb_ecm240':{},
               #'wzp6_ee_nunuH_Hcc_ecm240':{},
               #'wzp6_ee_nunuH_Hgg_ecm240':{},   
               #'wzp6_ee_nunuH_Hmumu_ecm240':{},
               #'wzp6_ee_nunuH_Hss_ecm240':{},
               #'wzp6_ee_nunuH_Htautau_ecm240':{},
               #'wzp6_ee_eeH_HZZ_ecm240':{},         #Signal
               #'wzp6_ee_eeH_HWW_ecm240':{},
               #'wzp6_ee_eeH_HZa_ecm240':{},
               #'wzp6_ee_eeH_Haa_ecm240':{},
               #'wzp6_ee_eeH_Hbb_ecm240':{},
               #'wzp6_ee_eeH_Hcc_ecm240':{},
               #'wzp6_ee_eeH_Hgg_ecm240':{},
               #'wzp6_ee_eeH_Hmumu_ecm240':{},
               #'wzp6_ee_eeH_Hss_ecm240':{},
               #'wzp6_ee_eeH_Htautau_ecm240':{}
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
        
               #---------------------------------------------------------------------------------------------------------------------Real data part
               #To keep the signal only (hzz)
               #.Filter("hzz_decay.Z_decay.size()>0")
               
               #We save the absolute value of the Z's pdg
               #Remark: pdg_Z saves 2 variables thus we need to choose one before applying the filter
               
               #Decay of the 1st Z into 2 leptons (2 electrons (11) or 2 muons (13))
               #.Define("abs_pdg_Z", "abs(MCParticle::get_pdg(hzz_decay.Z_decay)[0])")
               #.Filter("abs_pdg_Z == 11 || abs_pdg_Z == 13") 
                
               #Decay of the 2nd Z (on-shell) into 2 leptons (2 electrons (11) or 2 muons (13))
               #.Define("abs_pdg_Z1", "abs(MCParticle::get_pdg(hzz_decay.Z1_decay)[0])")
               #.Filter("abs_pdg_Z1 == 11 || abs_pdg_Z1 == 13")

               #Decay of the 3rd Z (off-shell) into 2 jets (dd (1), uu (2), ss (3), cc (4), bb (5)) 
               #.Define("abs_pdg_Z2", "abs(MCParticle::get_pdg(hzz_decay.Z2_decay)[0])")
               #.Filter("abs_pdg_Z2 == 1 || abs_pdg_Z2 == 2 || abs_pdg_Z2 == 3 || abs_pdg_Z2 == 4 || abs_pdg_Z2 == 5")
               #-----------------------------------------------------------------------------------------------------------------------------------
               
               #Filter to have two leptonic Z bosons               
               .Filter("N_other_Z_leptons == 2 && N_on_Z_leptons ==2")                    
            
               #Z1 (the on shell Z) decays into 2 leptons
               .Define("Za_inv_m",          "sqrt(on_Z_leptonic_tlv.E()*on_Z_leptonic_tlv.E()-on_Z_leptonic_tlv.P()*on_Z_leptonic_tlv.P())[0]")     #Invariant mass of the on shell Z
               .Define("Za_e",              "on_Z_leptonic.E()[0]")
               .Define("Za_energy",         "on_Z_leptonic.Energy()[0]")
               .Define("Za_m",              "on_Z_leptonic.M()[0]")
               .Define("Za_mag",            "on_Z_leptonic.Mag()[0]")
               .Define("Za_P",              "on_Z_leptonic.P()[0]")
               .Define("Za_recoil_m",       "on_Z_leptonic_recoil_m[0]")

               .Define("ll_tlv",            "on_Z_leptons_tlv[0] + on_Z_leptons_tlv[1]")
               .Define("ll_m",              "ll_tlv.M()")
               
               #Durham N = 2
               .Define("j5_p",              "jets_p2[0]")
               .Define("j5_pt",             "jets_pt2[0]")
               .Define("j5_e",              "jets_e2[0]")
               .Define("j5_px",             "jets_px2[0]")
               .Define("j5_py",             "jets_py2[0]")
               .Define("j5_pz",             "jets_pz2[0]")
               .Define("j5_theta",          "jets_theta2[0]")
               .Define("j5_phi",            "jets_phi2[0]")
               
               .Define("j6_p",              "jets_p2[1]")               
               .Define("j6_pt",             "jets_pt2[1]")              
               .Define("j6_e",              "jets_e2[1]")               
               .Define("j6_px",             "jets_px2[1]")           
               .Define("j6_py",             "jets_py2[1]")               
               .Define("j6_pz",             "jets_pz2[1]")               
               .Define("j6_theta",          "jets_theta2[1]")          
               .Define("j6_phi",            "jets_phi2[1]")
               
               .Define("diffthetajets_56",  "abs(j5_theta - j6_theta)")
               .Define("diffphijets_56",    "abs(j5_phi - j6_phi)")

               .Define("missing_theta",     "missing_tlv[0].Theta()")

               .Define("angle_miss_jet",    "ReconstructedParticle::get_angle(missing_tlv[0], jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("angle_miss_j5",     "angle_miss_jet[0]")
               .Define("angle_miss_j6",     "angle_miss_jet[1]")
       
               )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list.
    def output():
        branchList = [

            #-------------------------------------------------------------------------------------------Photons

            
            #----------------------------------------------------------------------------------------------Jets
            
            "j5_p",
            "j5_pt",
            "j5_e",
            "j5_px",
            "j5_py",
            "j5_pz",
            "j5_theta", 
            "j5_phi",

            "j6_p",
            "j6_pt",
            "j6_e",
            "j6_px",
            "j6_py",
            "j6_pz",
            "j6_theta", 
            "j6_phi",
            
            "diffthetajets_56",
            "diffphijets_56",
            
            #----------------------------------------------------------------------------Missing/Visible stuff

            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss",
            
            "visible_mass_predef"           
          
        ]        

        return branchList
