from histogram_dict import histogram
import sys, regex, random

def remove_punctuation(word):
    return regex.sub(ur'\p{P}+', '', word.lower())

# creates an array of words from a file
def get_words(source_file):
    words = list()

    with open(source_file, 'r') as file:
        for line in file:
            for word in line.split():
                words.append(remove_punctuation(word))

    return words

# returns one value from a random index in an array
def random_word(words):
    return words[random.randint(0, len(words) - 1)]
    
def sample_by_frequency(histogram):
    word_counts = histogram.values()
    word_array = histogram.keys()
    random_value = random.uniform(0,1)

    # create list of probabilities
    probabilities = list()
    for count in word_counts:
        probabilities.append((float(count)/sum(word_counts)))

    accumulator = 0
    index = 0
    for probability in probabilities:
        accumulator += probability
        if random_value >= accumulator:
            index += 1
        elif random_value <= accumulator: 
            break
    
    return word_array[index]

if __name__ == "__main__":
    source_file = sys.argv[1]
    source_histo = histogram(source_file)

    # get a random word
    print('random word from `{}`: {}'.format(source_file, random_word(get_words(source_file))))

    # get a frequency sample word
    print('frequency sample word from `{}`: {}'.format(source_file, sample_by_frequency(histogram(source_file))))

    # test relative probability
    x = 0
 
    # sample 1000x, write each response in a file, print a histogram from those words 
    f = open('words.txt','w+')
    while x < 100:
        f.write(sample_by_frequency(source_histo) + ' ')
        print(x)
        x += 1
    f.close()

    words_histogram = histogram('words.txt')
    print(words_histogram)
