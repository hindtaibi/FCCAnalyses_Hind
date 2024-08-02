import ROOT

#This file is used to sum the the signals and backgrounds
#Takes an output of finalAA as input
#It is to be used before performing Combine (fit)

inputDir = 'outputs/'
outputDir = 'outputssum/'

samples = [#Signal
	       #'wzp6_ee_mumuH_HZZ_ecm240',   
           'wzp6_ee_eeH_HZZ_ecm240',     
           'wzp6_ee_nunuH_HZZ_ecm240',   
           'wzp6_ee_qqH_HZZ_ecm240',
           'wzp6_ee_ssH_HZZ_ecm240',
           'wzp6_ee_bbH_HZZ_ecm240',
           'wzp6_ee_ccH_HZZ_ecm240',
           #Background
           'wzp6_ee_mumuH_HWW_ecm240',
           'wzp6_ee_mumuH_HZa_ecm240',
           'wzp6_ee_mumuH_Hbb_ecm240',
           'wzp6_ee_mumuH_Hcc_ecm240',
           'wzp6_ee_mumuH_Hmumu_ecm240',
           'wzp6_ee_mumuH_Hss_ecm240',
           'wzp6_ee_mumuH_Htautau_ecm240',
           'wzp6_ee_eeH_HWW_ecm240',
           'wzp6_ee_eeH_HZa_ecm240',
           'wzp6_ee_eeH_Hbb_ecm240',
           'wzp6_ee_eeH_Hcc_ecm240',
           'wzp6_ee_eeH_Hmumu_ecm240',
           'wzp6_ee_eeH_Hss_ecm240',
           'wzp6_ee_eeH_Htautau_ecm240',
           'p8_ee_ZZ_ecm240',
           'p8_ee_WW_ecm240'
           ]

signals = [#'wzp6_ee_mumuH_HZZ_ecm240',
           'wzp6_ee_eeH_HZZ_ecm240',
           'wzp6_ee_nunuH_HZZ_ecm240',
           'wzp6_ee_qqH_HZZ_ecm240',
           'wzp6_ee_ssH_HZZ_ecm240',
           'wzp6_ee_bbH_HZZ_ecm240',
           'wzp6_ee_ccH_HZZ_ecm240']

samplesHWW = [#'wzp6_ee_mumuH_HWW_ecm240',
              'wzp6_ee_eeH_HWW_ecm240']

samplesHqq = [#'wzp6_ee_mumuH_Hbb_ecm240', 
              'wzp6_ee_eeH_Hbb_ecm240',
              'wzp6_ee_mumuH_Hss_ecm240',
              'wzp6_ee_eeH_Hss_ecm240',
              'wzp6_ee_mumuH_Hcc_ecm240',
              'wzp6_ee_eeH_Hcc_ecm240']

samplesHmumu = [#'wzp6_ee_mumuH_Hmumu_ecm240', 
                'wzp6_ee_eeH_Hmumu_ecm240']

samplesHtautau = [#'wzp6_ee_mumuH_Htautau_ecm240',
                  'wzp6_ee_eeH_Htautau_ecm240']

samplesHZa = [#'wzp6_ee_mumuH_HZa_ecm240', 
              'wzp6_ee_eeH_HZa_ecm240']

samplesHgg = ['wzp6_ee_mumuH_Hgg_ecm240']

samplesZZ = ['p8_ee_ZZ_ecm240'],

samplesWW = ['p8_ee_WW_ecm240']


#Selections we intend to use for the fit
sels = ["region1"]

#Vatiabes we want to use for the fit
variables = ["Z1_recoil_m_fit"]

