'''
This script creates a dataframe showing video uploads per channel
per month, it is output as a csv file
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read in the dataframe from csv file
df = pd.read_csv('Twelve_Channels_2021.csv')
# create a new column extracting the month from 'published_at'
df['month'] = pd.DatetimeIndex(df['published_at']).month
# print 3 relevant columns of df

#group the data by the channel and month and count the number of uploads per month
df2 = df.groupby(['channel_title', 'month']).size().to_frame('size')

print(df2)

df2.to_csv('upload_month_distribution.csv', encoding='utf8')
