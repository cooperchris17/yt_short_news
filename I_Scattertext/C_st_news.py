'''
This is basically copied from the Scattertext GitHub repository
(https://github.com/JasonKessler/scattertext)

but amended to fit my data (with brief explanations)
'''
import spacy
import en_core_web_sm
import scattertext as st
import pandas as pd
# input the name of the prepared csv file
in_csv = 'JP_KR_st.csv'
# specify the name of the output html
out_html = 'NipponTV_Arirang.html'

df = pd.read_csv(in_csv)

nlp = spacy.load('en_core_web_sm')
corpus = st.CorpusFromPandas(df,
                             category_col='channel',
                             text_col='text',
                             nlp=nlp).build()

html = st.produce_scattertext_explorer(corpus,
       # this needs to match how one of the channels is written in the dataframe
       category='Nippon TV (JP)',
       # this is the label for the graph axis for the 'category' channel
       category_name='JP',
       # and the other channel
       not_category_name='KR',
       width_in_pixels=1200,
       # I added the url in brackets after the channel name in the 'concordance' part of Scattertext
       metadata=df['channel'] + ' (' + df['url'] + ')')
open(out_html, 'wb').write(html.encode('utf-8'))
