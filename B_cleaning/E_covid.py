'''
This script replaces the words in the 'covid_19_word' list with 'covid'
The words were taken from the 'covid_19.py' script, words that could have been
correctly used were deleted (e.g. coffee, cobra)
Other words ('cove', 'corvette', 'covert', 'coveted', 'curvy') were checked and
amended manually as they were mainly 'covid' words, but had correct usage cases too
'''

import glob, os, re

covid_19_word = ['covet', 'kovid', 'coven', 'kovit',
                'kovi', 'kovite', 'covenant', 'cobit', 'cova',
                'kova', 'kovy', 'kobit', 'covey', 'covit', 'covent', 'kovitt',
                'coved', 'kovan', 'coving', 'copin', 'kovind',
                'kovic', 'copic', 'kovitz', 'kava', 'kovat',
                'cobot', 'colbit', 'culvert', 'kowitt', 'kovac',
                'kerbin', 'kobit', 'curvit', 'kuvin', 'kuvy', 'kovate', 'kolvin',
                'covey', 'covad', 'govid', 'clovett', 'covett', 'clovert',
                'kroger', 'crovid', 'kogit', 'cobart', 'provite', 'cobia',
                'culver', 'coving', 'colvin', 'corvin', 'kuving',
                'cloven', 'koba', 'kuvin', 'covete', 'curvid',
                'kobi', 'kogan', 'corvae', 'cobo', 'kuvu',
                'kaabi', 'kaaba', 'kaveh', 'kaffir', 'kofit']

joined_covid = re.compile(r'\b(?:{0})\b'.format('|'.join(covid_19_word)))

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    for line in input:
                        output.write(re.sub(joined_covid, 'covid', line))

            # replace file with original name
            os.replace('temp.txt', file)
