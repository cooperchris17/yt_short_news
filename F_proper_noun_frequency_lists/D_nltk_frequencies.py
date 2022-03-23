'''
This script was used to calculate the frequency of proper nouns using nltk

The reaults were not used, as nltk didn't correctly tag many items as proper nouns
This is probably due to the lower case text in YouTube transcripts
'''

from nltk import pos_tag, word_tokenize
from nltk.probability import FreqDist
import pandas as pd

df = pd.read_csv('world_news_720_df.csv')
texts = df['text']

tokens = pos_tag(word_tokenize(str([text for text in texts])))

propn = [token[0] for token in tokens if token[1] == 'NNP']

fd = FreqDist(propn)

df = pd.DataFrame(fd.most_common(), columns=['word', 'frequency'])

df.to_csv('nltk_propn.csv', encoding='utf8')
