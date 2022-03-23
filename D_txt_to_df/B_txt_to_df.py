'''
This script creates a dataframe with rows in the following format:
channel, video_id, text
Two more scripts need to be run to add the upload month

This script should be run in the folder containing txt files for the channel

You only need to change 2 variables (channel_tag & channel)
'''

import re, os, glob
import pandas as pd
# Specify filepath, '*' for current filepath
filepath = '*'
# write channel name as it is at start of filename
channel_tag = 'CGTN_'
# write the text you want to appear in the 'channel' column of the df
channel = 'CGTN (CN)'

def process_txt_files(filelist):
    """ Takes in a list of txt files returns dictionary, output like this:
        {'video_id': 'text'} for all files in directory"""

    file_dict = {}

    for file in glob.iglob(filepath, recursive=True):
        if os.path.isfile(file): # filter dirs
            if file.endswith('.txt'): # avoid editing .py files, etc

                text = []

                with open(file, 'r') as input:
                    for line in input:
                        text.append(line)

                        captions_clean = ' '.join(text)
                        captions_clean = captions_clean.translate({ord(i):
                                                    None for i in '\n'})
                        # remove first part of filename
                        remove_channel = file.replace(channel_tag, '')
                        # remove .txt from filename
                        video_id = remove_channel.replace('.txt', '')
                        file_dict[video_id] = captions_clean

    return file_dict

captions_dict = {}
captions_dict.update(process_txt_files(filepath))

df = pd.DataFrame.from_dict(captions_dict.items())
df.columns = ['video_id', 'text']
df.insert(0, 'channel', channel, allow_duplicates=True)
df_sorted = df.sort_values(by=['video_id'])

print(df_sorted)

df_sorted.to_csv('txt_df.csv', encoding='utf8', index=False)
