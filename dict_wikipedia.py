import wikipedia
import re, time
from typing import List

def tokenize{text: str} 

article = wikipedia.page("Artemis ll" ,auto_suggest=False).content

tokens = tokenize(article)
print(token)

freqs = {}


for word in tokens:
    if word in freqs:
        freqs[word]+=1
    else:
        freqs[word] = 1

print(freqs)
