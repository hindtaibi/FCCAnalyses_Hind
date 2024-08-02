# Generalities
In this FCC-ee analysis, we are interested in the final states with 2 leptonic Z bosons (ZH &rarr; 4l + xx). Therefore, we have two possibilities concerning these leptonic Z bsosons. Indeed, we could have:
- two on shell leptonic Z bosons in the final state (case A), 
- one on shell and one off shell leptonic Z bosons in the final state (case B).

Case A is studied through the files in the stage1ter folder [here](https://github.com/hindtaibi/FCCAnalyses_Hind/tree/main/stage1ter) and case B is studied through the files in the stage1quater folder [here](https://github.com/hindtaibi/FCCAnalyses_Hind/tree/main/stage1quater). If you are wondering what happened to stage1 and stage1bis, they fell into the oblivion of unsuccessful attempts.  
The files must be run successively as follows:
- stage1X which takes as input the [simulated data](https://fcc-physics-events.web.cern.ch/FCCee/delphes/winter2023/idea/),
- stage2 which takes as input the output of stage1X,
- finalYZ which takes as input the output of stage2,
- plots YZ which takes as input the output of final YZ.

The use of each file is detailed below.

The preliminary source commands to use the FCCAnalyses framework are:

```
source setup.sh
fccanalysis build 
```

# FCCAnalyses
## stage1X
The main purpose of stage1ter and stage1quater is to reconstruct the leptonic Z bosons and jets and to gather the kinematic information to be used afterwards. stage1ter and stage1quater could be merged in one unique stage1 as their main purpose of the same but I chose to separate them in order to be able to run through the whole p8_ee_ZZ_ecm240 and p8_ee_WW_ecm240 data. Indeed, these file being quite heavy, it is difficult to save the entirety of the associated stage1 analysis. To get around this issue, filters were applied at the end of stage1:
- ```.Filter("on_Z_leptonic == 2 && other_Z_leptonic == 0")``` in stage1ter,
- ```.Filter("on_Z_leptonic == 1 && other_Z_leptonic == 1")``` in stage1quater.

The command to run stage1X:
```fccanalysis run stage1X```




