'''
This script combines the monthly metadata to check the monthly upload_month_distribution
'''

import pandas as pd

csv_out = 'Twelve_Channels_2021.csv'

df1 = pd.read_csv('ABC_News_transcript_metadata.csv')
df2 = pd.read_csv('Al_Jazeera_transcript_metadata.csv')
df3 = pd.read_csv('Arirang_News_transcript_metadata.csv')
df4 = pd.read_csv('BBC_News_transcript_metadata.csv')
df5 = pd.read_csv('CBC_News_transcript_metadata.csv')
df6 = pd.read_csv('CGTN_transcript_metadata.csv')
df7 = pd.read_csv('CNA_transcript_metadata.csv')
df8 = pd.read_csv('DW_News_transcript_metadata.csv')
df9 = pd.read_csv('i24_News_transcript_metadata.csv')
df10 = pd.read_csv('Nippon_TV_transcript_metadata.csv')
df11 = pd.read_csv('TVC_News_transcript_metadata.csv')
df12 = pd.read_csv('WION_transcript_metadata.csv')

frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

# merge dfs. ignore_index=True stops index column showing original values
df_out = pd.concat(frames, ignore_index=True)

# delete original index column
df_out.drop(df_out.columns[0], axis=1, inplace=True)

df_out.to_csv(csv_out, encoding='utf8')
