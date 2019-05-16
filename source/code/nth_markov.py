#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import sys, random
from histogram import get_words
from dictogram import Dictogram

class MarkovChain(dict):
    def __init__(self, source_file):
        super(MarkovChain)
        # create list of words from source_file
        words_list = get_words(source_file)

        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram

        if words_list is not None:
            # for each index in list of words,
            # call add_count() on that word and the next word
            for index in range(0, len(words_list) - 2):
                self.add_count(words_list[index], words_list[index + 1], words_list[index + 2])

    def add_count(self, word_0, word_1, word_2, count=1):
        self.tokens += count                          # increment tokens by count

        if len(self) == 0:                           
            self[(word_0, word_1)] = Dictogram([word_2])        # initialize a dictogram on word_0 with word_1
            self.types += 1                           # increment types
            return                                    # get next word

        if (word_0, word_1) in self:                         # if word_0 exists in markov chain
            self[(word_0, word_1)].add_count(word_2)      # call add_count(word_1) on the word_0 dictogram
            return                                    # get next word

        # if markov chain isn't empty, word_0 isn't inside it
        self[(word_0, word_1)] = Dictogram([word_2])      # initialize a dictogram on word_0 with word_1
        self.types += 1                               # increment types

    def random_word(self, input_set):
        if input_set in self.keys():
            next_words = self.get(input_set)                   # get dictogram belonging to word
            random_num = random.randint(0, len(next_words) - 1) # generate random_num to assess probabilities
            accumulator = 0                                     # set accumulator at 0
            for word, word_count in next_words.items():         # loop through (key, value) of dictogram values
                if len(next_words.items()) == 1:                # if the array is only 1 long, return that word
                    return word

                if random_num <= accumulator:                   # if random_num is less than the accumulator
                    return word                                 # return key
                else:
                    accumulator += word_count                   # or increase accumulator by value and loop again
    
    def make_sentence(self):
        sentence = list()
        sentence.extend(random.choice(list(self.keys())))

        for index in range(1, 10):                     # while sentence is less than 10 words
          word = self.random_word((sentence[index - 1], sentence[index]))
          if word is None:
            break
          
          sentence.append(word)      # append a random word to sentence
        return ' '.join(sentence).capitalize() + '.'                # return sentence array in form of sentence

if __name__ == '__main__':
    # python this_file corpus_file
    output = MarkovChain(sys.argv[1])    
    output.make_sentence()
