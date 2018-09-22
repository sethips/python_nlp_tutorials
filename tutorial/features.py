from textblob import TextBlob, Word
blob = TextBlob("ITP is a two-year graduate program located in the Tisch"
                "School of the Arts. Perhaps the best way to describe us is as"
                "a Center for the Recently Possible.")

print("")
print("---Print Sentences---")
print("")
for sentence in blob.sentences:
    print(sentence)


print("")
print("---Print Words---")
print("")
for sentence in blob.sentences:
    for word in sentence.words:
        print(word)

print("")
print("---Print Noun Phrases---")
print("")
for np in blob.noun_phrases:
    print(np)

print("")
print("---Print Part of Speech Tags---")
print("")
for word, pos in blob.tags:
    print(word, pos)


print("")
print("---Print Plural Form---")
print("")
w = Word("university")
print(w.pluralize())


print("")
print("---Print Lemma---")
print("")
w = Word("universities")
print(w.lemmatize())

print("")
print("---Print Positivity---")
print("")
print(blob.sentiment)
