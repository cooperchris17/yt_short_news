'''
This script was used to create graphs showing the 15 most frequent proper nouns
in each channel (with normalised frequency and document percentage)

The variables to change are 'channel', 'title', 'scale_factor'
and the colors of the bars can be changed in lines 36-37
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# created with the help of:
# https://stackoverflow.com/questions/51994537/equivalent-of-secondary-y-for-barh-in-pandas-matplotlib

channel = 'Nippon_TV'
title = 'Nippon TV (JP): Proper Nouns'
# knock 2 zeros off the highest frequency (per million) to get 100% on doc_freq axis
# e.g if highest frequency is 7000 per million, scale_factor = 70
scale_factor = 70

df = pd.read_csv(channel+'_ner_frequency.csv')
# sometimes words that were not proper nouns (e.g. 'the') were included
# this line of code was used to drop those lines from the graph (by index number of the row)
df2 = df.drop(df.index[12])
df3 = df2.drop(df2.index[14])
df_15 = df3[0:15]

fig, ax = plt.subplots(figsize=(5,7))

font_dict = {'fontsize': 20}

y_pos = np.arange(len(df_15))

# Change the colors, line width and linedge (color) in the following 2 lines
ax.barh(y_pos, df_15.doc_percentage, align='edge', height=0.4, label='doc %', color='red')
ax.barh(y_pos, df_15.per_million/scale_factor, align='edge', height=-0.4, label='frequency (per million)', color='white', edgecolor='black', linewidth=1)
ax.set_yticks(y_pos)
ax.set_yticklabels(df_15.word, fontdict=font_dict)
ax.set_xlabel('doc %')
ax.legend()
ax.invert_yaxis()

ax2 = ax.twiny()
ax2.set_xticks(ax.get_xticks())
ax2.set_xbound(ax.get_xbound())
ax2.set_xticklabels([int(x*scale_factor) for x in ax.get_xticks()])
ax2.set_xlabel('frequency (per million)')

plt.title(title, fontsize=25, loc='left', horizontalalignment='center',
            verticalalignment='center')

plt.savefig(channel+'_ner_freq_plot.png', bbox_inches='tight')
