from apiclient.discovery import build
import pandas as pd

'''
Script to extract metadata from the YouTube Data API
In this case, the parameters are:
Short videos (<4mins), uploaded in Jan 2021 to the specified channel
Relevance language is specified as 'en', but videos in other languages are still returned
A maximum of 500-600 IDs can be extracted at one time
'''

# you need to register an API key (https://developers.google.com/youtube/v3/getting-started)
api_key = 'INPUT_API_KEY'
# in this case 'search_term' is set as a blank string, you can input a search word or term here
search_term = ''
# extract the channel id by visiting the channel, right-click, 'View page source'
# then ctrl+f, 'channel_id', until you find a string like this
channel = 'UCzznO4xSV8BKnUBPyswtCUw'
# write the channel name and month number for the csv file name (output)
channel_name = 'Arirang_News_1'

youtube = build('youtube', 'v3', developerKey=api_key)

# create an empty list to extract the video information to
videos = [ ]

# nextPageToken is necessary to extract more than 50 maxResults
# this while loop wll search for the maximum number of videos that fit the search parameters
# maximum = 500-600
nextPageToken = None
while 1:
    # videos from the above specified channelId, less than 4 minutes,
    # published between specified dates, I searched in one month blocks
    # q=search_term is not necessary in this case, but this is the standard place for it
    res = youtube.search().list(q=search_term,
                part='id, snippet',
                type='video', videoDuration='short', channelId=channel,
                publishedAfter='2021-1-01T00:00:00Z', publishedBefore='2021-1-31T23:59:59Z',
                relevanceLanguage='en', maxResults=50, pageToken=nextPageToken).execute()

    videos += res["items"]
    nextPageToken = res.get("nextPageToken")
    if nextPageToken is None:
        break

#create an empty list for each column of metadata
video_id = [ ]
title = [ ]
published_at = [ ]
channel_title = [ ]
channel_id = [ ]
description = [ ]
etag = [ ]

# for each video, append the list with the information
for i in range(len(videos)):
    video_id.append((videos[i])['id']['videoId'])
    title.append((videos[i])['snippet']['title'])
    published_at.append((videos[i])['snippet']['publishedAt'])
    channel_title.append((videos[i])['snippet']['channelTitle'])
    channel_id.append((videos[i])['snippet']['channelId'])
    description.append((videos[i])['snippet']['description'])
    etag.append((videos[i])['etag'])

# create a dictionary
data = {'video_id': video_id,'title': title, 'published_at': published_at,
        'channel_title':channel_title,'channel_id':channel_id,
        'description':description, 'etag':etag}

# convert to dataframe and output to a csv file (name specified by 'channel_name' above)
df = pd.DataFrame(data)
csv_file = channel_name+'.csv'
df.to_csv(csv_file, encoding='utf8')
# print the df to look at the data and see how much has been extracted
print(df)
