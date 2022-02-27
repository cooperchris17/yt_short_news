'''
To check the files that are shorter than a set amount of tokens

I decided to delete files shorter than 50 tokens
because many of the videos were very short, didn’t have much spoken language
(mainly just subtitles and visuals), or were advertisements

You can input the video id into the URL to view
or use the simple Python script in this folder ‘id_play.py’
'''

import pandas as pd
from nltk.corpus import PlaintextCorpusReader

# specify root directory, in this case, current directoty
corpus_root = './'
# get PlaintextCorpusReader to read all of the text files in the directory
corpus = PlaintextCorpusReader(corpus_root, '.*\.txt') # doctest: +SKIP
# create empty lists to extract the information to
file_name = []
length = []
video_id = []
# loop through the files and return information for the short files
for doc in corpus.fileids():
    # specify the file length by changing the number here
    if len(corpus.words(doc)) <= 50:
        file_name.append(doc)
        video_id.append(doc[-15:-4])
        length.append(len(corpus.words(doc)))

# create a pandas df for the data, print and create a csv file with the data
data = {'file_name': file_name, 'video_id': video_id, 'length': length}
df = pd.DataFrame(data)
print(df)
df.to_csv('short_texts.csv', encoding='utf8')
