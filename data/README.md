
Edit this file to describe how to retrieve the data set. Except for very small data files, it's not recommended to check data into version control.

# code to retrieve the response data

f=h5py.File('data/PVC-7/concat_31Hz.h5','r')
ls = list(f)
print('List of datasets in this file: \n',ls)
dset = f['data']
print('dset',dset.shape)

# code to read in the stimulus.csv as integer

df = pd.read_csv('data/PVC-7/122008_140124_windowmix/stimulus.csv').astype(int)
df.columns = ["start","end","ori","sf","tf","contrast"]
stimuli = np.array(df[["start","end","ori","sf","tf","contrast"]])
print(stimuli)
stimuli.dtype
stimuli.shape

# code to read in the stimulus.csv as dataframe

DF = pd.read_csv('data/PVC-7/122008_140124_windowmix/stimulus.csv')

