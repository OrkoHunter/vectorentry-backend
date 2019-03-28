from flask import Flask, render_template, request, jsonify
import os

# from SymSpellDemo import SpellCorrect

from SpellingCorrectionUsingBiTriGrams import SpellingCorrectionUsingNGrams

import pickle

app = Flask(__name__)

spell_correct = SpellingCorrectionUsingNGrams.WordSpellingCorrection('en_wikinews.txt', 'SpellingCorrectionUsingBiTriGrams/wiki_dump.pkl', 'token_cnts_wiki.json', 'word_vocab.pkl')

@app.route("/")
def main():
    # with open('word_vocab.pkl', 'rb') as f:
    #     word2idx, idx2word = pickle.load(f)
    # pickle_dump(BKTree(items_dict = word2idx), 'wiki_dump.pkl')

    # spell_correct = SpellCorrect()

    return render_template("index.html")


@app.route("/result")
def result():

    word = request.args.get("query")
    # Process the word
    return SpellingCorrectionUsingNGrams.get_spelling_correction(word, spell_correct, max_edit_dis = 2)


if __name__ == "__main__":
    app.config.update(TEMPLATES_AUTO_RELOAD = True)
    # port = int(os.environ['PORT'])
    app.run(debug = True)
