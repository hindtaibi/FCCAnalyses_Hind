#Mandatory: List of processes

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
               'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
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
               'p8_ee_WW_ecm240':{},
               #Useless Background (gets eliminated easily)
               #'wzp6_ee_nunuH_HWW_ecm240':{},
               #'wzp6_ee_nunuH_HZa_ecm240':{},
               #'wzp6_ee_nunuH_Haa_ecm240':{},
               #'wzp6_ee_nunuH_Hbb_ecm240':{},
               #'wzp6_ee_nunuH_Hcc_ecm240':{},
               #'wzp6_ee_nunuH_Hgg_ecm240':{},
               #'wzp6_ee_nunuH_Hmumu_ecm240':{},
               #'wzp6_ee_nunuH_Hss_ecm240':{},
               #'wzp6_ee_nunuH_Htautau_ecm240':{}
               }

#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
prodTag = "FCCee/winter2023/IDEA/" #IDEA concept de detecteur


#Optional: output directory, default is local running directory
#outputDir = "outputs/fccee/higgs/mH-recoil/hzz/stage1/"
outputDir = "outputs"


#Optional: analysisName, default is ""
analysisName = " "

#Optional: ncpus, default is 4
nCPUS = 128

#Optional running on HTCondor, default is False
runBatch = False

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
#compGroup = "group_u_FCC.local_gen"




