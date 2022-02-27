'''
Simple script to play a YouTube video by inputting the video id
'''

import webbrowser
import os

# the directory of this file to start the program again (to input another video id)
dir = 'INPUT_FILEPATH'

video_id = input('Input the video id: ')

# show an error message if the input is not 11 characters long (YouTube ids are 11 characters)
while len(video_id) != 11:
    print('video id should be 11 characters long')
    video_id = input('Input the video id: ')
else:
    # open the YouTube video in a new browser window
    webbrowser.open('https://www.youtube.com/watch?v=' + video_id, new=1)

    #this opens the 'dir' file in the same python window
    os.system(dir)
