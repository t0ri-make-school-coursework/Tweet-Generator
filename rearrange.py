import sys
from random import shuffle

def rearrange(input):
    shuffle(input)
    return ' '.join(input)

if __name__ == '__main__':
    input = sys.argv
    input.pop(0)

    print(rearrange(input))