#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
    #__________________________________________________________________________________________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (
            df

            #------------------------------------------------------------------------------------We collect information about the particles

            .Alias("Muon0",                 "Muon#0.index")
            .Alias("Electron0",             "Electron#0.index")
            .Alias("Photon0",               "Photon#0.index")

            .Define("muons",                "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
            .Define("electrons",            "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
            .Define("photons",              "ReconstructedParticle::get(Photon0, ReconstructedParticles)")

            #We collect information about the photons
            .Define("photons_tlv",          "ReconstructedParticle::get_tlv(photons)")
            .Define("photon_tlv",           "photons_tlv[0]")
            .Define("photon_e",             "photon_tlv.E()")
            .Define("photon_px",            "photon_tlv.Px()")
            .Define("photon_py",            "photon_tlv.Py()")
            .Define("photon_pz",            "photon_tlv.Pz()")
            .Define("photon_theta",         "photon_tlv.Theta()")
            .Define("photon_phi",           "photon_tlv.Phi()")
            .Define("photon_eta",           "photon_tlv.Eta()")

            #We collect information about missing/visible variables
            .Define("emiss",                "MissingET.energy[0]")
            .Define("pxmiss",               "MissingET.momentum.x[0]")
            .Define("pymiss",               "MissingET.momentum.y[0]")
            .Define("pzmiss",               "MissingET.momentum.z[0]")
            .Define("missing_tlv",          "ReconstructedParticle::get_tlv(MissingET)")
            .Define("etmiss",               "sqrt((MissingET.momentum.x[0])*(MissingET.momentum.x[0]) + (MissingET.momentum.y[0])*(MissingET.momentum.y[0]))")
            .Define("missing_theta",        "missing_tlv[0].Theta()")
            
            #We force the invariant mass of the missing tlv to be around the Z mass
            .Define("missing_tlv_forced",     "ReconstructedParticle::set_tlvXYZM(MissingET.momentum.x, MissingET.momentum.y, MissingET.momentum.z, 91)")
            .Define("missing_recoil_m_forced","sqrt((240 - missing_tlv_forced.E())*(240 - missing_tlv_forced.E())-missing_tlv_forced.P()*missing_tlv_forced.P())")

            .Define("visible_4vector",      "ReconstructedParticle::get_P4vis(ReconstructedParticles)")
            .Define("visible_m",            "visible_4vector.M()")
            .Define("visible_p",            "visible_4vector.P()")
            .Define("visible_px",           "visible_4vector.Px()")
            .Define("visible_py",           "visible_4vector.Py()")
            .Define("visible_pz",           "visible_4vector.Pz()")

            #We select the muons/electrons within a certain range of high momentum; they should neither come from jets nor from an off shell Z
            .Define("on_muons",             "ReconstructedParticle::sel_p(20,80)(muons)")
            .Define("on_electrons",         "ReconstructedParticle::sel_p(20,80)(electrons)")

            #We select the muons/electrons with p > 5 GeV; they could come from an off shell Z
            .Define("other_muons",          "ReconstructedParticle::sel_p(5)(muons)")
            .Define("other_electrons",      "ReconstructedParticle::sel_p(5)(electrons)")

            #------------------------------------------------------------------------------------Z construction

            #On
            #We select 2 leptons (or 0 if there are none) which are the best candidates for the Z
            #findZleptons keeps the leptons, it doesn't reconstruct the Z
            #We create the Z from these leptons with resonanceBuilder
            #We remove these leptons from the selected leptons and do the process twice because we can have up to 2 pairs of leptons coming from an on shell Z
            
            #With muons
            .Define("on_Z_muons1",          "ReconstructedParticle::findZleptons(on_muons)")             
            .Define("on_Z_muonic1",         "ReconstructedParticle::resonanceBuilder(91)(on_Z_muons1)")

            .Define("on_muons2",            "ReconstructedParticle::remove(on_muons, on_Z_muons1)")
            .Define("on_Z_muons2",          "ReconstructedParticle::findZleptons(on_muons2)")
            .Define("on_Z_muonic2",         "ReconstructedParticle::resonanceBuilder(91)(on_Z_muons2)")

            .Define("on_Z_muons",           "ReconstructedParticle::merge(on_Z_muons1, on_Z_muons2)")
            .Define("on_Z_muonic",          "ReconstructedParticle::merge(on_Z_muonic1, on_Z_muonic2)")
    
            #With electrons
            .Define("on_Z_electrons1",      "ReconstructedParticle::findZleptons(on_electrons)")
            .Define("on_Z_electronic1",     "ReconstructedParticle::resonanceBuilder(91)(on_Z_electrons1)")
                        
            .Define("on_electrons2",        "ReconstructedParticle::remove(on_electrons, on_Z_electrons1)")
            .Define("on_Z_electrons2",      "ReconstructedParticle::findZleptons(on_electrons2)")
            .Define("on_Z_electronic2",     "ReconstructedParticle::resonanceBuilder(91)(on_Z_electrons2)")

            .Define("on_Z_electrons",       "ReconstructedParticle::merge(on_Z_electrons1, on_Z_electrons2)")
            .Define("on_Z_electronic",      "ReconstructedParticle::merge(on_Z_electronic1, on_Z_electronic2)")

            #We merge to get on_Z_leptons and on_Z_leptonic
            .Define("on_Z_leptons",         "ReconstructedParticle::merge(on_Z_muons, on_Z_electrons)")
            .Define("on_Z_leptons_tlv",     "ReconstructedParticle::get_tlv(on_Z_leptons)")
            .Define("on_l1_tlv",            "on_Z_leptons_tlv[0]")
            .Define("on_l2_tlv",            "on_Z_leptons_tlv[1]")
            .Define("on_Z_leptonic",        "ReconstructedParticle::merge(on_Z_muonic, on_Z_electronic)")

            #Off
            #We repeat the same process but with the other leptons
            #For the other leptons, we use findZleptons only once because there is only one off shell Z
            
            #We remove all the leptons that reconstructed the previous Z
            .Define("other_muons2",         "ReconstructedParticle::remove(other_muons, on_Z_muons)")
            .Define("other_electrons2",     "ReconstructedParticle::remove(other_electrons, on_Z_electrons)")
            
            #With muons
            .Define("other_Z_muons",        "ReconstructedParticle::findZleptons(other_muons2)")        
            .Define("other_Z_muonic",       "ReconstructedParticle::resonanceBuilder(91)(other_Z_muons)")
            
            #With electrons
            .Define("other_Z_electrons",    "ReconstructedParticle::findZleptons(other_electrons2)")
            .Define("other_Z_electronic",   "ReconstructedParticle::resonanceBuilder(91)(other_Z_electrons)")

            #We merge
            .Define("other_Z_leptons",      "ReconstructedParticle::merge(other_Z_muons, other_Z_electrons)")
            .Define("other_Z_leptons_tlv",  "ReconstructedParticle::get_tlv(other_Z_leptons)")
            .Define("other_l1_tlv",         "other_Z_leptons_tlv[0]")
            .Define("other_l2_tlv",         "other_Z_leptons_tlv[1]")
            .Define("other_Z_leptonic",     "ReconstructedParticle::merge(other_Z_muonic, other_Z_electronic)")

            #All the leptons that reconstructed Z bosons

            .Define("all_Z_leptons",        "ReconstructedParticle::merge(on_Z_leptons, other_Z_leptons)")
            .Define("N_on_Z_leptonic",      "ReconstructedParticle::get_n(on_Z_leptonic)")
            .Define("N_other_Z_leptonic",   "ReconstructedParticle::get_n(other_Z_leptonic)")

            #----------------------------------------------------------------------------------Jet construction

            #We select all the particles minus the particles used for the Z bosons to reconstruct the jets then we create the pseudojets with them

	        .Define("my_recoparticles",   	"ReconstructedParticle::remove(ReconstructedParticles, all_Z_leptons)")
            .Define("RP_px",              	"ReconstructedParticle::get_px(my_recoparticles)")
            .Define("RP_py",             	"ReconstructedParticle::get_py(my_recoparticles)")
            .Define("RP_pz",            	"ReconstructedParticle::get_pz(my_recoparticles)")
            .Define("RP_e",                	"ReconstructedParticle::get_e(my_recoparticles)")
            .Define("pseudo_jets",        	"JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")

            #Durham N=2
            #N is the number of jets we want to reconstruct. For example, in the final state ll ll jj we have two jets (N=2)

            .Define("FCCAnalysesJets_ee_genkt2",   "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)")          #Jets construction
            .Define("jets_ee_genkt2",              "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_genkt2)")     
            #Properties of the two jets
            .Define("jets_px2",                    "JetClusteringUtils::get_px(jets_ee_genkt2)")
            .Define("jets_py2",                    "JetClusteringUtils::get_py(jets_ee_genkt2)")
            .Define("jets_pz2",                    "JetClusteringUtils::get_pz(jets_ee_genkt2)")
            .Define("jets_p2",                     "JetClusteringUtils::get_p(jets_ee_genkt2)")
            .Define("jets_e2",                     "JetClusteringUtils::get_e(jets_ee_genkt2)")
            .Define("jets_m2",                     "JetClusteringUtils::get_m(jets_ee_genkt2)")
            .Define("jets_pt2",                    "JetClusteringUtils::get_pt(jets_ee_genkt2)")
            .Define("jets_y2",                     "JetClusteringUtils::get_y(jets_ee_genkt2)")
            .Define("jets_eta2",                   "JetClusteringUtils::get_eta(jets_ee_genkt2)")
            .Define("jets_theta2",                 "JetClusteringUtils::get_theta(jets_ee_genkt2)")
            .Define("jets_phi2",                   "JetClusteringUtils::get_phi(jets_ee_genkt2)")

            #-------------------------------------------------------------------------------------Jets properties
            
            #Dijet
            .Define("jj_tlv",         "ReconstructedParticle::jetsum(jets_e2, jets_px2, jets_py2, jets_pz2)")
            .Define("jj_e",           "jj_tlv.E()")
            .Define("jj_p",           "jj_tlv.P()")
            .Define("jj_px",          "jj_tlv.Px()")
            .Define("jj_py",          "jj_tlv.Py()")
            .Define("jj_pz",          "jj_tlv.Pz()")
            .Define("jj_pt",          "jj_tlv.Pt()")
            .Define("jj_theta",       "jj_tlv.Theta()")
            .Define("jj_phi",         "jj_tlv.Phi()")
            .Define("jj_eta",         "jj_tlv.Eta()")
            .Define("jj_m",           "jj_tlv.M()")

            #j1
            .Define("j1_e",              "jets_e2[0]")
            .Define("j1_p",              "jets_p2[0]")
            .Define("j1_px",             "jets_px2[0]")
            .Define("j1_py",             "jets_py2[0]")
            .Define("j1_pz",             "jets_pz2[0]")
            .Define("j1_pt",             "jets_pt2[0]")
            .Define("j1_theta",          "jets_theta2[0]")
            .Define("j1_phi",            "jets_phi2[0]")
            .Define("j1_m",              "jets_m2[0]")
            .Define("j1_eta",            "jets_eta2[0]")

            #j2
            .Define("j2_e",              "jets_e2[1]")
            .Define("j2_p",              "jets_p2[1]")
            .Define("j2_px",             "jets_px2[1]")
            .Define("j2_py",             "jets_py2[1]")
            .Define("j2_pz",             "jets_pz2[1]")
            .Define("j2_pt",             "jets_pt2[1]")
            .Define("j2_theta",          "jets_theta2[1]")
            .Define("j2_phi",            "jets_phi2[1]")
            .Define("j2_m",              "jets_m2[1]")
            .Define("j2_eta",            "jets_eta2[1]")

            #------------------------------------------------------------------------------------Properties of the Z bosons

            #Filter to have 1 on shell leptonic Z and 1 off shell leptonic Z (llxxll or xxllll)
            .Filter("N_other_Z_leptonic == 1 && N_on_Z_leptonic == 1")
            
            .Define("on_Z_leptonic_tlv",    "ReconstructedParticle::get_tlv(on_Z_leptonic)")
            .Define("other_Z_leptonic_tlv", "ReconstructedParticle::get_tlv(other_Z_leptonic)")

            .Define("Za_tlv",               "on_Z_leptonic_tlv[0]")   #Za is the on shell Z
            .Define("Zb_tlv",               "other_Z_leptonic_tlv[0]")   #Zb is the off shell Z
            
            
            #Properties of Za and Zb
            .Define("Za_m",                 "Za_tlv.M()")
            .Define("Za_recoil_m",          "sqrt((240 - Za_tlv.E())*(240 - Za_tlv.E())-(Za_tlv.P())*(Za_tlv.P()))")
            .Define("Za_theta",             "Za_tlv.Theta()")
            .Define("Za_phi",               "Za_tlv.Phi()")
            .Define("Za_eta",               "Za_tlv.Eta()")
            .Define("Za_e",                 "Za_tlv.E()")
            .Define("Za_p",                 "Za_tlv.P()")
            .Define("Za_px",                "Za_tlv.Px()")
            .Define("Za_py",                "Za_tlv.Py()")
            .Define("Za_pz",                "Za_tlv.Pz()")

            .Define("Zb_m",                 "Zb_tlv.M()")
            .Define("Zb_recoil_m",          "sqrt((240 - Zb_tlv.E())*(240 - Zb_tlv.E())-(Zb_tlv.P())*(Zb_tlv.P()))")
            .Define("Zb_theta",             "Zb_tlv.Theta()")
            .Define("Zb_phi",               "Zb_tlv.Phi()")
            .Define("Zb_eta",               "Zb_tlv.Eta()")
            .Define("Zb_e",                 "Zb_tlv.E()")
            .Define("Zb_p",                 "Zb_tlv.P()")
            .Define("Zb_px",                "Zb_tlv.Px()")
            .Define("Zb_py",                "Zb_tlv.Py()")
            .Define("Zb_pz",                "Zb_tlv.Pz()")

            #Zaa (Za + highest-energy photon) and Zba (Zb + highest-energy photon) recoil mass (maybe there is FSR)
            .Define("ll1a_tlv",             "Za_tlv + photons_tlv[0]")   #(ll1 is another name for Za)
            .Define("ll2a_tlv",             "Zb_tlv + photons_tlv[0]")   #(ll2 is another name for Zb)
            .Define("ll1a_recoil_m",        "sqrt((240 - ll1a_tlv.E())*(240 - ll1a_tlv.E())-(ll1a_tlv.P())*(ll1a_tlv.P()))")
            .Define("ll2a_recoil_m",        "sqrt((240 - ll2a_tlv.E())*(240 - ll2a_tlv.E())-(ll2a_tlv.P())*(ll2a_tlv.P()))")

            #Zbmiss mass (Zb + missing tlv)
            .Define("ll2miss_tlv",          "Zb_tlv + missing_tlv[0]")
            .Define("ll2miss_m",            "ll2miss_tlv.M()")
            .Define("ll2miss_tlv_forced",   "Zb_tlv + missing_tlv_forced")
            .Define("ll2miss_m_forced",     "ll2miss_tlv_forced.M()")

            .Define("ll1miss_tlv",          "Za_tlv + missing_tlv[0]")
            .Define("ll1miss_m",            "ll1miss_tlv.M()")

            #Zajj (Za + dijet) and Zbjj (Zb + dijet) mass 
            .Define("ll2jj_tlv",            "Zb_tlv + jj_tlv")
            .Define("ll2jj_m",              "ll2jj_tlv.M()")
            .Define("ll2jj_recoil_m",       "sqrt((240 - ll2jj_tlv.E())*(240 - ll2jj_tlv.E())-(ll2jj_tlv.P())*(ll2jj_tlv.P()))")
            .Define("ll1jj_tlv",            "Za_tlv + jj_tlv")
            .Define("ll1jj_m",              "ll1jj_tlv.M()")

            #ZZ (Za + Zb)
            .Define("ZZ_tlv",               "Za_tlv + Zb_tlv")
            .Define("ZZ_m",                 "ZZ_tlv.M()")
            .Define("ZZ_recoil_m",          "sqrt((240 - ZZ_tlv.E())*(240 - ZZ_tlv.E())-(ZZ_tlv.P())*(ZZ_tlv.P()))")

            #Leptons properties

            #l1 and l2 (for on and other)
            #on_l1 and on_l2 are the leptons coming from Za (on shell Z)
            .Define("on_l1_theta",          "on_l1_tlv.Theta()")
            .Define("on_l1_phi",            "on_l1_tlv.Phi()")
            .Define("on_l1_eta",            "on_l1_tlv.Eta()")
            
            .Define("on_l2_theta",          "on_l2_tlv.Theta()")
            .Define("on_l2_phi",            "on_l2_tlv.Phi()")
            .Define("on_l2_eta",            "on_l2_tlv.Eta()")
            
            #other_l1 and other_l2 are the leptons coming from Zb (off shell Z)
            .Define("other_l1_theta",       "other_l1_tlv.Theta()")
            .Define("other_l1_phi",         "other_l1_tlv.Phi()")
            .Define("other_l1_eta",         "other_l1_tlv.Eta()")
            
            .Define("other_l2_theta",       "other_l2_tlv.Theta()")
            .Define("other_l2_phi",         "other_l2_tlv.Phi()")
            .Define("other_l2_eta",         "other_l2_tlv.Eta()")
            
            #ll1 and ll2
            #ll1 is the dilepton coming from Za
            .Define("ll1_angle",            "ReconstructedParticle::get_angle_general(on_l1_tlv, on_l2_tlv)")
            .Define("ll1_theta_diff",       "abs(on_l1_theta - on_l2_theta)")
            .Define("ll1_phi_diff",         "abs(on_l1_phi - on_l2_phi)")
            .Define("ll1_eta_diff",         "abs(on_l1_eta - on_l2_eta)")
            .Define("ll1_delta_R",          "sqrt(ll1_phi_diff*ll1_phi_diff + ll1_eta_diff*ll1_eta_diff)")
            
            #ll2 is the dilepton coming from Zb
            .Define("ll2_angle",            "ReconstructedParticle::get_angle_general(other_l1_tlv, other_l2_tlv)")
            .Define("ll2_theta_diff",       "abs(other_l1_theta - other_l2_theta)")
            .Define("ll2_phi_diff",         "abs(other_l1_phi - other_l2_phi)")
            .Define("ll2_eta_diff",         "abs(other_l1_eta - other_l2_eta)")
            .Define("ll2_delta_R",          "sqrt(ll2_phi_diff*ll2_phi_diff + ll2_eta_diff*ll2_eta_diff)")

            #on lj (angular difference between the leptons coming from Za and the jets)
            .Define("on_l1j1_theta_diff",   "abs(on_l1_theta - j1_theta)")
            .Define("on_l1j1_phi_diff",     "abs(on_l1_phi - j1_phi)")
            .Define("on_l1j1_eta_diff",     "abs(on_l1_eta - j1_eta)")
            .Define("on_l1j1_delta_R",      "sqrt(on_l1j1_phi_diff*on_l1j1_phi_diff + on_l1j1_eta_diff*on_l1j1_eta_diff)")

            .Define("on_l1j2_theta_diff",   "abs(on_l1_theta - j2_theta)")
            .Define("on_l1j2_phi_diff",     "abs(on_l1_phi - j2_phi)")
            .Define("on_l1j2_eta_diff",     "abs(on_l1_eta - j2_eta)")
            .Define("on_l1j2_delta_R",      "sqrt(on_l1j2_phi_diff*on_l1j2_phi_diff + on_l1j2_eta_diff*on_l1j2_eta_diff)")

            .Define("on_l2j1_theta_diff",   "abs(on_l2_theta - j1_theta)")
            .Define("on_l2j1_phi_diff",     "abs(on_l2_phi - j1_phi)")
            .Define("on_l2j1_eta_diff",     "abs(on_l2_eta - j1_eta)")
            .Define("on_l2j1_delta_R",      "sqrt(on_l2j1_phi_diff*on_l2j1_phi_diff + on_l2j1_eta_diff*on_l2j1_eta_diff)")
            
            .Define("on_l2j2_theta_diff",   "abs(on_l2_theta - j2_theta)")
            .Define("on_l2j2_phi_diff",     "abs(on_l2_phi - j2_phi)")
            .Define("on_l2j2_eta_diff",     "abs(on_l2_eta - j2_eta)")
            .Define("on_l2j2_delta_R",      "sqrt(on_l2j2_phi_diff*on_l2j2_phi_diff + on_l2j2_eta_diff*on_l2j2_eta_diff)")

            #other lj (angular difference between the leptons coming from Zb and the jets)
            .Define("other_l1j1_theta_diff",   "abs(other_l1_theta - j1_theta)")
            .Define("other_l1j1_phi_diff",     "abs(other_l1_phi - j1_phi)")
            .Define("other_l1j1_eta_diff",     "abs(other_l1_eta - j1_eta)")
            .Define("other_l1j1_delta_R",      "sqrt(other_l1j1_phi_diff*other_l1j1_phi_diff + other_l1j1_eta_diff*other_l1j1_eta_diff)")

            .Define("other_l1j2_theta_diff",   "abs(other_l1_theta - j2_theta)")
            .Define("other_l1j2_phi_diff",     "abs(other_l1_phi - j2_phi)")
            .Define("other_l1j2_eta_diff",     "abs(other_l1_eta - j2_eta)")
            .Define("other_l1j2_delta_R",      "sqrt(other_l1j2_phi_diff*other_l1j2_phi_diff + other_l1j2_eta_diff*other_l1j2_eta_diff)")

            .Define("other_l2j1_theta_diff",   "abs(other_l2_theta - j1_theta)")
            .Define("other_l2j1_phi_diff",     "abs(other_l2_phi - j1_phi)")
            .Define("other_l2j1_eta_diff",     "abs(other_l2_eta - j1_eta)")
            .Define("other_l2j1_delta_R",      "sqrt(other_l2j1_phi_diff*other_l2j1_phi_diff + other_l2j1_eta_diff*other_l2j1_eta_diff)")

            .Define("other_l2j2_theta_diff",   "abs(other_l2_theta - j2_theta)")
            .Define("other_l2j2_phi_diff",     "abs(other_l2_phi - j2_phi)")
            .Define("other_l2j2_eta_diff",     "abs(other_l2_eta - j2_eta)")
            .Define("other_l2j2_delta_R",      "sqrt(other_l2j2_phi_diff*other_l2j2_phi_diff + other_l2j2_eta_diff*other_l2j2_eta_diff)")

            )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        #List of the variables we want to keep 
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
                "missing_recoil_m_forced",
                "missing_theta",
                "visible_m",
                "visible_p",
                "visible_px",
                "visible_py",
                "visible_pz",
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
                "ll2jj_recoil_m",
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
                "ll2miss_m",
                "ll2miss_m_forced",
                #--------------------------------ZZ
                "ZZ_m",
                "ZZ_recoil_m",
                #--------------------------------Leptons angular information
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
                "other_l2j2_delta_R"
                
                ]

        return branchList



