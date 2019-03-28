from flask import Flask, render_template, request, jsonify
import os

# from SymSpellDemo import SpellCorrect

from SpellingCorrectionUsingBiTriGrams import SpellingCorrectionUsingNGrams

import pickle

app = Flask(__name__)

spell_correct = None

@app.route("/")
def main():
    global spell_correct

    # with open('word_vocab.pkl', 'rb') as f:
    #     word2idx, idx2word = pickle.load(f)
    # pickle_dump(BKTree(items_dict = word2idx), 'wiki_dump.pkl')

    # spell_correct = SpellCorrect()
    spell_correct = SpellingCorrectionUsingNGrams.WordSpellingCorrection('en_wikinews.txt', 'wiki_dump.pkl', 'token_cnts_wiki.json', 'word_vocab.pkl')

    return render_template("index.html")


@app.route("/result")
def result():
    global spell_correct

    word = request.args.get("query")
    # Process the word
    return SpellingCorrectionUsingNGrams.get_spelling_correction(word, spell_correct)


if __name__ == "__main__":
    app.config.update(TEMPLATES_AUTO_RELOAD = True)
    # port = int(os.environ['PORT'])
    app.run(debug = True)
