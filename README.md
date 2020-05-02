
# Computational Neuroscience Project Skeleton

This repository is a skeleton Python package that students in PSYC 5270 can use to get started on their data exploration assignments.

## Getting started

Start by cloning the repository: `git clone https://github.com/melizalab/comp-neurosci-skeleton.git`

This will create a new directory, `comp-neurosci-skeleton`, containing the following items:

- `README.md`: this file
- `setup.py`:  package description file. You will need to edit this.
- `requirements.txt`: a list of packages your code depends on
- `.gitignore`: a list of files git will ignore when telling you what's changed
- `src`:       a directory where you will put your python code
- `test`:      a directory where you will put test code
- `data`:      a directory where your data will live
- `build`:     a directory where processed output from your analysis will live

Choose a new name for your package. For the PSYC 5270 assignment, use something like `crcns-datasetid-computingid`. Rename the top-level directory (`comp-neurosci-skeleton`) and edit `setup.py` to set the new name and other identifying information.

Now you need to create a github repository of your own. Go to [https://github.com/new](https://github.com/new). Give the repository your chosen name and a description, then click Create Repository. **DO NOT** check the box to initialize the repository with a readme. Ignore the instructions on how to set up your repository, but make a note of the address. It will look something like `https://github.com/dmeliza/dummy.git`

Finally, set your local directory to track the github repository by running the following commands in your working directory. Replace the repository address in the code below with the one for your project.

``` shell
git remote rm origin
git remote add origin https://github.com/dmeliza/dummy.git
git push -u origin master
```

If you get an error on the last command, it's probably because you let github initialize your repository. You'll have to delete and re-create the repository on github and then run the last command again.

## Next steps

Edit `data/README.md` to describe how to retrieve data. Better yet, write a script.

Edit `requirements.txt` to add any needed dependencies, then create a virtual environment and install the dependencies as follows:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Alternatively, if you're using anaconda, create a new environment and run the following to install dependencies:

``` shell
conda install git numpy scipy pandas matplotlib notebook
```

Install the project in development mode by running `python setup.py develop`. If you use notebooks, this will ensure that you can access your modules.

Edit this file to describe your actual project.

## pvc-7 data exploration project instructions:

Aim: explore how spatial and temporal frequency affect direction tuning.

Hypothesis: direction tuning intensity is stronger in specific spatial and temporal frequency.

Steps for the analysis:

1. load the dataset
   
   hdf5 format, 3D matrix (255256, 512, 1154) of light intensity

2. open the stimulus.csv as integer, so the values can be used in the function to calculate df/f.

3. pick a ROI. The rectangle matrix [jstart:jend,kstart:kend] is defined as ROI.

4. define the function to aquire df/f for a neuron [jstart:jend,kstart:kend]

5. create stimuli sets for spatial frequency and temporal frequency, for later use in for loops.

6. For each neuron, repeat the steps as follows 

 (1) create a dataframe (DFneuroni) for ROI = [jstart:jend,kstart:kend]. shape=(1600,7)
 (2) create a grouped dataframe (groupedDFi) of the neuron's dff under 5sf*5tf condition.
 (3) update groupedDF. let groupedDF represent the current neuron.
 (4) plot direction tuning under different spatial frequencies, merged across temporal frequencies
 (5) plot direction tuning under different temporal frequencies, merged across spatial frequencies
 (6) plot direction tuning under 5 sf * 5 tf combinations.
 (7) plot direction tuning under 5 sf * 5 tf combinations, using polar diagram


7. define a function DSI_calculation to calculate DSI under 5sf * 5tf conditions.

8. generate a long dataframe, containing each neuron's DSI under 5sf * 5tf

9. statictical analysis, using one-way ANOVA
   
   unit of analysis: cell; dependent variable: DSI 

 (1) based on the literature, pick tf = 4 and test the difference across sf.
 (2) based on the literature, pick sf = 0.04 and test the difference across tf.

10. calculate the mean DSI for 5sf * 5tf conditions, to be used in bar plots. 

11. generate bar plots for the two the one-way ANOVAs

Notes:

Since the sixth step for each neuron is the same and that it tooks half an hour to generate df/f for each neuron, I only choose 5 neurons to demonstrate. I guess the reason it took 30 min is because 1） I put the data in an external hard drive and 2) that the 8g memory of my laptop is below the demand of this task.

Appendix 

cell coordinates
cell1 [240:255, 360:380] -- my neuron 1
cell2 [255:270, 340:360]
cell3 [195:212, 180:210]
cell4 [135:145, 325:345] -- my neuron 4
cell5 [210:223; 320:340]
cell6 [160:175, 340:360]
cell7 [310:325, 400:420]
cell8 [329:340,467:486]
cell9 [200:215, 260:280]
cell10 [140:152,397:420]
cell11 [168:181,315:333] -- my neuron 2
cell12 [342:355,255:272] -- my neuron 3
cell13 [182:190,265:278] -- my neuron 5
cell14 [240:250, 180:195]
cell15 [228:245,248:260]
cell16 [272:284,248:267]
cell17 [125:142,142:168]
cell18 [297:307,364:378]



Future attempts:

1. before calculateing DSI, fit each direction tuning response using Gaussian function,

2. in order to pick out the cells that do have direction tuning properties, set a threshold (DSI = 0.7). this would remove the non-direction-selective cells, so that the effect of sf/tf on DSI would more likely be revealed.