def main():
    
    for v in variables:
        print("_____________________________________ Variable:",v)
        #----------------------------------------------------------------------------------------------------------Signal

        for sel in sels:
    
            #We start with the 1st sample
            f = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_{sel}_histo.root")
            hf = f.Get(v)
   
            #We add all the signal samples
            for s in signals : 
                f1 = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1 = f1.Get(v)
                hf.Add(hf1, 1)
    
            #We multiply by the luminosity
            hf = 5*10**(6)*hf
            print("Signal", sel, "=", hf.Integral())

            filesignalregion1 = ROOT.TFile.Open(f"{outputDir}SumSignal_{sel}_{v}.root", "RECREATE")
            filesignalregion1.WriteObject(hf, v)

        #----------------------------------------------------------------------------------------------------------All samples

        for sel in sels:

            fS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_{sel}_histo.root")
            hfS = fS.Get(v)

            for s in samples : 
                f1S = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1S = f1S.Get(v)
                hfS.Add(hf1S, 1)

            hfS = 5*10**(6)*hfS
            print("Sum", sel, "=", hfS.Integral())

            filesumregion1 = ROOT.TFile.Open(f"{outputDir}Sum_{sel}_{v}.root", "RECREATE")
            filesumregion1.WriteObject(hfS, v)

        #----------------------------------------------------------------------------------------------------------HWW

        for sel in sels:
    
            fHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_{sel}_histo.root")
            hfHWW = fHWW.Get(v)
    
            for s in samplesHWW : 
                f1HWW = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1HWW = f1HWW.Get(v)
                hfHWW.Add(hf1HWW, 1)

            hfHWW = 5*10**(6)*hfHWW
            print("HWW", sel, "=", hfHWW.Integral())

            fileHWWregion1 = ROOT.TFile.Open(f"{outputDir}SumHWW_{sel}_{v}.root", "RECREATE")
            fileHWWregion1.WriteObject(hfHWW, v)

        #----------------------------------------------------------------------------------------------------------Hqq

        for sel in sels:

            fHqq = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_{sel}_histo.root")
            hfHqq = fHqq.Get(v)
    
            for s in samplesHqq : 
                f1Hqq = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1Hqq = f1Hqq.Get(v)
                hfHqq.Add(hf1Hqq, 1)

            hfHqq = 5*10**(6)*hfHqq
            print("Hqq", sel, "=", hfHqq.Integral())

            fileHqqregion1 = ROOT.TFile.Open(f"{outputDir}SumHqq_{sel}_{v}.root", "RECREATE")
            fileHqqregion1.WriteObject(hfHqq, v)
    
        #----------------------------------------------------------------------------------------------------------Hmumu

        for sel in sels:

            fHmumu = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hmumu_ecm240_{sel}_histo.root")
            hfHmumu = fHmumu.Get(v)
    
            for s in samplesHmumu : 
                f1Hmumu = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1Hmumu = f1Hmumu.Get(v)
                hfHmumu.Add(hf1Hmumu, 1)

            hfHmumu = 5*10**(6)*hfHmumu  
            print("Hmumu", sel, "=", hfHmumu.Integral())

            fileHmumuregion1 = ROOT.TFile.Open(f"{outputDir}SumHmumu_{sel}_{v}.root", "RECREATE")
            fileHmumuregion1.WriteObject(hfHmumu, v)
    
        #----------------------------------------------------------------------------------------------------------Htautau

        for sel in sels:

            fHtautau = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_{sel}_histo.root")
            hfHtautau = fHtautau.Get(v)
    
            for s in samplesHtautau :
                f1Htautau = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1Htautau = f1Htautau.Get(v)
                hfHtautau.Add(hf1Htautau, 1)

            hfHtautau = 5*10**(6)*hfHtautau
            print("Htautau", sel, "=", hfHtautau.Integral())

            fileHtautauregion1 = ROOT.TFile.Open(f"{outputDir}SumHtautau_{sel}_{v}.root", "RECREATE")
            fileHtautauregion1.WriteObject(hfHtautau, v)

        #----------------------------------------------------------------------------------------------------------HZa
        
        for sel in sels:

            fHZa = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZa_ecm240_{sel}_histo.root")
            hfHZa = fHZa.Get(v)
    
            for s in samplesHZa :
                f1HZa = ROOT.TFile.Open(f"{inputDir}{s}_{sel}_histo.root")
                hf1HZa = f1HZa.Get(v)
                hfHZa.Add(hf1HZa, 1)

            hfHZa = 5*10**(6)*hfHZa
            print("HZa", sel, "=", hfHZa.Integral())

            fileHZaregion1 = ROOT.TFile.Open(f"{outputDir}SumHZa_{sel}_{v}.root", "RECREATE")
            fileHZaregion1.WriteObject(hfHZa, v)

        #----------------------------------------------------------------------------------------------------------Hgg

        for sel in sels:

            fHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_{sel}_histo.root")
            hfHgg = fHgg.Get(v)

            hfHgg = 5*10**(6)*hfHgg
            print("Hgg", sel, "=", hfHgg.Integral())

            fileHggregion1 = ROOT.TFile.Open(f"{outputDir}SumHgg_{sel}_{v}.root", "RECREATE")
            fileHggregion1.WriteObject(hfHgg, v)

        #----------------------------------------------------------------------------------------------------------ZZ
        
        for sel in sels:
            
            fZZ = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_{sel}_histo.root")
            hfZZ = fZZ.Get(v)

            hfZZ = 5*10**(6)*hfZZ
            print("ZZ", sel, "=", hfZZ.Integral())

            fileZZregion1 = ROOT.TFile.Open(f"{outputDir}SumZZ_{sel}_{v}.root", "RECREATE")
            fileZZregion1.WriteObject(hfZZ, v)

        #----------------------------------------------------------------------------------------------------------WW

        for sel in sels:

            fWW = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_{sel}_histo.root")
            hfWW = fWW.Get(v)

            hfWW = 5*10**(6)*hfWW
            print("WW", sel, "=", hfWW.Integral())

            fileWWregion1 = ROOT.TFile.Open(f"{outputDir}SumWW_{sel}_{v}.root", "RECREATE")
            fileWWregion1.WriteObject(hfWW, v)



if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
