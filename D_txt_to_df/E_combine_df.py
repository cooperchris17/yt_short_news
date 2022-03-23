'''
This script joins the individual channel dataframes together
the output is one csv file with the channel, upload month, video_id and full text
for all videos in the corpus
'''

import pandas as pd

csv_out = 'world_news_720_df.csv'

df1 = pd.read_csv('df_ABC_News.csv')
df2 = pd.read_csv('df_Al_Jazeera.csv')
df3 = pd.read_csv('df_Arirang_News.csv')
df4 = pd.read_csv('df_BBC_News.csv')
df5 = pd.read_csv('df_CBC_News.csv')
df6 = pd.read_csv('df_CGTN.csv')
df7 = pd.read_csv('df_CNA.csv')
df8 = pd.read_csv('df_DW_News.csv')
df9 = pd.read_csv('df_i24_News.csv')
df10 = pd.read_csv('df_Nippon_TV.csv')
df11 = pd.read_csv('df_TVC_News.csv')
df12 = pd.read_csv('df_WION.csv')

frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

# merge dfs. ignore_index=True stops index column showing original values
df_out = pd.concat(frames, ignore_index=True)

# delete original index column
# df_out.drop(df_out.columns[0], axis=1, inplace=True)

df_out.to_csv(csv_out, encoding='utf8', index=False)
