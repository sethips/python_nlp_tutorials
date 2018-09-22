from textblob import TextBlob
import sys

blob = TextBlob(sys.stdin.read())

print("Per sentence sentiment")
for sentence in blob.sentences:
    print(sentence)
    print("\t {}".format(sentence.sentiment))

print("")
print("Summary Sentiment")
print(blob.sentiment)
