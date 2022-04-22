from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Главная страничка"




app.run()
