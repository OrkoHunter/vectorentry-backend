from utility import load_words, pickle_dump, pickle_load

from bktree import BKTree

# pickle_dump(BKTree(items_dict = load_words('words_dictionary')), 'eng_tree')

def run():
    tree = pickle_load("eng_tree")
    while True:
        user_input = input("Write the word you want spellchecked :: ")
        N = int(input("Enter N :: "))
        if user_input != "":
            print(tree.find(user_input, N))
        else:
            break

run()