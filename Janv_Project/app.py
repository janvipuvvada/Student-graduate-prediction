from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print("Initialized")
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        name = request.form['Name']
        feature_values = [
            str(request.form['Name']),
            float(request.form['Sem1']),
            float(request.form['Sem2']),
            float(request.form['Sem3']),
            float(request.form['Sem4']),
            float(request.form['Sem5']),
            float(request.form['Sem6']),
            float(request.form['Sem7']),
            float(request.form['Sem8'])
        ]

        prediction = gnb.predict([feature_values[1:]])[0]
        if prediction == 'Pass':
            return render_template('index_pass.html', prediction=prediction)
        else:
            return render_template('index_fail.html', prediction=prediction)


if __name__ == '__main__':
    os.chdir("F:\Janv_Project")
    data = pd.read_csv("data.csv")
    x_train, x_test, y_train, y_test = train_test_split(data.iloc[:, [3, 4, 5, 6, 7, 8, 9, 10]], data.iloc[:, 11], test_size=0.2, random_state=42)
    gnb = GaussianNB()
    gnb.fit(x_train, y_train)
    app.run(debug=True)
