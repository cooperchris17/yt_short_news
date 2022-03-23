'''
This script takes the [channel]_metadata_sample_2.csv as input
it creates a new column with the upload month and orders the data by 'video_id'
this is the same as the txt_df in the previous script
- so the month column can be added on (in the next script)

You only need to change the channel variable
'''

import pandas as pd

channel = 'CGTN'

# read in the metadata csv to get the upload month
df = pd.read_csv(channel+'_metadata_sample_2.csv')
# create a new column extracting the month from 'published_at'
df['month'] = pd.DatetimeIndex(df['published_at']).month
# sort by video_id, so it is the same order as the new df
df_sorted = df.sort_values(by=['video_id'])

print(df_sorted)

df_sorted.to_csv('metadata_month.csv', encoding='utf8', index=False)
