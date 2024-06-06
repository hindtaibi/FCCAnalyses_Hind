inputDir    = "../../stage1bis/outputs"

#In this case, we are looking for he final state Z1, Z2, Z3* -> ll (l1 + l2) ll (l3 + l4) xx (jj, vv ou ll)

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
               
               #The three following filters do the same thing               
               .Filter("N_on_taken_leptons == 4")          #Filter to have exactly four lepton candidates for the Z
               #.Filter("N_on_zed_leptonic == 2")           #Filter to have exactly 2 Z candidates for the reconstructed particles
               
               #Final state we are looking for

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
               .Define("Z1_y",           "on_zed_leptonic_y[0]")
               .Define("Z1_eta",         "on_zed_leptonic_eta[0]")

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
               .Define("Z2_y",           "on_zed_leptonic_y[1]")
               .Define("Z2_eta",         "on_zed_leptonic_eta[1]")

               #Z3 can decay into anything (ll, vv, jj), we don't look at it for now
       
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
            
            #-------------------------------------------------------------------------------------------Leptons

            #Properties of the on/ff leptons (p(25,80) GeV)/(p(5,25) GeV), i. e. the leptons not coming from jets
            "on_muons_pt",
            "on_electrons_pt",
            "on_leptons_pt",
            "off_muons_pt",
            "off_electrons_pt",
            "off_leptons_pt",

            "on_muons_px",
            "on_electrons_px",
            "on_leptons_px",
            "off_muons_px",
            "off_electrons_px",
            "off_leptons_px",

            "on_muons_py",
            "on_electrons_py",
            "on_leptons_py",
            "off_muons_py",
            "off_electrons_py",
            "off_leptons_py",

            "on_muons_pz",
            "on_electrons_pz",
            "on_leptons_pz",
            "off_muons_pz",
            "off_electrons_pz",
            "off_leptons_pz",

            "on_muons_p",
            "on_electrons_p",
            "on_leptons_p",
            "off_muons_p",
            "off_electrons_p",
            "off_leptons_p",
            
            "on_muons_y",
            "on_electrons_y",
            "on_leptons_y",
            "off_muons_y",
            "off_electrons_y",
            "off_leptons_y",

            "on_muons_e",
            "on_electrons_e",
            "on_leptons_e",
            "off_muons_e",
            "off_electrons_e",
            "off_leptons_e",
            
            "N_on_muons",
            "N_on_electrons",
            "N_on_leptons",
            "N_off_muons",
            "N_off_electrons",
            "N_off_leptons",

            #LooseLeptons_p0 are leptons with p>p0
            "N_LooseLeptons_10",
            "N_LooseLeptons_2",
            "N_LooseLeptons_1",
            "LooseLeptons_10_pt",
            "LooseLeptons_10_theta",
            "LooseLeptons_10_phi",
            "LooseLeptons_10_p",

            #Taken leptons are the selected leptons without the extraleptons, i. e. the leptons that reconstructed the Z
            "N_on_taken_muons",
            "N_on_taken_electrons",
            "N_on_taken_leptons",
            "on_taken_leptons_e",
            "on_taken_leptons_p",
            "on_taken_leptons_px",
            "on_taken_leptons_py",
            "on_taken_leptons_pz",
            "on_taken_leptons_pt",
            "on_taken_leptons_theta",
            "on_taken_leptons_phi",
            "on_taken_leptons_eta",
            "on_taken_leptons_y",
            "on_taken_leptons_m",
            "on_taken_leptons_recoil_m",

            "N_off_taken_muons",
            "N_off_taken_electrons",
            "N_off_taken_leptons",
            "off_taken_leptons_e",
            "off_taken_leptons_p",
            "off_taken_leptons_px",
            "off_taken_leptons_py",
            "off_taken_leptons_pz",
            "off_taken_leptons_pt",
            "off_taken_leptons_theta",
            "off_taken_leptons_phi",
            "off_taken_leptons_eta",
            "off_taken_leptons_y",
            "off_taken_leptons_m",
            "off_taken_leptons_recoil_m",

            #Angular difference of the leptons that reconstructed the Z bosons
            "on_difftheta1_muons",
            "on_difftheta2_muons",
            "on_difftheta1_electrons",
            "on_difftheta2_electrons",
            "on_diffphi1_muons",
            "on_diffphi2_muons",
            "on_diffphi1_electrons",
            "on_diffphi2_electrons",

            "off_difftheta_muons",
            "off_difftheta_electrons",
            "off_diffphi_muons",
            "off_diffphi_electrons",        
            
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
            
            #----------------------------------------------------------------------------Missing/Visible stuff

            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss",
            
            "visible_mass_predef"           
          
        ]        

        return branchList
