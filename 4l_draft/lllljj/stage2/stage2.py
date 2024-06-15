inputDir    = "../../stage1/outputs"

#In this case, we are looking for he final state Z1, Z2, Z3* -> ll (l1 + l2) ll (l3 + l4) jj (j5 + j6)
#Since we have two jets in the final state, we use the Durham algorithm with N = 2 to reconstruct the jets j5 and j6
#We also use the Durham algorithm with N = 3 for more investigation and in this case, the 3 reconstructed jets are named ja, jb and jc

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
nCPUS       = 128

#Optional running on HTCondor, default is False
#runBatch    = False

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
               
               #The three following filters do the same thing               
               #Filter to have exactly 2 Z candidates for the reconstructed particles
               #.Filter("zed_leptonic_m.size() == 2")   #Filter to have exactly 2 Z candidates for the reconstructed particles
               .Filter("N_taken_leptons == 4")          #Filter to have exactly four lepton candidates for the Z
               #.Filter("N_zed_leptonic == 2")
               
               #In the ll ll jj final state, we are not supposed to have any missing energy
               #.Filter("emiss < 20")

               #Z1 decays into 2 leptons
               .Define("Z1_e",           "zed_leptonic_e[0]")
               .Define("Z1_m",           "zed_leptonic_m[0]")
               .Define("Z1_recoil_m",    "zed_leptonic_recoil_m[0]")
               .Define("Z1_pt",          "zed_leptonic_pt[0]")
               .Define("Z1_px",          "zed_leptonic_px[0]")
               .Define("Z1_py",          "zed_leptonic_py[0]")
               .Define("Z1_pz",          "zed_leptonic_pz[0]")
               .Define("Z1_p",           "zed_leptonic_p[0]")
               .Define("Z1_q",           "zed_leptonic_charge[0]")
               .Define("Z1_phi",         "zed_leptonic_phi[0]")
               .Define("Z1_theta",       "zed_leptonic_theta[0]")
               .Define("Z1_y",           "zed_leptonic_y[0]")
               .Define("Z1_eta",         "zed_leptonic_eta[0]")

               #Z2 decays into 2 leptons
               .Define("Z2_e",           "zed_leptonic_e[1]")
               .Define("Z2_m",           "zed_leptonic_m[1]")
               .Define("Z2_recoil_m",    "zed_leptonic_recoil_m[1]")
               .Define("Z2_pt",          "zed_leptonic_pt[1]")
               .Define("Z2_px",          "zed_leptonic_px[1]")
               .Define("Z2_py",          "zed_leptonic_py[1]")
               .Define("Z2_pz",          "zed_leptonic_pz[1]")
               .Define("Z2_p",           "zed_leptonic_p[1]")
               .Define("Z2_q",           "zed_leptonic_charge[1]")
               .Define("Z2_phi",         "zed_leptonic_phi[1]")
               .Define("Z2_theta",       "zed_leptonic_theta[1]")
               .Define("Z2_y",           "zed_leptonic_y[1]")
               .Define("Z2_eta",         "zed_leptonic_eta[1]")

               #Z3 decays into jets and it is an off-shell 
               #We sum the jets' tlv to recreate Z3's tlv because Z3 decays into 2 jets
               #jetsum returns zoffshell where zoffshell is a TLorentzVector variable
               
               .Define("Z3",             "ReconstructedParticle::jetsum(jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("Z3_m",           "Z3.M()")
               .Define("Z3_px",          "Z3.Px()")
               .Define("Z3_py",          "Z3.Py()")
               .Define("Z3_pz",          "Z3.Pz()")
               .Define("Z3_p",           "Z3.P()")
               .Define("Z3_pt",          "Z3.Pt()")
               .Define("Z3_theta",       "Z3.Theta()")
               .Define("Z3_phi",         "Z3.Phi()")
               .Define("Z3_eta",         "Z3.Eta()")

               #Angular difference
            
               #Theta
               .Define("zed_electrons_difftheta1",       "abs(zed_electrons_theta[0]-zed_electrons_theta[1])")
               .Define("zed_muons_difftheta1",           "abs(zed_muons_theta[0]-zed_muons_theta[1])")
               .Define("zed_leptons_difftheta1",         "abs(zed_leptons_theta[0]-zed_leptons_theta[1])")

               .Define("zed_electrons_difftheta2",       "abs(zed_electrons_theta_bis[0]-zed_electrons_theta_bis[1])")
               .Define("zed_muons_difftheta2",           "abs(zed_muons_theta_bis[0]-zed_muons_theta_bis[1])")
               .Define("zed_leptons_difftheta2",         "abs(zed_leptons_theta_bis[0]-zed_leptons_theta_bis[1])")

               #Phi
               .Define("zed_electrons_diffphi1",         "abs(zed_electrons_phi[0]-zed_electrons_phi[1])")
               .Define("zed_muons_diffphi1",             "abs(zed_muons_phi[0]-zed_muons_phi[1])")
               .Define("zed_leptons_diffphi1",           "abs(zed_leptons_phi[0]-zed_leptons_phi[1])")

               .Define("zed_electrons_diffphi2",         "abs(zed_electrons_phi_bis[0]-zed_electrons_phi_bis[1])")
               .Define("zed_muons_diffphi2",             "abs(zed_muons_phi_bis[0]-zed_muons_phi_bis[1])")
               .Define("zed_leptons_diffphi2",           "abs(zed_leptons_phi_bis[0]-zed_leptons_phi_bis[1])")
                

	           #jetconstituents_ee_genkt2 is obtained with JetClusteringUtils::get_constituents
		       #jetconstituents_ee_2 is obtained with JetConstituentsUtils::build_constituents_cluster
     		   #jetconstituents_2 is obtained with JetConstituentsUtils::count_consts

               #Durham trie naturellement les jets dans l'ordre décroissant de 
               
               #Durham N = 2
               .Define("j5_p",              "jets_p2[0]")
               .Define("j6_p",              "jets_p2[1]")

               .Define("j5_pt",             "jets_pt2[0]")
               .Define("j6_pt",             "jets_pt2[1]")

               .Define("j5_e",              "jets_e2[0]")
               .Define("j6_e",              "jets_e2[1]")

               .Define("j5_px",             "jets_px2[0]")
               .Define("j6_px",             "jets_px2[1]")
               
               .Define("j5_py",             "jets_py2[0]")
               .Define("j6_py",             "jets_py2[1]")

               .Define("j5_pz",             "jets_pz2[0]")
               .Define("j6_pz",             "jets_pz2[1]")

               .Define("j5_theta",          "jets_theta2[0]")
               .Define("j6_theta",          "jets_theta2[1]")
               
               .Define("j5_phi",            "jets_phi2[0]")
               .Define("j6_phi",            "jets_phi2[1]")

               .Define("j5_eta",            "jets_eta2[0]")
               .Define("j6_eta",            "jets_eta2[1]")

               .Define("j5_const",          "jetconstituents_2[0]")
               .Define("j6_const",          "jetconstituents_2[1]")
               
               .Define("min_const_2",       "min(j5_const, j6_const)")
               .Define("max_const_2",       "max(j5_const, j6_const)")
               .Define("mean_const_2",      "(j5_const + j6_const)/2")
               
               .Define("diffthetajets_56",  "abs(j5_theta - j6_theta)")
               .Define("diffphijets_56",    "abs(j5_phi - j6_phi)")

               .Define("missing_theta",     "missing_tlv[0].Theta()")

               .Define("angle_miss_jet",    "ReconstructedParticle::get_angle(missing_tlv[0], jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("angle_miss_j5",     "angle_miss_jet[0]")
               .Define("angle_miss_j6",     "angle_miss_jet[1]")
               .Define("min_angle_miss_jet","min(angle_miss_j5, angle_miss_j6)")
               .Define("max_angle_miss_jet","max(angle_miss_j5, angle_miss_j6)")

               
               #Durham N = 3 
               .Define("ja_const",          "jetconstituents_3[0]")
               .Define("jb_const",          "jetconstituents_3[1]")
               .Define("jc_const",          "jetconstituents_3[2]")
               
               .Define("min_const_3",       "min(ja_const, min(jb_const, jc_const))")
               .Define("max_const_3",       "max(ja_const, max(jb_const, jc_const))")
               .Define("mean_const_3",      "(ja_const + jb_const + jc_const)/3")

               .Define("ja_theta",          "jets_theta3[0]")
               .Define("jb_theta",          "jets_theta3[1]")
               .Define("jc_theta",          "jets_theta3[2]")

               .Define("diffthetajets_ab",  "abs(ja_theta - jb_theta)")
               .Define("diffthetajets_ac",  "abs(ja_theta - jc_theta)")
               .Define("diffthetajets_bc",  "abs(jb_theta - jc_theta)")

               .Define("ja_phi",            "jets_phi3[0]")
               .Define("jb_phi",            "jets_phi3[1]")
               .Define("jc_phi",            "jets_phi3[2]")

               .Define("diffphijets_ab",    "abs(ja_phi - jb_phi)")
               .Define("diffphijets_ac",    "abs(ja_phi - jc_phi)")
               .Define("diffphijets_bc",    "abs(jb_phi - jc_phi)")

               .Define("ja_e", "jets_e3[0]")
               .Define("jb_e", "jets_e3[1]")
               .Define("jc_e", "jets_e3[2]")
               
               .Define("ja_p", "jets_p3[0]")
               .Define("jb_p", "jets_p3[1]")
               .Define("jc_p", "jets_p3[2]")
 
       
               )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list.
    def output():
        branchList = [
            
            #-------------------------------------------------------------------------------------------Photons

            "N_photons",
            "photons_e",
            "photons_p",
            "photons_px",
            "photons_py",
            "photons_pz",
            "photons_pt",
            "photons_phi",
            "photons_theta",
            "photons_eta",
            "photons_y",

            #----------------------------------------------------------------------------Leptons

            "selected_muons_pt",
            "selected_electrons_pt",
            "selected_leptons_pt",

            "selected_muons_px",
            "selected_electrons_px",
            "selected_leptons_px",

            "selected_muons_py",
            "selected_electrons_py",
            "selected_leptons_py",

            "selected_muons_pz",
            "selected_electrons_pz",
            "selected_leptons_pz",

            "selected_muons_y",
            "selected_electrons_y",
            "selected_leptons_y",

            "selected_muons_p",
            "selected_electrons_p",
            "selected_leptons_p",

            "selected_muons_e",
            "selected_electrons_e",
            "selected_leptons_e",
            
            "N_zed_leptonic",   
            "N_selected_leptons",
            "N_taken_leptons",

            "N_LooseLeptons_10",
            "N_LooseLeptons_2",
            "N_LooseLeptons_1",
            "LooseLeptons_10_pt",
            "LooseLeptons_10_theta",
            "LooseLeptons_10_phi",
            "LooseLeptons_10_p",

            "taken_leptons_e",
            "taken_leptons_p",
            "taken_leptons_px",
            "taken_leptons_py",
            "taken_leptons_pz",
            "taken_leptons_pt",
            "taken_leptons_theta",
            "taken_leptons_phi",
            "taken_leptons_eta",
            "taken_leptons_y",
            "taken_leptons_m",
            "taken_leptons_recoil_m",

            "zed_leptons_difftheta1",
            "zed_leptons_diffphi1",
            "zed_leptons_difftheta2",
            "zed_leptons_diffphi2",
                        
            #----------------------------------------------------------------------------Z

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
            "Z1_y",
            "Z1_eta",

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
            "Z2_y",
            "Z2_eta",

            "Z3_m",
            "Z3_px",
            "Z3_py",
            "Z3_pz",
            "Z3_p",
            "Z3_pt",
            "Z3_theta",  
            "Z3_eta",
            "Z3_phi",
            
            #----------------------------------------------------------------------------Jets
            
            #j5 and j6 (N = 2)

            "j5_p",
            "j5_pt",
            "j5_e",
            "j5_px",
            "j5_py",
            "j5_pz",
            "j5_theta", 
            "j5_phi",
            "j5_eta",
            "j5_const",

            "j6_p",
            "j6_pt",
            "j6_e",
            "j6_px",
            "j6_py",
            "j6_pz",
            "j6_theta", 
            "j6_phi",
            "j6_eta",
            "j6_const",

            "min_const_2",
            "max_const_2",
            "mean_const_2",
            
            "diffthetajets_56",
            "diffphijets_56",

            "missing_theta",
            "angle_miss_j5",
            "angle_miss_j6",
            "min_angle_miss_jet",
            "max_angle_miss_jet",

            "dmerge_2_45",
            "dmerge_2_34",
            "dmerge_2_23",
            "dmerge_2_12",

            #ja, jb and jc (N = 3)

            "diffthetajets_ab",
            "diffthetajets_ac",
            "diffthetajets_bc",

            "diffphijets_ab",
            "diffphijets_ac",
            "diffphijets_bc",
            
            "ja_e",
            "jb_e",
            "jc_e",

            "ja_p",
            "jb_p",
            "jc_p",
            
            "min_const_3",
            "max_const_3",
            "mean_const_3",

            "dmerge_3_45",
            "dmerge_3_34",
            "dmerge_3_23",
            "dmerge_3_12",
            
            #----------------------------------------------------------------------------Missing/Visible stuff

            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss",
            
            "visible_mass_predef"           
          
        ]        

        return branchList
