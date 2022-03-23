'''
This script adds the upload month to the text_df
it should be run in the same folder as txt_df.csv and metadata_month.csv
- those 2 dfs can be deleted after

This script should be repeated for all channels, then the dfs will be combined

You only need to change the channel variable
'''

import pandas as pd

channel = 'CGTN'

out_file = 'df_'+channel+'.csv'

df = pd.read_csv('txt_df.csv')
meta_df = pd.read_csv('metadata_month.csv')
# insert the month month from metadata into the new df
df.insert(1, 'month', meta_df['month'], allow_duplicates=True)

print(df)

df.to_csv(out_file, encoding='utf8', index=False)
