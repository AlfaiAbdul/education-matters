
from flask import Flask, jsonify, render_template, request
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
    return render_template("index.html")
	
@app.route("/index")
def index():
    return render_template("index.html")
	
@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/cluster_3d")
def cluster_3d():
    return render_template("cluster_3d.html")

@app.route("/prediction", methods = ['POST','GET'])
def predict():

    # return render_template("predict.html")
	if request.method == 'POST':
		age = request.form.get('age')
		satAvg = request.form.get('satAvg')
		tutionFee = request.form.get('tutionFee')
		hhIncome = request.form.get('hhIncome')
		predicted_val = getPredictedEarnings(satAvg,tutionFee,age,hhIncome)
		return redirect("predict.html", range = predicted_val)
	else:
      # return redirect(url_for('index'))
		return render_template("predict.html")

@app.route("/cluster")
def cluster():
    return render_template("cluster.html")

@app.route("/observations")
def observations():
    return render_template("observations.html")
    
@app.route('/prediction/<sat>/<tution>/<age>/<hhincome>')
def prediction(sat,tution,age,hhincome):
    predicted_val = getPredictedEarnings(sat,tution,age,hhincome)
    return jsonify(predicted_val)
    

if __name__ == '__main__':
    app.run(debug=True)