import pandas as pd
'''
This script links individual dataframes into one.
Here individual monthly files are concatenated
This could be edited to link channel dataframes together too
'''

# output filename
csv_out = 'Arirang_News_2021.csv'

# input the individual filenames extracted from the YouTube Data API
df1 = pd.read_csv('Arirang_News_1.csv')
df2 = pd.read_csv('Arirang_News_2.csv')
df3 = pd.read_csv('Arirang_News_3.csv')
df4 = pd.read_csv('Arirang_News_4.csv')
df5 = pd.read_csv('Arirang_News_5.csv')
df6 = pd.read_csv('Arirang_News_6.csv')
df7 = pd.read_csv('Arirang_News_7.csv')
df8 = pd.read_csv('Arirang_News_8.csv')
df9 = pd.read_csv('Arirang_News_9.csv')
df10 = pd.read_csv('Arirang_News_10.csv')
df11 = pd.read_csv('Arirang_News_11.csv')
df12 = pd.read_csv('Arirang_News_12.csv')

frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

# merge dfs. ignore_index=True stops index column showing original values
df_out = pd.concat(frames, ignore_index=True)

# delete original index column
df_out.drop(df_out.columns[0], axis=1, inplace=True)

df_out.to_csv(csv_out, encoding='utf8')
