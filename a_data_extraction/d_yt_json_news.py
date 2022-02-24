from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import pandas as pd

'''
This script uses the youtube_ids extracted from the YouTube Data API
It downloads available transripts as .json with the youtube-transcript-api
The json files also have timestamps (in addition to the transcript text)
Only need to amend 3 variables (output_folder, file_name_identifier, metadata_file)
'''

json_formatter = JSONFormatter()
# create the folder first and add the filepath here
output_folder = 'transcripts_txt/Arirang_News_2021//'
# input shortened channel name to append to file_name
file_name_identifier = 'Arirang_'
# input file to read the video_ids
metadata_file = 'Arirang_2021.csv'
df = pd.read_csv(metadata_file)
# the column in the df containing video ids
id_col = df.iloc[:,1]

# create an open list to extract the video_ids that have a transcript
HasTranscript = [ ]

# this for loop reads the video_ids from the metadata_file and outputs transcript text files
i = 0
for vid_id in id_col:
    try:
        file_name = file_name_identifier+vid_id
        # generate a list of transcripts for each video id from the df
        transcript_list = YouTubeTranscriptApi.list_transcripts(id_col[i])
        # if the transcript file in the transcript_list is in English and auto-generated (not manually input by user) transcript will be returned
        for transcript in transcript_list:
            if transcript.language_code == 'en' and transcript.is_generated == True:
                en_transcript = transcript.fetch()
                # return json file, containing timestamps and text
                json_formatted = json_formatter.format_transcript(en_transcript)
                with open(output_folder+file_name+'.json', 'w', encoding='utf-8') as json_file:
                    json_file.write(json_formatted)
                    # print file_name to see progress
                    print(file_name)
                    HasTranscript.append(vid_id)
    # I added this to overcome a 'transcriptsDisabled' error message, some transcripts are not available
    except:
        print("no transcript: ", vid_id)

    i = i + 1

# output video_ids that have a transcript to csv file
data = {'HasTranscript': HasTranscript}
df_out = pd.DataFrame(data)
append_file = metadata_file.replace('.csv', '_TranIds.csv')
df_out.to_csv(append_file, encoding='utf8')
