from histogram import histogram_dict, get_words
import sys, random

# returns one value from a random index in an array
def random_word(words):
    return words[random.randint(0, len(words) - 1)]
    
def sample_by_frequency(histogram):
    values_total = sum(histogram.values())
    random_value = random.uniform(0,1)

    accumulator = 0
    for word, word_count in histogram.items():
        accumulator += word_count/values_total # word_count/values_total is probabilites, executed only if we reach them
        if random_value <= accumulator:
            return word

if __name__ == "__main__":
    source_file = sys.argv[1]
    words_array = get_words(source_file)
    histogram = histogram_dict(words_array)

    # get a random word
    print('random word from `{}`: {} \n'.format(source_file, random_word(words_array)))

    # get a frequency sample word
    print('frequency sample word from `{}`: {} \n'.format(source_file, sample_by_frequency(histogram)))

    # testing relative probability
    # sample 1000x, write each response in a file, print a histogram from those words 
    x = 0
    f = open('words.txt','w+')
    while x < 1000:
        f.write(str(sample_by_frequency(histogram)) + ' ')
        x += 1
    f.close()

    print(histogram_dict(get_words('words.txt')))
