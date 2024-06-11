#This file aims to plot the energy of the photons and the missing energy in order to determine the first cuts to apply on this variables next

#Input directory where the files produced at the pre-selection level are
inputDir  = "../outputs/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs"

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},        #Signal
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
               'wzp6_ee_eeH_HZZ_ecm240':{},          #Signal
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

#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
#procDictAdd={"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

#Number of CPUs to use
nCPUS = 128

#produces ROOT TTrees, default is False
doTree = False
doScale = False


#Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {"sel0":"emiss > -10"   #No Cut
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    "emiss":          {"name":"emiss",          "title":"Missing energy [GeV]",               			 "bin":100,  "xmin":0,    "xmax":150}
}



    

