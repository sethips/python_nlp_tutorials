from textblob import TextBlob, Word
import sys

blob = TextBlob(sys.stdin.read())

nouns = [word.lemmatize() for word, tag in blob.tags if tag == 'NN']

print("This text is about:")

for noun in nouns:
    print(Word(noun).pluralize())
