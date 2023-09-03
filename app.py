from flask import Flask, render_template, request
from model import model_predict
from util import *

app = Flask(__name__)
app.static_folder = 'templates/static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        high_bp = 'HighBP' in request.form
        return "a"
    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)