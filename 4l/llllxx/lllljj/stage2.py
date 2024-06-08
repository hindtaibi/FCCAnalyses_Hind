inputDir    = "../../../stage1bis/outputs"

#In this case, we are looking for he final state Z1, Z2, Z3* -> ll (l1 + l2) ll (l3 + l4) jj (j1 + j2)

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
               'wzp6_ee_eeH_Htautau_ecm240':{}
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
               .Filter("N_on_taken_leptons == 4 && N_off_taken_leptons == 0")          
               #.Filter("N_on_zed_leptonic == 2 && N_off_zed_leptonic == 0")           
            
               #Z1 decays into 2 leptons
               .Define("Z1_e",           "on_zed_leptonic_e[0]")
               .Define("Z1_m",           "on_zed_leptonic_m[0]")
               .Define("Z1_recoil_m",    "on_zed_leptonic_recoil_m[0]")
               .Define("Z1_pt",          "on_zed_leptonic_pt[0]")
               .Define("Z1_px",          "on_zed_leptonic_px[0]")
               .Define("Z1_py",          "on_zed_leptonic_py[0]")
               .Define("Z1_pz",          "on_zed_leptonic_pz[0]")
               .Define("Z1_p",           "on_zed_leptonic_p[0]")
               .Define("Z1_q",           "on_zed_leptonic_charge[0]")
               .Define("Z1_phi",         "on_zed_leptonic_phi[0]")
               .Define("Z1_theta",       "on_zed_leptonic_theta[0]")

               #Z2 decays into 2 leptons
               .Define("Z2_e",           "on_zed_leptonic_e[1]")
               .Define("Z2_m",           "on_zed_leptonic_m[1]")
               .Define("Z2_recoil_m",    "on_zed_leptonic_recoil_m[1]")
               .Define("Z2_pt",          "on_zed_leptonic_pt[1]")
               .Define("Z2_px",          "on_zed_leptonic_px[1]")
               .Define("Z2_py",          "on_zed_leptonic_py[1]")
               .Define("Z2_pz",          "on_zed_leptonic_pz[1]")
               .Define("Z2_p",           "on_zed_leptonic_p[1]")
               .Define("Z2_q",           "on_zed_leptonic_charge[1]")
               .Define("Z2_phi",         "on_zed_leptonic_phi[1]")
               .Define("Z2_theta",       "on_zed_leptonic_theta[1]")

               #Z3 decays into 2 jets
               .Define("Z3",             "ReconstructedParticle::jetsum(jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("Z3_m",           "Z3.M()")
               .Define("Z3_px",          "Z3.Px()")
               .Define("Z3_py",          "Z3.Py()")
               .Define("Z3_pz",          "Z3.Pz()")
               .Define("Z3_p",           "Z3.P()")
               .Define("Z3_pt",          "Z3.Pt()")
               .Define("Z3_theta",       "Z3.Theta()")
               .Define("Z3_phi",         "Z3.Phi()")
               
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

            "N_photons",
            "photons_e",
            "photons_px",
            "photons_py",
            "photons_pz",
            "photons_pt",
            "photons_phi",
            "photons_theta",
            
            #-------------------------------------------------------------------------------------------Leptons

            #LooseLeptons_p0 are leptons with p>p0
            "N_LooseLeptons_10",
            "N_LooseLeptons_2",
            "N_LooseLeptons_1",
            "LooseLeptons_10_e",
            "LooseLeptons_10_theta",
            "LooseLeptons_10_phi",
            "LooseLeptons_10_p",

            #Taken leptons are the selected leptons without the extraleptons, i. e. the leptons that reconstructed the Z
            "N_all_taken_leptons",
            "all_taken_leptons_e",
            "all_taken_leptons_p",
            "all_taken_leptons_px",
            "all_taken_leptons_py",
            "all_taken_leptons_pz",
            "all_taken_leptons_pt",
            "all_taken_leptons_theta",
            "all_taken_leptons_phi",
            "all_taken_leptons_eta",
            "all_taken_leptons_y",

            #Angular difference of the leptons that reconstructed the Z bosons
            "on_difftheta1_muons",
            "on_difftheta2_muons",
            "on_difftheta1_electrons",
            "on_difftheta2_electrons",
            "on_diffphi1_muons",
            "on_diffphi2_muons",
            "on_diffphi1_electrons",
            "on_diffphi2_electrons",      
            
            #-------------------------------------------------------------------------------------------------Z

            "Z1_e",
            "Z1_m",
            "Z1_recoil_m",
            "Z1_pt",
            "Z1_px",
            "Z1_py",
            "Z1_pz",
            "Z1_p",
            "Z1_q",
            "Z1_phi",
            "Z1_theta",

            "Z2_e",
            "Z2_m",
            "Z2_recoil_m",
            "Z2_pt",
            "Z2_px",
            "Z2_py",
            "Z2_pz",
            "Z2_p",
            "Z2_q",
            "Z2_phi",
            "Z2_theta",
            
            "Z3_m",
            "Z3_px",
            "Z3_py",
            "Z3_pz",
            "Z3_p",
            "Z3_pt",
            "Z3_theta",  
            "Z3_phi",
            
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
