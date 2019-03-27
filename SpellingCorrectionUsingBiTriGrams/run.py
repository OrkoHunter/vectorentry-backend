# ### Loads the Eng Vocab Dictionary, Creates a tree, Adds the dictionary to the tree and Dumps the created Tree to a PICKLE OBJECT
import os
import json
import pickle

def pickle_load(filename):
    try:
        filepath = os.path.join(filename)
        with open(filepath, 'rb') as f:
            tree = pickle.load(f)
        return tree
    except Exception as e:
        print(str(e))

# pickle_dump(BKTree(items_dict = load_words('words_dictionary')), 'eng_tree')

def run(word, tree, max_edit_distance = 2):
    return [tree.find(word, x) for x in range(max_edit_distance + 1)]