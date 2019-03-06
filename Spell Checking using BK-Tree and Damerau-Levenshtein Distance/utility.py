# DamerauLevenshtein
from pyxdameraulevenshtein import damerau_levenshtein_distance, normalized_damerau_levenshtein_distance

import os
import json
import pickle

dirpath = os.path.dirname('__file__')

def distance_function(str1, str2):
    return damerau_levenshtein_distance(str1, str2)

def load_words(filename):
    try:
        with open(os.path.join(dirpath, filename + '.json')) as dictionary:
            words = json.load(dictionary)
        return words
    except Exception as e:
        print(str(e))

def pickle_dump(tree, filename):
    try:
        filepath = os.path.join(dirpath, filename + '.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(tree, f)
    except Exception as e:
        print(str(e))

def pickle_load(filename):
    try:
        filepath = os.path.join(dirpath, filename + '.pkl')
        with open(filepath, 'rb') as f:
            tree = pickle.load(f)
        return tree
    except Exception as e:
        print(str(e))