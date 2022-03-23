'''
This script takes the '490_sample_metadata.csv' file as input
- to resample and get the data in this format follow the files in C_sampling:
/B_pandas_sample.py (amend to reflect sample size)
+ /C_combine_df.py (amend as necessary)
+ /F_add_filename_column.py
+ /G_delete_non_sample_files.py (this is to delete unwanted .txt files)

This script extracts the upload month from the uploaded date/time
It adds a column with the YouTube URL for each video (replacing the video_id)
And the channel names are amended, so users can see the channel name and country code
The output is a 4 column dataframe:
'file', 'channel', 'month', 'url'
- the 'file' is necessary to link the metadata to txt files
- the other columns are the metadata I wanted to display in ShinyConc
'''

import pandas as pd

# read in the metadata csv to get the upload month
df = pd.read_csv('490_sample_metadata.csv')
# create a new column extracting the month from 'published_at'
df['month'] = pd.DatetimeIndex(df['published_at']).month
# sort by video_id, so it is the same order as the new df

url =[]

for id in df['video_id']:
    url.append('youtube.com/watch?v='+id)

df.insert(1, 'url', url)

df2 = df.rename(columns={'file_name': 'file', 'channel_title': 'channel'})

df3 = df2.filter(items=['file', 'channel', 'month', 'url'])

# Change the channel names so ShinyConc will show a coutry code for each channel
df3['channel'].replace({'ABC News': 'ABC News (US)', 'Al Jazeera English': 'Al Jazeera (QA)',
                'Arirang News': 'Arirang News (KR)', 'BBC News': 'BBC News (UK)',
                'CBC News': 'CBC News (CA)', 'CGTN': 'CGTN (CN)', 'CNA': 'CNA (SG)',
                'DW News': 'DW News (DE)', 'i24NEWS English': 'i24 News (IL)',
                'Nippon TV News 24 Japan': 'Nippon TV (JP)',
                'TVC News Nigeria': 'TVC News (NG)', 'WION': 'WION (IN)'},
                inplace=True)
print(df3)

df3.to_csv('shiny_conc_490_metadata.csv', encoding='utf8', index=False)
