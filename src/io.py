# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import

# load the dataset
f=h5py.File('data/PVC-7/concat_31Hz.h5','r')
ls = list(f)
print('List of datasets in this file: \n',ls)
dset = f['data']
print('dset',dset.shape)

# f.close()

# open the stimulus.csv as integer

df = pd.read_csv('data/PVC-7/122008_140124_windowmix/stimulus.csv').astype(int)
df.columns = ["start","end","ori","sf","tf","contrast"]
stimuli = np.array(df[["start","end","ori","sf","tf","contrast"]])


# define the function to aquire df/f for a neuron [jstart:jend,kstart:kend] in each trial.
def dff_results(jstart,jend,kstart,kend):
    dff_mean_all= []
    for stimrow in stimuli[:,0]:
        F0=np.mean(dset[(stimrow-30):stimrow,jstart:jend,kstart:kend],axis=0)# baseline response: for each pixel, average across frames. 2D matrix
        F=np.mean(dset[stimrow:(stimrow+90),jstart:jend,kstart:kend],axis=0)# stumulus response: for each pixel, average across frames. 2D matrix
        dff = (F-F0)/F0 # 2D matrix
        dff_mean = np.mean(dff)# one df/f for each trial
        dff_mean_all = np.append(dff_mean_all,dff_mean)# an array of df/f for 1600 trials
    return dff_mean_all

# for a neuron, [jstart:jend,kstart:kend], DF is a an array of shape=(1600,1), containing the df/f in each trial. 

DF = pd.read_csv('data/PVC-7/122008_140124_windowmix/stimulus.csv')
DF.insert(6,'dff',dff_results(jstart:jend,kstart:kend)) 
print(DF)

