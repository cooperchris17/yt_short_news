import pandas as pd

'''
This script filters metadata for files that didn't have a transcript
Full metadata for the files that had a transcript is saved in a new csv file
You only need to input the name of the news_channel
(if previous naming conventions were followed)
'''

# just input the name of the news channel
news_channel = 'Arirang_News'

# no need to amend these variables (unless they don't match your input files)
metadata_file = news_channel+'_2021.csv'
tran_id_file = news_channel+'_2021_TranIds.csv'
out_csv = news_channel+'_transcript_metadata.csv'
# read in the original metadata file as a df
metadata_df = pd.read_csv(metadata_file)
# read in the list of video ids that had transcripts as a df
tranId_df = pd.read_csv(tran_id_file)
# search for ids in the metadata file that actually had a transcript
search = metadata_df.video_id.isin(tranId_df.HasTranscript)
# output new df to csc containing metadata for files that had a transcript
df_out = metadata_df[search]
# the output will retain initial index values, but this will be realigned when all channels' metadata is combined in one file
df_out.to_csv(out_csv, encoding='utf8', index=False)
