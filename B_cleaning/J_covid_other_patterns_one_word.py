'''
This script works in the same way as covid_19.py and covid.py
But it was used to amend other patterns by amending the list in 'covid_19_word'
with 'corrected_word'
'''

import glob, os, re

covid_19_word = 'kovacs'
corrected_word = 'covax'

# joined_covid = re.compile(r'\b(?:{0})\b'.format('|'.join(covid_19_word)))

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    for line in input:
                        output.write(re.sub(covid_19_word, corrected_word, line))

            # replace file with original name
            os.replace('temp.txt', file)
