import pandas as pd
from konlpy.tag import Okt
import json
from tqdm import tqdm

wordDict = {}
okt = Okt()
num_lines = sum(1 for line in open('corpus.txt','r'))
with open('corpus.txt', 'r') as f:
    for line in tqdm(f, total=num_lines):
        # if '<doc ' or '&lt' in line:
        #     continue
        # print(f'text: {line}')
        # print(f'Phrases: {okt.phrases(line)}')
        Nouns = okt.nouns(line)
        # print(f'Nouns: {Nouns}')
        for word in Nouns:
            if word not in wordDict:
                wordDict[word]=0
            wordDict[word]+=1

with open('./dictionary.json', 'w') as f:
    json.dump(wordDict, f, ensure_ascii=False, indent=4)

    
    