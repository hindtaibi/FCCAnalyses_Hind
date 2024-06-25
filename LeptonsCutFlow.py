#Mandatory: List of processes

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
            .Define("photons",              "ReconstructedParticle::get(Photon0, ReconstructedParticles)")

            #We collect information about the photons
            
            .Define("muons_p",              "ReconstructedParticle::get_p(muons)")
            .Define("electrons_p",          "ReconstructedParticle::get_p(electrons)")
            .Define("photons_p",            "ReconstructedParticle::get_p(photons)")
		
	    .Filter("muons_p > 5 && electrons_p > 5")

            

            )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            
            "muons_p",
            "electrons_p",
            "photons_p"
        
            ]

        return branchList
