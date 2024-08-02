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
            .Define("photon_tlv",           "photons_tlv[0]")   #The first photon is the highest-energy photon
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
            .Define("visible_m",            "visible_4vector.M()")   #Set to 0
            .Define("missing_theta",        "missing_tlv[0].Theta()")

            .Define("missing_tlv_forced",   "ReconstructedParticle::set_tlvXYZM(MissingET.momentum.x, MissingET.momentum.y, MissingET.momentum.z, 30)")
            .Define("emiss_forced",         "missing_tlv_forced.E()")

            .Define("visible_4vector",      "ReconstructedParticle::get_P4vis(ReconstructedParticles)")

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

            .Define("on_Z_muons",           "ReconstructedParticle::merge(on_Z_muons1, on_Z_muons2)")   #All muons used for Z reconstruction
            .Define("on_Z_muonic",          "ReconstructedParticle::merge(on_Z_muonic1, on_Z_muonic2)")   #Reconstructed muonic on shell Z bosons
    
            #With electrons
            .Define("on_Z_electrons1",      "ReconstructedParticle::findZleptons(on_electrons)")
            .Define("on_Z_electronic1",     "ReconstructedParticle::resonanceBuilder(91)(on_Z_electrons1)")
                        
            .Define("on_electrons2",        "ReconstructedParticle::remove(on_electrons, on_Z_electrons1)")
            .Define("on_Z_electrons2",      "ReconstructedParticle::findZleptons(on_electrons2)")
            .Define("on_Z_electronic2",     "ReconstructedParticle::resonanceBuilder(91)(on_Z_electrons2)")

            .Define("on_Z_electrons",       "ReconstructedParticle::merge(on_Z_electrons1, on_Z_electrons2)")   #All electrons used for Z reconstruction
            .Define("on_Z_electronic",      "ReconstructedParticle::merge(on_Z_electronic1, on_Z_electronic2)")   #Reconstructed electronic on shell Z bosons

            #We merge to get on_Z_leptons and on_Z_leptonic
            .Define("on_Z_leptons",         "ReconstructedParticle::merge(on_Z_muons, on_Z_electrons)")
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

            #Filter to have two on shell leptonic Z (llllxx)
            .Filter("N_other_Z_leptonic == 0 && N_on_Z_leptonic == 2")

            #We get Z1 and Z2
            .Define("Za",                   "on_Z_leptonic[0]")
            .Define("Zb",                   "on_Z_leptonic[1]")

            #We define which one is Z1 and which one is Z2 by looking at the recoil mass
            #The recoil mass closer to 125 corresponds to Z1and vice versa
            .Define("Z1",                   "ReconstructedParticle::sel_recoilMassCloserToH(Za, Zb)")
            .Define("Z2",                   "ReconstructedParticle::sel_recoilMassFurtherFromH(Za, Zb)")
            
            #Properties of Z1 and Z2
            .Define("Z1_tlv",               "ReconstructedParticle::get_tlv(Z1)")
            .Define("Z1_m",                 "Z1_tlv.M()")
            .Define("Z1_recoil_m",          "sqrt((240 - Z1_tlv.E())*(240 - Z1_tlv.E())-(Z1_tlv.P())*(Z1_tlv.P()))")
            .Define("Z1_theta",             "Z1_tlv.Theta()")
            .Define("Z1_phi",               "Z1_tlv.Phi()")
            .Define("Z1_eta",               "Z1_tlv.Eta()")
            .Define("Z1_e",                 "Z1_tlv.E()")
            .Define("Z1_p",                 "Z1_tlv.P()")
            .Define("Z1_px",                "Z1_tlv.Px()")
            .Define("Z1_py",                "Z1_tlv.Py()")
            .Define("Z1_pz",                "Z1_tlv.Pz()")

            .Define("Z2_tlv",               "ReconstructedParticle::get_tlv(Z2)")
            .Define("Z2_m",                 "Z2_tlv.M()")
            .Define("Z2_recoil_m",          "sqrt((240 - Z2_tlv.E())*(240 - Z2_tlv.E())-(Z2_tlv.P())*(Z2_tlv.P()))")
            .Define("Z2_theta",             "Z2_tlv.Theta()")
            .Define("Z2_phi",               "Z2_tlv.Phi()")
            .Define("Z2_eta",               "Z2_tlv.Eta()")
            .Define("Z2_e",                 "Z2_tlv.E()")
            .Define("Z2_p",                 "Z2_tlv.P()")
            .Define("Z2_px",                "Z2_tlv.Px()")
            .Define("Z2_py",                "Z2_tlv.Py()")
            .Define("Z2_pz",                "Z2_tlv.Pz()")

            #Z1a (Z1 + highest-energy phoyon) and Z2a (Z2 + highest-energy photon) recoil mass (maybe there is FSR)
            .Define("Z1a_tlv",              "Z1_tlv + photons_tlv[0]")
            .Define("Z2a_tlv",              "Z2_tlv + photons_tlv[0]")
            .Define("Z1a_recoil_m",         "sqrt((240 - Z1a_tlv.E())*(240 - Z1a_tlv.E())-(Z1a_tlv.P())*(Z1a_tlv.P()))")
            .Define("Z2a_recoil_m",         "sqrt((240 - Z2a_tlv.E())*(240 - Z2a_tlv.E())-(Z2a_tlv.P())*(Z2a_tlv.P()))")

            #Z2miss (Z2 + Missing tlv) mass
            .Define("Z2miss_tlv",           "Z2_tlv + missing_tlv[0]")
            .Define("Z2miss_m",             "Z2miss_tlv.M()")
            .Define("Z2miss_tlv_forced",    "Z2_tlv + missing_tlv_forced")
            .Define("Z2miss_m_forced",      "Z2miss_tlv_forced.M()")

            #Z1jj (Z1 + dijet) and Z2jj (Z2 + dijet) mass
            .Define("Z2jj_tlv",             "Z2_tlv + jj_tlv")
            .Define("Z2jj_m",               "Z2jj_tlv.M()")
            .Define("Z1jj_tlv",             "Z1_tlv + jj_tlv")
            .Define("Z1jj_m",               "Z1jj_tlv.M()")

            )
        return df2


    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list

    #The following list contains all the variables which are to be used

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
                #------------------------------------Forced missing information
                "Z2miss_m_forced",
                "emiss_forced"
                 
                ]

        return branchList



