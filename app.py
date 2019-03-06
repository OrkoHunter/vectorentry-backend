from flask import Flask, render_template, request, jsonify

from SymSpellDemo import SpellCorrect

app = Flask(__name__)

spell_correct = None

@app.route("/")
def main():
    global spell_correct

    spell_correct = SpellCorrect()
    return render_template("index.html")


@app.route("/result")
def result():
    global spell_correct

    word = request.args.get("query")
    # Process the word
    return spell_correct.spelling_correct(word)


if __name__ == "__main__":
    app.config.update(TEMPLATES_AUTO_RELOAD = True)
    # port = int(os.environ['PORT'])
    app.run(host = 'localhost', port = 8080, debug = True)
