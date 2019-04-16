"""
Input: `python source/code/histogram.py source/code/text/fish.txt fish`

Output:

```
Histogram as a dictionary: {'blue': 1, 'fish': 4, 'two': 1, 'red': 1, 'one': 1}

Histogram as a list of tuples: [('one', 1), ('two', 1), ('red', 1), ('blue', 1), ('fish', 4)]

Histogram as a list of lists: [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]

`source/code/text/fish.txt` has 4 unique words

"fish" appears in `source/code/text/fish.txt` 4 times
```
"""

import sys, string
    
def remove_punctuation(word):
    translator = str.maketrans('','',string.punctuation)
    return word.translate(translator).lower()

# creates an array of words from a file
def get_words(source_file):
    words = list()

    with open(source_file, 'r') as file:
        for line in file:
            for word in line.split():
                words.append(remove_punctuation(word))

    return words

def histogram_dict(words_array):
    histogram = dict()

    for word in words_array:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram

# expects histogram to be a dict
def unique_words(histogram):
    unique = 0
    values = histogram.values()

    for num in values:
        if num == 1:
            unique += 1

    return unique

# expects histogram to be a dict
def frequency(histogram, word):
    return histogram[word]

def histogram_tuples(source_file):
    histogram = list()

    with open(source_file, 'r') as file:
        for line in file:
            for word in line.split():
                clean_word = remove_punctuation(word)

                if len(histogram) > 0:
                    word_found = False
                    index = -1
                    for word_item in histogram:
                        index += 1
                        if clean_word == word_item[0]:
                            histogram.append((clean_word, word_item[1] + 1))
                            del histogram[index]
                            word_found = True
                            break

                    if not word_found:
                        histogram.append((clean_word, 1))
                else:
                    histogram.append((clean_word, 1))

    return histogram

def histogram_list(source_file):
    histogram = list()

    with open(source_file, 'r') as file:
        for line in file:
            for word in line.split():
                clean_word = remove_punctuation(word)

                if len(histogram) > 0:
                    word_found = False

                    for word_item in histogram:
                        if clean_word == word_item[0]:
                            word_item[1] += 1
                            word_found = True

                    if not word_found:
                        histogram.append([clean_word, 1])
                else:
                    histogram.append([clean_word, 1])

    return histogram

if __name__ == "__main__":
    source_file = sys.argv[1]

    # Create an array from a file.txt
    get_words_array = get_words(source_file)

    # Create a histogram from an array of words
    histogram_dict = histogram_dict(get_words_array)
    print('Histogram as a dictionary: {} \n'.format(histogram_dict))

    histogram_tuple = histogram_tuples(source_file)
    print('Histogram as a list of tuples: {} \n'.format(histogram_tuple))

    histogram_list = histogram_list(source_file)
    print('Histogram as a list of lists: {} \n'.format(histogram_list))

    # Return the amount of unique words in a file.txt
    print('`{}` has {} unique words \n'.format(source_file, unique_words(histogram_dict)))

    # If another argument exists, perform frequency()
    if len(sys.argv) > 2:
      frequency_word = sys.argv[2]
      print('"{}" appears in `{}` {} times \n'.format(frequency_word, source_file, frequency(histogram_dict, frequency_word)))
