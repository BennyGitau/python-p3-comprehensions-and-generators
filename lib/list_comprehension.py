#!/usr/bin/env python3
num_list = range(10)
def return_evens(num_list):

    evens_list = [n for n in num_list if n%2 == 0]
    print(evens_list)
    return evens_list
return_evens(num_list)

sentence_list = [
        "I like computers",
        "I require coffee",
        "Live long and prosper",
]
def make_exclamation(sentence_list):
    sentences_with_exclamation = [s if s.endswith('!') else s + '!' for s in sentence_list]
    print(sentences_with_exclamation)
    return sentences_with_exclamation

make_exclamation(sentence_list)