from flask import Flask, render_template, request
import pickle
import joblib

app = Flask(__name__)

model = pickle.load(open("placement (1).pkl", 'rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index_page():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def index():
    sen1 = request.form['sen1']
    sen2 = request.form['sen2']
    sen3 = request.form['sen3']
    sen4 = request.form['sen4']
    sen5 = request.form['sen5']
    sen6 = request.form['sen6']

    X = [[int(sen1), int(sen2), int(sen3), int(sen4), int(sen5), int(sen6)]]

    prediction = model.predict(X)

    return render_template("submit.html", y=prediction)



if __name__ == '__main__':
    app.run(debug=True)
