'''
This script prepares the data for the Scattertext interactive visulization
It filters data from the whole corpus csv file ('world_news_720_df.csv')
and amends the video_id to a YouTube URL
The output is a 3-column dataframe with the following columns:
'channel', 'url', 'text'
'''

import pandas as pd

#specify the 2 channel names as they are written in the world_news_720_df
channel_1_in_df = 'Nippon TV (JP)'
channel_2_in_df = 'Arirang News (KR)'
#input the country codes for the output filename
country_codes = 'JP_KR'

# read in the csv
df = pd.read_csv('world_news_720_df.csv')
# create a filtered df for each channel
df1 = df[df['channel'] == channel_1_in_df]
df2 = df[df['channel'] == channel_2_in_df]
# combine the dfs together to give a df with the data for 2 channels
frames = [df1, df2]
df3 = pd.concat(frames, ignore_index=True)

# create a list of URLs from the video IDs
url =[]
for id in df3['video_id']:
    url.append('youtube.com/watch?v='+id)
# Insert the list of URLs as a column in the dataframe
df3.insert(1, 'url', url)
# drop the unwanted columns
df4 = df3.drop(columns=['month', 'video_id'])
# print the output to check
print(df4)
# output the df to a csv file
df4.to_csv(country_codes+'_st.csv', encoding='utf8', index=False)
