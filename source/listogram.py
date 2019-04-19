#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        self.tokens += count    # increment tokens by count
        word_found = False      # initiate word_found as False Bool

        for word_item in self:
            if word in word_item:
                # if the word is in listogram
                word_item[1] += count   # increment value by count
                word_found = True       # set word_found to True

        # if word_found is still False
        if not word_found:
            self.types += 1                 # increment types by 1
            self.append([word, count])      # create new word_item for new word

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for word_item in self: 
            if word in word_item:
                return word_item[1]  # return frequency if word is found
        
        return 0    # return 0 if frequency not found

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for word_item in self:
            if word in word_item:
                return True         # if word is in listogram, return True
        
        return False                # if word isn't in listogram, return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        index = 0                    # initialize index as 0
        for word_item in self:
            index += 1               # increment variable index for each index
            if target in word_item:
                return index         # return index when target is found

        return None                  # return None if target is not found

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
