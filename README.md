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

''' 
source setup.sh
fccanalysis build 
'''

# stage1X




