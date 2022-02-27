'''
delete all documents shorter than a set length
'''

import os
from nltk.corpus import PlaintextCorpusReader

# specify root directory, in this case, current directoty
corpus_root = './'
# get PlaintextCorpusReader to read all of the text files in the directory
corpus = PlaintextCorpusReader(corpus_root, '.*\.txt') # doctest: +SKIP
# loop through the files and delete files shorter than the set length
for doc in corpus.fileids():
    # specify the file length by changing the number here
    if len(corpus.words(doc)) <= 50:
        os.remove(doc)

'''
The metadata needs to be updated to delete data for files that have now been deleted
I did this using a text editor (Atom), pasting in the path of all the remaining files in the channel
Then using find & replace all to delete the unnecessary text before and after the video_id
Then I re-ran ‘metadata_has_transcript.py’ and ‘delete_duplicated_rows’
'''
