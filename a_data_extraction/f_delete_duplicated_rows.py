import pandas as pd

'''
Some metadata files had duplicated metadata
This script checks for and deletes duplicated data, creating a new csv file
You only need to input the name of the channel
(if previous naming conventions were followed)
'''

# input the channel name here:
channel = 'Arirang_News'
# read in the csv file
df = pd.read_csv(channel+'_transcript_metadata.csv')
# check if the csv file has any duplicate rows, if not, 'no duplicated rows' is printed'
if df.duplicated(['video_id']).sum() == 0:
    print('')
    print('No duplicate rows')
    print('')
# if there are duplicate rows, print a new metadata file with the duplicates deleted
# manually delete the old file and rename the new file if necessary
else:
    no_duplicates_df = df.drop_duplicates(['video_id'])
    no_duplicates_df.to_csv(channel+'_transcript_metadata_2.csv', encoding='utf8', index=False)
