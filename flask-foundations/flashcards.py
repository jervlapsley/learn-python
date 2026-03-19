from flask import Flask

app = Flask(__name__)

@app.route("/")
def flashcards():
    return "Welcome to the Flashcards App!"