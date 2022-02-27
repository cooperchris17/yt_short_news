'''
This script replaces the words in the 'covid_19_word' list with 'covid-19'
The words were identified by extracting words that occured with ' 19', '-19', '19'
The words were qualitatively checked to only replace words that actually
represented 'covid-19'
'''

import glob, os, re

covid_19_word = ['covet 19', 'covert 19', 'covid19', 'kobe 19', 'coven 19',
'covet-19','kovid 19', 'kovit 19', 'cover 19', 'kovi 19', 'kovite 19',
'coveted 19', 'covered 19', 'kovy 19', 'carbon 19', 'kovit-19',
'covid 19', 'cobit 19', 'cobra 19', 'kova 19', 'kava 19', 'kevin 19',
'kovid19', 'cova 19', 'kobit 19', 'cov19', 'covenant 19', 'covit 19',
'kovan 19', 'coffee 19', 'covey 19', 'coving 19', 'copin 19',
'kovitt 19', 'cova-19', 'kovin-19', 'cove 19', 'kovin 19',
'kovind 19', 'kelvin 19', 'coba 19', 'curvy 19', 'corbett 19',
'corvette 19', 'kovic 19', 'curved 19', 'kv-19', 'kovit19', 'covit19',
'cobin 19', 'copa 19', 'carver 19', 'covent 19', 'kovat 19', 'kofi 19',
'probing 19', 'kervin 19', 'covin 19', 'code 19', 'profit 19',
'cooper 19', 'coved 19', 'koda 19', 'coming 19', 'toby 19', 'copic 19',
'cobot 19', 'covate 19', 'colbit 19', 'kobet 19', 'kermit 19',
'coffin 19', 'corvid 19', 'carpet 19', 'kave 19', 'culvert 19',
'corporate 19', 'convent 19', 'comet 19', 'coping 19', 'clovid 19',
'kavit 19', 'curving 19', 'kov 19', 'carved 19', 'core 19',
'kovitz 19', 'copy 19', 'copen 19', 'korvid-19', 'covat-19',
'covit-19', 'coven-19', 'covin-19', 'kovid-19', 'covey-19',
'curvet-19', 'copen19', 'copit19', 'kovac 19', 'kobe 19th',
'kov19', 'call v19', 'cool v19', 'qv19', 'kerbin 19', 'copper 19',
'curve 19', 'clover 19', 'combat 19', 'coca-19', 'copied 19',
'conflict 19', 'kobit-19', 'coded 19', 'covering 19', 'curvit 19',
'covering 19', 'quebec 19', 'carbon-19', 'kuvin19', 'cop19', 'kuvy 19',
'kirby 19', 'kovate 19', 'kolvin 19', 'calling 19', 'kavin 19', 'korean 19',
'convict 19', 'covey 19', 'forward 19', 'kuwait 19', 'kovi-19', 'cobit-19',
'covad19', 'govid19', 'clovett 19', 'covett 19', 'clovert 19', 'curvature 19',
'kroger 19', 'crovid 19', 'coyote 19', 'kogit 19', 'cobart 19', 'provite 19',
'yukov 19', 'carving 19', 'cobia 19', 'cognitive 19', 'occulvie 19', 'kuv 19',
'culver 19', 'coving 19', 'colvin 19', 'clove 19', 'corvin 19', 'kuving 19',
'cloven 19', 'koba 19', 'kuvin 19', 'cougar 19', 'covete 19', 'calvin 19',
'kv 19', 'cool 19', 'cleveland 19', 'scovit 19', 'curvid 19', 'coped 19',
'kobi 19', 'coke 19', 'kogan 19', 'corvae 19', 'cobo 19', 'karma 19', 'kuvu 19',
'kaabi 19', 'kaaba 19', 'kaveh 19', 'kaffir 19', 'pulpit 19', 'kofit 19',
'cove in 19', 'cove at 19', 'cove with 19']

joined_covid = re.compile(r'\b(?:{0})\b'.format('|'.join(covid_19_word)))

# optional space, does this work [\r\n]*
# joined_covid = re.compile(r'\b(?:%s)\b' % '|'.join(covid_19_word))

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    for line in input:
                        output.write(re.sub(joined_covid, 'covid-19', line))

            # replace file with original name
            os.replace('temp.txt', file)
