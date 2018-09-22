from textblob import TextBlob
import sys
import random

blob = TextBlob(sys.stdin.read())

noun_phrases = blob.noun_phrases
verbs = [word.lemmatize() for word, tag in blob.tags if tag == 'VB']

for i, verb in enumerate(verbs):
    print(f'Step {i}: {verb.title()} {random.choice(noun_phrases)}')
