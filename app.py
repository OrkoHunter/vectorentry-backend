from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/result")
def result():
    word = request.args.get("query")
    # Process the word
    return word


if __name__ == "__main__":
    app.config.update(TEMPLATES_AUTO_RELOAD = True)
    app.run(debug=True)
