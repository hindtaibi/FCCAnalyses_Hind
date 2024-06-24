#Mandatory: List of processes

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},   #Signal
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
               'wzp6_ee_eeH_HZZ_ecm240':{},     #Signal
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
               'p8_ee_ZZ_ecm240':{'fraction':0.01},
               'p8_ee_WW_ecm240':{'fraction':0.001}
               }

#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
#prodTag = "FCCee/spring2021/IDEA/" #IDEA concept de detecteur
#prodTag = "FCCee/pre_fall2022/IDEA/" #IDEA concept de detecteur
prodTag = "FCCee/winter2023/IDEA/" #IDEA concept de detecteur


#Optional: output directory, default is local running directory
#outputDir = "outputs/fccee/higgs/mH-recoil/hzz/stage1/"
outputDir = "outputs"


#Optional: analysisName, default is ""
analysisName = "4l_stage1bis"

#Optional: ncpus, default is 4
nCPUS = 128

#Optional running on HTCondor, default is False
#runBatch = False

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
            .Alias("Muon0",                 "Muon#0.index")
            .Alias("Electron0",             "Electron#0.index")
            .Alias("Photon0",               "Photon#0.index")

            .Define("muons",                "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
            .Define("electrons",            "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
            .Define("leptons",              "ReconstructedParticle::merge(muons, electrons)")
            .Define("photons",              "ReconstructedParticle::get(Photon0, ReconstructedParticles)")

            #We collect information about the photons
            
            .Define("N_photons",            "ReconstructedParticle::get_n(photons)")
            .Define("photons_recoil",       "ReconstructedParticle::recoilBuilder(240)(photons)")
	        .Define("photons_recoil_m",     "ReconstructedParticle::get_mass(photons_recoil)")
            .Define("photons_tlv",          "ReconstructedParticle::get_tlv(photons)")

            #We select the muons/electrons within a certain range of high momentum; they should neither come from jets nor from an off shell Z

            .Define("on_muons",             "ReconstructedParticle::sel_p(20,80)(muons)")
            .Define("on_electrons",         "ReconstructedParticle::sel_p(20,80)(electrons)")
            .Define("on_leptons",           "ReconstructedParticle::merge(on_muons, on_electrons)")

            #We select the muons/electrons with p > 5 GeV; they could come from an off shell Z

            .Define("other_muons",          "ReconstructedParticle::sel_p(5)(muons)")
            .Define("other_electrons",      "ReconstructedParticle::sel_p(5)(electrons)")
            .Define("other_leptons",        "ReconstructedParticle::merge(other_muons, other_electrons)")

            #Properties of the preselected leptons

            #On                      
            .Define("N_on_muons",           "ReconstructedParticle::get_n(on_muons)")
            .Define("N_on_electrons",       "ReconstructedParticle::get_n(on_electrons)")
            .Define("N_on_leptons",         "ReconstructedParticle::get_n(on_leptons)")
            
            .Define("on_muons_tlv",         "ReconstructedParticle::get_tlv(on_muons)")
            .Define("on_electrons_tlv",     "ReconstructedParticle::get_tlv(on_electrons)")
            .Define("on_leptons_tlv",       "ReconstructedParticle::get_tlv(on_leptons)")
                
            #Other          
            .Define("N_other_muons",        "ReconstructedParticle::get_n(other_muons)")
            .Define("N_other_electrons",    "ReconstructedParticle::get_n(other_electrons)")
            .Define("N_other_leptons",      "ReconstructedParticle::get_n(other_leptons)")
            
            .Define("other_muons_tlv",      "ReconstructedParticle::get_tlv(on_muons)")
            .Define("other_electrons_tlv",  "ReconstructedParticle::get_tlv(on_electrons)")
            .Define("other_leptons_tlv",    "ReconstructedParticle::get_tlv(on_leptons)")

            #------------------------------------------------------------------------------------Z construction
            
            #On
            #We select 2 muons (or 0 if there are none) which are the best candidates for the Z
            #findZleptons keeps the leptons, it doesn't reconstruct the Z
            #We create the Z from these muons with resonanceBuilder
            #We remove these muons from the selected muons and do the process twice because we can have up to 2 pairs of muons coming from an on shell Z

            .Define("on_Z_muons1",          "ReconstructedParticle::findZleptons(on_muons)")               #Selection of the muons (2 or 0) that could come from a Z
            .Define("on_Z_muonic1",         "ReconstructedParticle::resonanceBuilder(91)(on_Z_muons1)")    #Builds resonance from 2 particles
            
            .Define("on_muons2",            "ReconstructedParticle::remove(on_muons, on_Z_muons1)")
            .Define("on_Z_muons2",          "ReconstructedParticle::findZleptons(on_muons2)")
            .Define("on_Z_muonic2",         "ReconstructedParticle::resonanceBuilder(91)(on_Z_muons2)")

            .Define("on_extramuons",        "ReconstructedParticle::remove(on_muons2, on_Z_muons2)")     #All muons not selected by findZleptons
            .Define("on_Z_muons",           "ReconstructedParticle::merge(on_Z_muons1, on_Z_muons2)")    #All muons selected by findZleptons
            .Define("on_Z_muonic",          "ReconstructedParticle::merge(on_Z_muonic1, on_Z_muonic2)")  #We merge the Z muonic, their number can be 0, 1 or 2
            
            #Same process but with the electrons

            .Define("on_Z_electrons1",      "ReconstructedParticle::findZleptons(on_electrons)")
            .Define("on_Z_electronic1",     "ReconstructedParticle::resonanceBuilder(91)(on_Z_electrons1)")
                        
            .Define("on_electrons2",        "ReconstructedParticle::remove(on_electrons, on_Z_electrons1)")
            .Define("on_Z_electrons2",      "ReconstructedParticle::findZleptons(on_electrons2)")
            .Define("on_Z_electronic2",     "ReconstructedParticle::resonanceBuilder(91)(on_Z_electrons2)")
                
            .Define("on_extraelectrons",    "ReconstructedParticle::remove(on_electrons2, on_Z_electrons2)")     #All electrons not selected by findZleptons
            .Define("on_Z_electrons",       "ReconstructedParticle::merge(on_Z_electrons1, on_Z_electrons2)")    #All electrons selected by findZleptons
            .Define("on_Z_electronic",      "ReconstructedParticle::merge(on_Z_electronic1, on_Z_electronic2)")  #We merge the Z electronic, their number can be 0, 1 or 2
            
            #All the leptons that reconstructed/didn't reconstruct the on shell Z
            
            .Define("on_Z_leptons",         "ReconstructedParticle::merge(on_Z_muons, on_Z_electrons)")
	        .Define("N_on_Z_leptons",       "ReconstructedParticle::get_n(on_Z_leptons)")
	        .Define("on_Z_leptons_recoil",  "ReconstructedParticle::recoilBuilder(240)(on_Z_leptons)")
	        .Define("on_Z_leptons_recoil_m","ReconstructedParticle::get_mass(on_Z_leptons_recoil)")
	        .Define("on_Z_leptons_tlv",     "ReconstructedParticle::get_tlv(on_Z_leptons)")

		
            .Define("on_extra_leptons",            "ReconstructedParticle::merge(on_extramuons, on_extraelectrons)")
	        .Define("N_on_extra_leptons",          "ReconstructedParticle::get_n(on_extra_leptons)")
	        .Define("on_extra_leptons_recoil",     "ReconstructedParticle::recoilBuilder(240)(on_extra_leptons)")
	        .Define("on_extra_leptons_recoil_m",   "ReconstructedParticle::get_mass(on_extra_leptons_recoil)")
            .Define("on_extra_leptons_tlv",        "ReconstructedParticle::get_tlv(on_extra_leptons)")

            #We group the Z bosons previously reconstructed to get on_Z_leptonic

            .Define("on_Z_leptonic",        	  "ReconstructedParticle::merge(on_Z_muonic, on_Z_electronic)")
            .Define("N_on_Z_leptonic",            "ReconstructedParticle::get_n(on_Z_leptonic)")
	        .Define("on_Z_leptonic_recoil",       "ReconstructedParticle::recoilBuilder(240)(on_Z_leptonic)")
	        .Define("on_Z_leptonic_recoil_m",     "ReconstructedParticle::get_mass(on_Z_leptonic_recoil)")
            .Define("on_Z_leptonic_tlv",          "ReconstructedParticle::get_tlv(on_Z_leptonic)") 

            #Off
            #We repeat the same process but with the other leptons
            #For the other leptons, we use findZleptons only once because there is only one off shell Z
            
            #We remove all the leptons that reconstructed the previous Z
            .Define("other_muons2",          "ReconstructedParticle::remove(other_muons, on_Z_muons)")
            .Define("other_electrons2",      "ReconstructedParticle::remove(other_electrons, on_Z_electrons)")

            .Define("other_Z_muons",         "ReconstructedParticle::findZleptons(other_muons2)")                #Selection of the muons (2 or 0) that could come from a Z
            .Define("other_Z_muonic",        "ReconstructedParticle::resonanceBuilder(91)(other_Z_muons)")       #Builds resonance from 2 particles
            .Define("other_extramuons",      "ReconstructedParticle::remove(other_muons2, other_Z_muons)")       #All muons not selected by findZleptons

	        #Same thing but with the electrons
            .Define("other_Z_electrons",     "ReconstructedParticle::findZleptons(other_electrons2)")               
            .Define("other_Z_electronic",    "ReconstructedParticle::resonanceBuilder(91)(other_Z_electrons)")  
            .Define("other_extraelectrons",  "ReconstructedParticle::remove(other_electrons2, other_Z_electrons)")     

            .Define("other_Z_leptonic",     	     "ReconstructedParticle::merge(other_Z_muonic, other_Z_electronic)")   #We merge to create the other Z leptonic (their number can be 0, 1, or 2)
	        .Define("N_other_Z_leptonic",    	     "ReconstructedParticle::get_n(other_Z_leptonic)")
	        .Define("other_Z_leptonic_recoil",       "ReconstructedParticle::recoilBuilder(240)(other_Z_leptonic)")
	        .Define("other_Z_leptonic_recoil_m",     "ReconstructedParticle::get_mass(other_Z_leptonic_recoil)")
            .Define("other_Z_leptonic_tlv",    	     "ReconstructedParticle::get_tlv(other_Z_leptonic)")
		
            .Define("other_extra_leptons",    	     "ReconstructedParticle::merge(other_extramuons, other_extraelectrons)")
	        .Define("N_other_extra_leptons",          "ReconstructedParticle::get_n(other_extra_leptons)")
	        .Define("other_extra_leptons_recoil",     "ReconstructedParticle::recoilBuilder(240)(other_extra_leptons)")
	        .Define("other_extra_leptons_recoil_m",   "ReconstructedParticle::get_mass(other_extra_leptons_recoil)")
	        .Define("other_extra_leptons_tlv",        "ReconstructedParticle::get_tlv(other_extra_leptons)")
		
            .Define("other_Z_leptons",               "ReconstructedParticle::merge(other_Z_muons, other_Z_electrons)")   #All the leptons that reconstructed the off shell Z (called the other Z)
	        .Define("N_other_Z_leptons",             "ReconstructedParticle::get_n(other_Z_leptons)")
	        .Define("other_Z_leptons_recoil",        "ReconstructedParticle::recoilBuilder(240)(other_Z_leptons)")
	        .Define("other_Z_leptons_recoil_m",      "ReconstructedParticle::get_mass(other_Z_leptons_recoil)")
	        .Define("other_Z_leptons_tlv",           "ReconstructedParticle::get_tlv(other_Z_leptons)")

            #Properties of the taken leptons

            .Define("all_Z_leptons",                 "ReconstructedParticle::merge(on_Z_leptons, other_Z_leptons)")
	        .Define("N_all_Z_leptons",               "ReconstructedParticle::get_n(all_Z_leptons)")
	        .Define("all_Z_leptons_tlv",                     "ReconstructedParticle::get_tlv(all_Z_leptons)")

            #----------------------------------------------------------------------------------Jet construction

            #We select all the particles minus the particles used for the Z bosons and the photons to reconstruct the jets then we create the pseudojets with them 
            
	        .Define("my_recoparticles1",   	       "ReconstructedParticle::remove(ReconstructedParticles, photons)")
            .Define("my_recoparticles",    	       "ReconstructedParticle::remove(my_recoparticles1, all_Z_leptons)")
            .Define("RP_px",              	       "ReconstructedParticle::get_px(my_recoparticles)")
            .Define("RP_py",             	       "ReconstructedParticle::get_py(my_recoparticles)")
            .Define("RP_pz",            	       "ReconstructedParticle::get_pz(my_recoparticles)")
            .Define("RP_e",                	       "ReconstructedParticle::get_e(my_recoparticles)")
            .Define("pseudo_jets",        	       "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")

            #Durham N=2
            #N is the number of jets we want to reconstruct. For example, in the final state ll ll jj we have two jets (N=2)
            #Construction des jets selon l'algo durham kt pour N=2 + (ligne2) mise en objet "pseudo_jets", dont on peut extraire des informations cinematiques
            
            .Define("FCCAnalysesJets_ee_genkt2",   "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)")          #Contrcution of the jets
            .Define("jets_ee_genkt2",              "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_genkt2)")     #Mise en objet pour pouvoir en extraire les proprietes
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

            .Define("jetconstituents_ee_genkt2",   "JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_genkt2)")
            .Define("jetconstituents_ee_2",        "JetConstituentsUtils::build_constituents_cluster(my_recoparticles, jetconstituents_ee_genkt2)")
            .Define("jetconstituents_2",           "JetConstituentsUtils::count_consts(jetconstituents_ee_2)")

            #La fonction get_constituents donne le nombre de particules dans le jet ? 

            .Define("dmerge_2_45",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 4)")
            .Define("dmerge_2_34",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 3)")
            .Define("dmerge_2_23",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 2)")
            .Define("dmerge_2_12",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 1)")
            
            #Durham N=3
            
            .Define("FCCAnalysesJets_ee_genkt3",   "JetClustering::clustering_ee_kt(2, 3, 1, 0)(pseudo_jets)")
            .Define("jets_ee_genkt3",              "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_genkt3)")

            .Define("jets_px3",                    "JetClusteringUtils::get_px(jets_ee_genkt3)")
            .Define("jets_py3",                    "JetClusteringUtils::get_py(jets_ee_genkt3)")
            .Define("jets_pz3",                    "JetClusteringUtils::get_pz(jets_ee_genkt3)")
            .Define("jets_p3",                     "JetClusteringUtils::get_p(jets_ee_genkt3)")
            .Define("jets_e3",                     "JetClusteringUtils::get_e(jets_ee_genkt3)")
            .Define("jets_m3",                     "JetClusteringUtils::get_m(jets_ee_genkt3)")
            .Define("jets_pt3",                    "JetClusteringUtils::get_pt(jets_ee_genkt3)")
            .Define("jets_y3",                     "JetClusteringUtils::get_y(jets_ee_genkt3)")
            .Define("jets_eta3",                   "JetClusteringUtils::get_eta(jets_ee_genkt3)")
            .Define("jets_theta3",                 "JetClusteringUtils::get_theta(jets_ee_genkt3)")
            .Define("jets_phi3",                   "JetClusteringUtils::get_phi(jets_ee_genkt3)")

            .Define("jetconstituents_ee_genkt3",   "JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_genkt3)")
            .Define("jetconstituents_ee_3",        "JetConstituentsUtils::build_constituents_cluster(my_recoparticles, jetconstituents_ee_genkt3)")
            .Define("jetconstituents_3",           "JetConstituentsUtils::count_consts(jetconstituents_ee_3)")

            .Define("dmerge_3_45",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 4)")
            .Define("dmerge_3_34",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 3)")
            .Define("dmerge_3_23",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 2)")
            .Define("dmerge_3_12",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 1)")
            
            #Durham N=4
            
            .Define("FCCAnalysesJets_ee_genkt4",   "JetClustering::clustering_ee_kt(2, 4, 1, 0)(pseudo_jets)")
            .Define("jets_ee_genkt4",              "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_genkt4)")

            .Define("jets_px4",                    "JetClusteringUtils::get_px(jets_ee_genkt4)")
            .Define("jets_py4",                    "JetClusteringUtils::get_py(jets_ee_genkt4)")
            .Define("jets_pz4",                    "JetClusteringUtils::get_pz(jets_ee_genkt4)")
            .Define("jets_p4",                     "JetClusteringUtils::get_p(jets_ee_genkt4)")
            .Define("jets_e4",                     "JetClusteringUtils::get_e(jets_ee_genkt4)")
            .Define("jets_m4",                     "JetClusteringUtils::get_m(jets_ee_genkt4)")
            .Define("jets_pt4",                    "JetClusteringUtils::get_pt(jets_ee_genkt4)")
            .Define("jets_y4",                     "JetClusteringUtils::get_y(jets_ee_genkt4)")
            .Define("jets_eta4",                   "JetClusteringUtils::get_eta(jets_ee_genkt4)")
            .Define("jets_theta4",                 "JetClusteringUtils::get_theta(jets_ee_genkt4)")
            .Define("jets_phi4",                   "JetClusteringUtils::get_phi(jets_ee_genkt4)")

            .Define("jetconstituents_ee_genkt4",   "JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_genkt4)")
            .Define("jetconstituents_ee_4",        "JetConstituentsUtils::build_constituents_cluster(my_recoparticles, jetconstituents_ee_genkt4)")
            .Define("jetconstituents_4",           "JetConstituentsUtils::count_consts(jetconstituents_ee_4)")

            .Define("dmerge_4_45",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt4, 4)")
            .Define("dmerge_4_34",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt4, 3)")
            .Define("dmerge_4_23",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt4, 2)")
            .Define("dmerge_4_12",                 "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt4, 1)")
            
            #-----------------------------------------------------------------------------------Missing/Visible

            #Missing energy and momentum

            .Define("emiss",                       "MissingET.energy[0]")
            .Define("pxmiss",                      "MissingET.momentum.x[0]")
            .Define("pymiss",                      "MissingET.momentum.y[0]")
            .Define("pzmiss",                      "MissingET.momentum.z[0]")
            .Define("missing_tlv",                 "ReconstructedParticle::get_tlv(MissingET)")
            .Define("etmiss",                      "sqrt((MissingET.momentum.x[0])*(MissingET.momentum.x[0]) + (MissingET.momentum.y[0])*(MissingET.momentum.y[0]))")
            
            #Visible mass
            .Define("visible_4vector",             "ReconstructedParticle::get_P4vis(ReconstructedParticles)")           

            #hzz monte carlo
            #---------------------------------------------------------------------------------------------------------------------------------------Truth about the data
            .Alias("Particle1",                    "Particle#1.index")
            .Define("hzz_decay",                   "MCParticle::fill_ZHZZ_decay(Particle, Particle1)")

            .Define("inv_mass_Z",                  "MCParticle::invariant_mass(hzz_decay.Z_decay)")
            .Define("pdg_Z",                       "MCParticle::get_pdg(hzz_decay.Z_decay)")
            .Define("Z_true_p",                    "MCParticle::get_p(hzz_decay.Z_decay)")
            .Define("Z_true_e",                    "MCParticle::get_e(hzz_decay.Z_decay)")
            .Define("Z_true_m",                    "MCParticle::get_mass(hzz_decay.Z_decay)")

            .Define("inv_mass_Z1",                 "MCParticle::invariant_mass(hzz_decay.Z1_decay)")
            .Define("pdg_Z1",                      "MCParticle::get_pdg(hzz_decay.Z1_decay)")
            .Define("Z1_true_p",                   "MCParticle::get_p(hzz_decay.Z1_decay)")
            .Define("Z1_true_e",                   "MCParticle::get_e(hzz_decay.Z1_decay)")
            .Define("Z1_true_m",                   "MCParticle::get_mass(hzz_decay.Z1_decay)")

            .Define("inv_mass_Z2",                 "MCParticle::invariant_mass(hzz_decay.Z2_decay)")
            .Define("pdg_Z2",                      "MCParticle::get_pdg(hzz_decay.Z2_decay)")
            .Define("Z2_true_p",                   "MCParticle::get_p(hzz_decay.Z2_decay)")
            .Define("Z2_true_e",                   "MCParticle::get_e(hzz_decay.Z2_decay)")
            .Define("Z2_true_m",                   "MCParticle::get_mass(hzz_decay.Z2_decay)")
            
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------

            )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            
            #-------------------------------------------------------------------------------------------Photons
           
            "N_photons",
            "photons_recoil_m",
            "photons_tlv",
            
            #-------------------------------------------------------------------------------------------Leptons

	        #Preselected leptons
            "N_on_muons",
	        "N_on_electrons",
	        "N_on_leptons",
	        "N_other_muons",
	        "N_other_electrons",
	        "N_other_leptons",
	        "on_muons_tlv",
	        "on_electrons_tlv",
	        "on_leptons_tlv",
	        "other_muons_tlv",
	        "other_electrons_tlv",
	        "other_leptons_tlv",

       	    "N_on_Z_leptons",
       	    "on_Z_leptons_recoil_m",
	        "on_Z_leptons_tlv",
       	    
       	    "N_on_extra_leptons",
       	    "on_extra_leptons_recoil_m",
	        "on_extra_leptons_tlv",
       	    
       	    "N_other_Z_leptons",
       	    "other_Z_leptons_recoil_m",
	        "other_Z_leptons_tlv",
       	    
       	    "N_other_extra_leptons",
       	    "other_extra_leptons_recoil_m",
	        "other_extra_leptons_tlv",
	    
	        "all_Z_leptons",
	        "N_all_Z_leptons",
	        "all_Z_leptons_tlv",

            #-------------------------------------------------------------------------------------------------Z
		
 	        "N_on_Z_leptonic",
 	        "on_Z_leptonic_recoil_m",                       
	        "on_Z_leptonic_tlv",
		
	        "N_other_Z_leptonic",
 	        "other_Z_leptonic_recoil_m",                       
	        "other_Z_leptonic_tlv",
            
            #----------------------------------------------------------------------------------------------Jets
            
            #N=2
            "jets_px2",
            "jets_py2",
            "jets_pz2",
            "jets_p2",
            "jets_e2",
	        "jets_m2",
            "jets_pt2",
            "jets_y2",
            "jets_eta2",
            "jets_theta2",
            "jets_phi2",
            "jetconstituents_ee_genkt2",
            "jetconstituents_ee_2",
            "jetconstituents_2",
            "dmerge_2_45",
            "dmerge_2_34",
            "dmerge_2_23",
            "dmerge_2_12",
            
            #N=3
            "jets_px3",
            "jets_py3",
            "jets_pz3",
            "jets_p3",
            "jets_e3",
            "jets_m3",
            "jets_pt3",
            "jets_y3",
            "jets_eta3",
            "jets_theta3",
            "jets_phi3",
            "jetconstituents_ee_genkt3",
            "jetconstituents_ee_3",
            "jetconstituents_3",
            "dmerge_3_45",
            "dmerge_3_34",
            "dmerge_3_23",
            "dmerge_3_12",
            
            #N=4
            "jets_px4",
            "jets_py4",
            "jets_pz4",
            "jets_p4",
            "jets_e4",
            "jets_m4",
            "jets_pt4",
            "jets_y4",
            "jets_eta4",
            "jets_theta4",
            "jets_phi4",
            "jetconstituents_ee_genkt4",
            "jetconstituents_ee_4",
            "jetconstituents_4",
            "dmerge_4_45",
            "dmerge_4_34",
            "dmerge_4_23",
            "dmerge_4_12",

            #-----------------------------------------------------------------------------Missing/Visible variables
            
            #Missing
            "emiss",
            "etmiss",
            "pxmiss",
            "pymiss",
            "pzmiss",
            "missing_tlv",
            
            #Visible
            "visible_4vector",
            
            #---------------------------------------------------------------------------------------Monte-Carlo

            #hzz monte carlo
            "hzz_decay",

            "inv_mass_Z",
            "pdg_Z",
            "Z_true_p",
            "Z_true_e",
            "Z_true_m",

            "inv_mass_Z1",
            "pdg_Z1",
            "Z1_true_p",
            "Z1_true_e",
            "Z1_true_m",

            "inv_mass_Z2",
            "pdg_Z2",
            "Z2_true_p",
            "Z2_true_e",
            "Z2_true_m"

            #--------------------------------------------------------------------------------------------------
        

            ]

        return branchList
