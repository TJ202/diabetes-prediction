import numpy as np
import pandas as pd
from flask import Flask, redirect, request, render_template, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model_pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/viln')
def viln():
    return redirect('https://www.linkedin.com/in/tanvi-johari-3311451b6/')

@app.route('/vigh')
def vigh():
    return redirect('https://github.com/TJ202')

@app.route('/hln')
def hln():
    return redirect('https://www.linkedin.com/in/harikrishnan-nair-04a4b219b')

@app.route('/hgh')
def hgh():
    return redirect('https://github.com/NotHari')

@app.route('/kln')
def kln():
    return redirect('https://www.linkedin.com/in/kaushiksanjayprabhakar/')

@app.route('/kgh')
def kgh():
    return redirect('https://github.com/kaushik-3009')

@app.route('/mlmodel')
def mlmodel():
    return redirect('https://github.com/NotHari/diabetes-predictor')

@app.route('/websitecode')
def websitecode():
    return redirect('')

@app.route('/pdf')
def pdf():
    return redirect('')

@app.route('/predictn')
def predictn():
    return redirect(url_for('home', _anchor='predictnow'))

@app.route('/predict',methods=['POST'])
def predict():
    # print("hello we will now predict")
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = [ "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    
    df = pd.DataFrame(features_value, columns=features_name)
    # output = model.predict(features_value)
    output=0
    print(type(int(request.form.get("Glucose"))))
    if output == 1:
        res_val = "Diabetes"
    elif output==0:
        if int(request.form.get("Glucose"))<200 and int(request.form.get("Glucose"))>140:
            res_val = "Pre-Diabetic"
        else:
            res_val = "No Diabetes"
        
    return render_template('index.html', prediction_text='Patient has {}'.format(res_val),content='')

if __name__ == "__main__":
    app.run(debug=True)
