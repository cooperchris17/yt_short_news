'''
This script deletes all files in the folder that are not listed
in the [channel]_metadata_sample_2
The [channel]_metadata_sample_2 file should be in the folder too

I ran the script for each channel individually in case of errors
Only need to change the channel variable

It is highly recommended to run this script on a copy of the original
files (in case of any mistakes)
'''

import os, glob
import pandas as pd
# this is the only variable that need to be changed
channel = 'ABC_News'

df = pd.read_csv(channel+'_metadata_sample_2.csv')

file_names = [f for f in df['file_name']]

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            if file not in file_names:
                os.remove(file)
