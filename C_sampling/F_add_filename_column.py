'''
Add a column to the metadata dataframe listing the file names
- this is necessary so unwanted files can be deleted
Just need to change the channel and short_channel variables
the output is saved to a new csv file
'''

import pandas as pd

channel = 'WION'
short_channel = 'WION_'

df = pd.read_csv(channel+'_metadata_sample.csv')

file_name =[]

for id in df['video_id']:
    file_name.append(short_channel+id+'.txt')

df.insert(2, 'file_name', file_name)
df.to_csv(channel+'_metadata_sample_2.csv', encoding='utf8')
