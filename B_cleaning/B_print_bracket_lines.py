'''
this script iterates through all files in all directories
(from where the program is run)
it prints the filename and any word in square brackets (only .txt files)
after deleting [Music], etc, this will show where words have been censored
the words can be checked by using the videos id to watch the video
'''

import glob, os, re

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            f = open(file, "r")
            raw = f.readlines()

            for line in raw:
                if re.search('\[.*\]', line):
                    print(file, ': ', line)
