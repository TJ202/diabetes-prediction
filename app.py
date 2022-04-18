import numpy as np
import pandas as pd
from flask import Flask, redirect, request, render_template, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

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
    return redirect('https://github.com/TJ202/diabetes-prediction')

@app.route('/pdf')
def pdf():
    return redirect('')

@app.route('/predictn')
def predictn():
    return redirect(url_for('home', _anchor='predictnow'))

@app.route('/predict',methods=['POST'])
def predict():
    # choose individual values and convert to numpy array
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    # assign names to columns
    features_name = [ "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    # dataframe
    df = pd.DataFrame(features_value, columns=features_name)
    # pass values to ml model to predict
    output = model.predict(features_value)
    
    # render template based on output of prediction
    if output == 1:
        return render_template('diabetes.html', prediction_text='Diabetic')
    elif output==0:
        if int(request.form.get("Glucose"))<200 and int(request.form.get("Glucose"))>140:
            return render_template('prediabetes.html', prediction_text='Pre-Diabetic')
        else:
            return render_template('nodiabetes.html', prediction_text='Not Diabetic')
        
if __name__ == "__main__":
    app.run(debug=True)
