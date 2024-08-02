import ROOT

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



sels = ["region1", "region2"]

variables = ["Z1_recoil_m", "Z2_p"]

def main():
    
    for v in variables:
        print("_____________________________________ Variable:",v)
        #----------------------------------------------------------------------------------------------------------Signal
    
        #We start with the 1st sample
        f = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_region1_histo.root")
        g = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_region2_histo.root")
        hf = f.Get(v)
        hg = g.Get(v)
   
        #We add all the signal samples
        for s in signals : 
            f1 = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1 = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1 = f1.Get(v)
            hg1 = g1.Get(v)
            hf.Add(hf1, 1)
            hg.Add(hg1, 1)
    
        #We multiply by the luminosity
        hf = 5*10**(6)*hf
        print("Signal region 1 =", hf.Integral())
        hg = 5*10**(6)*hg
        print("Signal region 2 =", hg.Integral())

        filesignalregion1 = ROOT.TFile.Open(f"{outputDir}SumSignal_region1_{v}.root", "RECREATE")
        filesignalregion1.WriteObject(hf, v)
        filesignalregion2 = ROOT.TFile.Open(f"{outputDir}SumSignal_region2_{v}.root", "RECREATE")
        filesignalregion2.WriteObject(hg, v)

        #----------------------------------------------------------------------------------------------------------All samples

        fS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_region1_histo.root")
        gS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_region2_histo.root")
        hfS = fS.Get(v)
        hgS = gS.Get(v)

        for s in samples : 
            f1S = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1S = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1S = f1S.Get(v)
            hg1S = g1S.Get(v)
            hfS.Add(hf1S, 1)
            hgS.Add(hg1S, 1)

        hfS = 5*10**(6)*hfS
        print("Sum region 1 =", hfS.Integral())
        hgS = 5*10**(6)*hgS
        print("Sum region 2 =", hgS.Integral())

        filesumregion1 = ROOT.TFile.Open(f"{outputDir}Sum_region1_{v}.root", "RECREATE")
        filesumregion1.WriteObject(hfS, v)
        filesumregion2 = ROOT.TFile.Open(f"{outputDir}Sum_region2_{v}.root", "RECREATE")
        filesumregion2.WriteObject(hgS, v)

        #----------------------------------------------------------------------------------------------------------HWW
    
        fHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_region1_histo.root")
        gHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_region2_histo.root")
        hfHWW = fHWW.Get(v)
        hgHWW = gHWW.Get(v)
    
        for s in samplesHWW : 
            f1HWW = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1HWW = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1HWW = f1HWW.Get(v)
            hg1HWW = g1HWW.Get(v)
            hfHWW.Add(hf1HWW, 1)
            hgHWW.Add(hg1HWW,1)

        hfHWW = 5*10**(6)*hfHWW
        print("HWW region 1 =", hfHWW.Integral())
        hgHWW = 5*10**(6)*hgHWW
        print("HWW region 2 =", hgHWW.Integral())

        fileHWWregion1 = ROOT.TFile.Open(f"{outputDir}SumHWW_region1_{v}.root", "RECREATE")
        fileHWWregion1.WriteObject(hfHWW, v)
        fileHWWregion2 = ROOT.TFile.Open(f"{outputDir}SumHWW_region2_{v}.root", "RECREATE")
        fileHWWregion2.WriteObject(hgHWW, v)

        #----------------------------------------------------------------------------------------------------------Hqq

        fHqq = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_region1_histo.root")
        gHqq = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_region2_histo.root")
        hfHqq = fHqq.Get(v)
        hgHqq = gHqq.Get(v)
    
        for s in samplesHqq : 
            f1Hqq = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1Hqq = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1Hqq = f1Hqq.Get(v)
            hg1Hqq = g1Hqq.Get(v)
            hfHqq.Add(hf1Hqq, 1)
            hgHqq.Add(hg1Hqq, 1)

        hfHqq = 5*10**(6)*hfHqq
        print("Hqq region 1 =", hfHqq.Integral())
        hgHqq = 5*10**(6)*hgHqq
        print("Hqq region 2 =", hgHqq.Integral())

        fileHqqregion1 = ROOT.TFile.Open(f"{outputDir}SumHqq_region1_{v}.root", "RECREATE")
        fileHqqregion1.WriteObject(hfHqq, v)
        fileHqqregion2 = ROOT.TFile.Open(f"{outputDir}SumHqq_region2_{v}.root", "RECREATE")
        fileHqqregion2.WriteObject(hgHqq, v)
    
        #----------------------------------------------------------------------------------------------------------Hmumu

        fHmumu = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hmumu_ecm240_region1_histo.root")
        gHmumu = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hmumu_ecm240_region2_histo.root")
        hfHmumu = fHmumu.Get(v)
        hgHmumu = gHmumu.Get(v)
    
        for s in samplesHmumu : 
            f1Hmumu = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1Hmumu = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1Hmumu = f1Hmumu.Get(v)
            hg1Hmumu = g1Hmumu.Get(v)
            hfHmumu.Add(hf1Hmumu, 1)
            hgHmumu.Add(hg1Hmumu,1)

        hfHmumu = 5*10**(6)*hfHmumu  
        print("Hmumu region 1 =", hfHmumu.Integral())
        hgHmumu = 5*10**(6)*hgHmumu
        print("Hmumu region 2 =", hgHmumu.Integral())

        fileHmumuregion1 = ROOT.TFile.Open(f"{outputDir}SumHmumu_region1_{v}.root", "RECREATE")
        fileHmumuregion1.WriteObject(hfHmumu, v)
        fileHmumuregion2 = ROOT.TFile.Open(f"{outputDir}SumHmumu_region2_{v}.root", "RECREATE")
        fileHmumuregion2.WriteObject(hgHmumu, v)
    
        #----------------------------------------------------------------------------------------------------------Htautau

        fHtautau = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_region1_histo.root")
        gHtautau = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_region2_histo.root")
        hfHtautau = fHtautau.Get(v)
        hgHtautau = gHtautau.Get(v)
    
        for s in samplesHtautau :
            f1Htautau = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1Htautau = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1Htautau = f1Htautau.Get(v)
            hg1Htautau = g1Htautau.Get(v)
            hfHtautau.Add(hf1Htautau, 1)
            hgHtautau.Add(hg1Htautau ,1)

        hfHtautau = 5*10**(6)*hfHtautau
        print("Htautau region 1 =", hfHtautau.Integral())
        hgHtautau = 5*10**(6)*hgHtautau
        print("Htautau region 2 =", hgHtautau.Integral())

        fileHtautauregion1 = ROOT.TFile.Open(f"{outputDir}SumHtautau_region1_{v}.root", "RECREATE")
        fileHtautauregion1.WriteObject(hfHtautau, v)
        fileHtautauregion2 = ROOT.TFile.Open(f"{outputDir}SumHtautau_region2_{v}.root", "RECREATE")
        fileHtautauregion2.WriteObject(hgHtautau, v)

        #----------------------------------------------------------------------------------------------------------HZa

        fHZa = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZa_ecm240_region1_histo.root")
        gHZa = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZa_ecm240_region2_histo.root")
        hfHZa = fHZa.Get(v)
        hgHZa = gHZa.Get(v)
    
        for s in samplesHZa :
            f1HZa = ROOT.TFile.Open(f"{inputDir}{s}_region1_histo.root")
            g1HZa = ROOT.TFile.Open(f"{inputDir}{s}_region2_histo.root")
            hf1HZa = f1HZa.Get(v)
            hg1HZa = g1HZa.Get(v)
            hfHZa.Add(hf1HZa, 1)
            hgHZa.Add(hg1HZa, 1)

        hfHZa = 5*10**(6)*hfHZa
        print("HZa region 1 =", hfHZa.Integral())
        hgHZa = 5*10**(6)*hgHZa
        print("HZa region 2 =", hgHZa.Integral())

        fileHZaregion1 = ROOT.TFile.Open(f"{outputDir}SumHZa_region1_{v}.root", "RECREATE")
        fileHZaregion1.WriteObject(hfHZa, v)
        fileHZaregion2 = ROOT.TFile.Open(f"{outputDir}SumHZa_region2_{v}.root", "RECREATE")
        fileHZaregion2.WriteObject(hgHZa, v)

        #----------------------------------------------------------------------------------------------------------Hgg

        fHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_region1_histo.root")
        gHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_region2_histo.root")
        hfHgg = fHgg.Get(v)
        hgHgg = gHgg.Get(v)

        hfHgg = 5*10**(6)*hfHgg
        print("Hgg region 1 =", hfHgg.Integral())
        hgHgg = 5*10**(6)*hgHgg
        print("Hgg region 2 =", hgHgg.Integral())

        fileHggregion1 = ROOT.TFile.Open(f"{outputDir}SumHgg_region1_{v}.root", "RECREATE")
        fileHggregion1.WriteObject(hfHgg, v)
        fileHggregion2 = ROOT.TFile.Open(f"{outputDir}SumHgg_region2_{v}.root", "RECREATE")
        fileHggregion2.WriteObject(hgHgg, v)

        #----------------------------------------------------------------------------------------------------------ZZ

        fZZ = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_region1_histo.root")
        gZZ = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_region2_histo.root")
        hfZZ = fZZ.Get(v)
        hgZZ = gZZ.Get(v)

        hfZZ = 5*10**(6)*hfZZ
        print("ZZ region 1 =", hfZZ.Integral())
        hgZZ = 5*10**(6)*hgZZ
        print("ZZ region 2 =", hgZZ.Integral())

        fileZZregion1 = ROOT.TFile.Open(f"{outputDir}SumZZ_region1_{v}.root", "RECREATE")
        fileZZregion1.WriteObject(hfZZ, v)
        fileZZregion2 = ROOT.TFile.Open(f"{outputDir}SumZZ_region2_{v}.root", "RECREATE")
        fileZZregion2.WriteObject(hgZZ, v)

        #----------------------------------------------------------------------------------------------------------WW

        fWW = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_region1_histo.root")
        gWW = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_region2_histo.root")
        hfWW = fWW.Get(v)
        hgWW = gWW.Get(v)

        hfWW = 5*10**(6)*hfWW
        print("WW region 1 =", hfWW.Integral())
        hgWW = 5*10**(6)*hgWW
        print("WW region 2 =", hgWW.Integral())

        fileWWregion1 = ROOT.TFile.Open(f"{outputDir}SumWW_region1_{v}.root", "RECREATE")
        fileWWregion1.WriteObject(hfWW, v)
        fileWWregion2 = ROOT.TFile.Open(f"{outputDir}SumWW_region2_{v}.root", "RECREATE")
        fileWWregion2.WriteObject(hgWW, v)







if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
