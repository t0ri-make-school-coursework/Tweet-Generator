""""
set sentence list

open words.txt
set wordsCount to the amount of words in words.txt

while there are less than INPUT words in len(sentence)
  get a random number between 0 and wordsCount
  look up that line number in words.txt and append that string to sentence list

after exiting while
  `return ' '.join(input)` makes sentence format from list

"""
import sys, random

# https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def make_sentence(file, length):
    sentence = []
    dictionary_length = file_len(file)

    while len(sentence) < length:
        randomLine = random.randint(0, dictionary_length + 1)

        with open(file) as f:
            for i, line in enumerate(f):
                if i == randomLine:
                    sentence.append(line.rstrip())
    
    return ' '.join(sentence).capitalize() + '.'

if __name__ == '__main__':
    dictionary_file = sys.argv[1]
    sentence_length = int(sys.argv[2])
    
    print(make_sentence(dictionary_file, sentence_length))