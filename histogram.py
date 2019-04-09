"""
A histogram() function which takes a source_text argument 
(can be either a filename or the contents of the file as 
a string, your choice) and return a histogram data 
structure.

A unique_words() function that takes a histogram argument 
and returns the total count of unique words in the 
histogram.

A frequency() function that takes a word and histogram 
argument and returns the number of times that word appears 
in a text.

Pseudocodingish --

def histogram(file_name):
    # return histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    source_text = 

    each source_word in source_text
        each histogram_word in histogram
            if source_word == histogram_word
                increment histogram_word pair
            else
                create new value in histogram and set it to 1

"""

import sys, string, regex

# https://stackoverflow.com/questions/11066400/remove-punctuation-from-unicode-formatted-strings/11066687#11066687
# Cleaning the text with this Regex produces better results than other options like
# word.translate(string.maketrans('', ''), string.punctuation)
def remove_punctuation(word):
    return regex.sub(ur'\p{P}+', '', word.lower())

def histogram(source_file):
    histogram = {}

    with open(source_file, 'r') as file:
        for line in file:
            for word in line.split():
                clean_word = remove_punctuation(word)
                if clean_word not in histogram:
                    histogram[clean_word] = 1
                else:
                    histogram[clean_word] += 1

    return histogram

def unique_words(histogram):
    unique = 0
    values = histogram.values()

    for num in values:
        if num == 1:
            unique += 1

    return unique

def frequency(histogram, word):
    return histogram.get(word, 0)


if __name__ == "__main__":
    # Take a file.txt and create a histogram
    histogram = histogram(sys.argv[1])

    print('`{}` has {} unique words'.format(sys.argv[1], unique_words(histogram)))

    # If another argument exists, perform frequency()
    if len(sys.argv) > 2:
      frequency_word = sys.argv[2]
      print('"{}" appears in `{}` {} times'.format(frequency_word, sys.argv[1], frequency(histogram, frequency_word)))


    

