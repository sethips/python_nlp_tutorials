from textblob import TextBlob
import sys

blob = TextBlob(sys.stdin.read())

short_sentences = [sentence for sentence in blob.sentences
                   if len(sentence.words) <= 5]

for short_sentence in short_sentences:
    print(short_sentence)
