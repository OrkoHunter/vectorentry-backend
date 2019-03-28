# DamerauLevenshtein
from pyxdameraulevenshtein import damerau_levenshtein_distance, normalized_damerau_levenshtein_distance
from Levenshtein import distance

import os
import json
import pickle

def distance_function(str1, str2, transposition=True):
    return damerau_levenshtein_distance(str1, str2) if transposition else distance(str1, str2)

def load_words(filename):
    try:
        with open(os.path.join(dirpath, filename + '.json')) as dictionary:
            words = json.load(dictionary)
        return words
    except Exception as e:
        print(str(e))

def pickle_dump(tree, filename):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(tree, f)
    except Exception as e:
        print(str(e))