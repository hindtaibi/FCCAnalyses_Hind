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
               .Filter("N_other_Z_leptons == 2 && N_on_Z_leptons ==2")

               #On shell Dilepton

               .Define("on_ll_tlv",         "on_Z_leptons_tlv[0] + on_Z_leptons_tlv[1]")
               .Define("on_ll_e",           "on_ll_tlv.E()")
               .Define("on_ll_p",           "on_ll_tlv.P()")
               .Define("on_ll_px",          "on_ll_tlv.Px()")
               .Define("on_ll_py",          "on_ll_tlv.Py()")
               .Define("on_ll_pz",          "on_ll_tlv.Pz()")
               .Define("on_ll_theta_diff",  "abs(on_Z_leptons_theta[0] - on_Z_leptons_theta[1])")
               .Define("on_ll_phi_diff",    "abs(on_Z_leptons_phi[0] - on_Z_leptons_phi[1])")
               .Define("on_ll_inv_m",       "on_ll_tlv.M()")

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

            #------------------------------------------------------------------------------------------------lla

            "on_lla_inv_m",  
            "on_lla_tlv",

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
            
            #----------------------------------------------------------------------------Missing/Visible stuff

            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss"       
          
        ]        

        return branchList
