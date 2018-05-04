
from flask import Flask, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


def getPredictedEarnings(sat,tution,age,hhincome):    
    with open('modelFile', 'rb') as f:
        my_model = pickle.load(f)
        print("sat getPredictedEarnings ", sat)
        predicted_val = my_model.predict(np.reshape([sat,tution,age,hhincome], (1,4)))
        print("predicted_val", predicted_val)
        return predicted_val[0]
#rf_2 = pickle.loads(f)

@app.route("/")
def home():
    """Render Home Page."""
    #return render_template("index.html")
    return render_template("index.html")
    
@app.route('/prediction/<sat>/<tution>/<age>/<hhincome>')
def prediction(sat,tution,age,hhincome):
    predicted_val = getPredictedEarnings(sat,tution,age,hhincome)
    return jsonify(predicted_val)
    

if __name__ == '__main__':
    app.run(debug=True)