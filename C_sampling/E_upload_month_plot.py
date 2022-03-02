'''
This script creates a simple line graph showing the distribution of
video uploads per channel per month
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('upload_month_distribution.csv')

df = df.pivot(index='month', columns='channel_title', values='size')

df.plot(lw=2,
        colormap='twilight_shifted',
        title='Distribution of video uploads by month')
plt.xlabel('Month of upload')
plt.ylabel('Uploads')
plt.legend(loc='upper left', title='News Channel', ncol=3)
plt.show()

'''
In my case the distribution was fairly even

Some months were under represented due to a lack of uploads
in certain months.

some months were over represented, but that reflected the number 
of uploads in that month (e.g. i24 News in Aug 2021)
'''
