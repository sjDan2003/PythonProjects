import json
import argparse

def IsWordInDictionary(dictionary, word):



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('chars', help='Characters to match to words')
    args = parser.parse_args()
    print(args.chars)

    with open('dictionary.json') as f:
        dictionary = json.load(f)

    for outerIter in range(0, len(args.chars)):



    word = args.chars.strip().lower()
    if IsWordInDictionary(dictionary, word):
        print('In dict')
    else:
        print('Not in dict')


EALKI

EALKI
EALIK
EAKLI
EAKIL
EAILK
EAIKL
