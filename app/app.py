from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    form = request.form.get('HighBP')
    #buscar la manera de hacerlo en dataframe
    print(form)
    return form

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)