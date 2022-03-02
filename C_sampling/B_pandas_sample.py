'''
This script randomly samples 720 lines in each metadata file using pandas
The output csv has no index column
You only need to change the news_channel name if previous naming steps were followed
'''

import pandas as pd
# change the channel name here
channel_name = 'i24_News'
# read in the csv file
df = pd.read_csv(channel_name+'_transcript_metadata.csv', index_col=0)
# change the number here to change the sample size
df2 = df.sample(n=720)
# output the sample to a csv file
df2.to_csv(channel_name+'_metadata_sample.csv', encoding='utf8', index=False)
