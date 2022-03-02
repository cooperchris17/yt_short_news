'''
This script works in the same way as covid_19.py and covid.py
But it was used to amend other patterns by amending the list in 'covid_19_word'
with 'corrected_word'
'''

import glob, os, re

covid_19_word = ['coveted', 'covert']
corrected_word = 'covid'

joined_covid = re.compile(r'\b(?:{0})\b'.format('|'.join(covid_19_word)))

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    for line in input:
                        output.write(re.sub(joined_covid, corrected_word, line))

            # replace file with original name
            os.replace('temp.txt', file)


''' Corrected patterns
['yukovit 19', 'yukovic 19', 'yukova 19'] -> new covid-19
['uncover 19', 'uncovered 19'] -> on covid-19
['medernikovic 19', 'modern akova 19'] -> moderna covid-19
['coveted', 'covert'] -> covid-19
- coveted & covert were done separately as they required lots of manual checking
- the files with genuine use cases were removed from the folder before cleaning
'''
