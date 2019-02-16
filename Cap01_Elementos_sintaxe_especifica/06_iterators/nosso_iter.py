#!/usr/bin/env python3


my_sentence = ("This is a sentence")
for word in my_sentence.split():
    print(word)
#
# my_sentence = Sentence("This is a sentence")
print()

class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

my_sentence = Sentence("this is a test")
for word in my_sentence:
    print(word)

#print(next(my_sentence))
print()

# generator
def new_sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence = new_sentence("this is a test")
for w in my_sentence:
    print(w)