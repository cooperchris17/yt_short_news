'''
This script creates a graph of the 21-40 ranked frequent nouns in the B1_plus dataframe
The graph shows normalised frequency (per million) and the percentage of documents the word is in 
I ran the script 5 times (amending the specified parts) to create graphs for the most frequent 100 nouns
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# created with the help of:
# https://stackoverflow.com/questions/51994537/equivalent-of-secondary-y-for-barh-in-pandas-matplotlib

# change the 2 colors here to change the bars and x axis label colors
top_color = 'indigo'
bottom_color = 'mediumslateblue'

pos = 'noun'
# change the numbers on the title each time
title = 'B1+ Frequent News Nouns (21-40)'

# delete 2 zeros from the end of the highest frequency (per million) to get 100% on doc_freq axis
# e.g. if the highest frequency (per million) is 1300, the scale_factor should be 13
scale_factor = 13

df = pd.read_csv('World_'+pos+'_B1_plus.csv')
# I created graphs in blocks of 20, change the numbers to make a graph for different frequency ranges
df_range = df[20:40]

fig, ax = plt.subplots(figsize=(5,7))

font_dict = {'fontsize': 20}

y_pos = np.arange(len(df_range))

ax.barh(y_pos, df_range.doc_percentage, align='edge', height=0.4, color=bottom_color)
ax.barh(y_pos, df_range.per_million/scale_factor, align='edge', height=-0.4, color=top_color)
ax.set_yticks(y_pos)
ax.set_yticklabels(df_range.word, fontdict=font_dict)
ax.set_xlabel('doc %').set_color(bottom_color)
ax.tick_params(axis='x', colors=bottom_color)
ax.legend()
ax.invert_yaxis()
# add the next line of code to keep the x-axis scale the same for all graphs
ax.set_xlim(0, 110)
ax.get_legend().remove()

ax2 = ax.twiny()
ax2.set_xticks(ax.get_xticks())
ax2.set_xbound(ax.get_xbound())
ax2.set_xticklabels([int(x*scale_factor) for x in ax.get_xticks()])
ax2.set_xlabel('frequency (per million)').set_color(top_color)
ax2.tick_params(axis='x', colors=top_color)

plt.title(title, fontsize=15, loc='left', horizontalalignment='center',
            verticalalignment='center')

plt.savefig(pos+'_freq_plot.png', bbox_inches='tight')

