
from flask import Flask, jsonify, render_template, request
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


def getPredictedEarningsRange(sat,tution,age,hhincome):    
    with open('TreeModelFile', 'rb') as f:
        tree_model = pickle.load(f)
        predicted_range = tree_model.predict(np.reshape([sat,tution,age,hhincome], (1,4)))
        print("predicted_val tree_model", predicted_range)
        f.close()
        return predicted_range[0]

def getPredictedEarnings(sat,tution,age,hhincome):    
    with open('lr_model', 'rb') as m_file:
        reg_model = pickle.load(m_file)
        predicted_val = reg_model.predict(np.reshape([float(sat),float(age),float(hhincome),float(tution)], (1,4)))[0][0].astype(int)
        print("predicted_val reg_model", predicted_val)
        m_file.close()
        return predicted_val
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

@app.route("/prediction")
def predict():
    return render_template("predict.html")
	

@app.route("/cluster")
def cluster():
    return render_template("cluster.html")

@app.route("/observations")
def observations():
    return render_template("observations.html")
    
@app.route('/prediction/<sat>/<tution>/<age>/<hhincome>')
def prediction(sat,tution,age,hhincome):
    # print(type(sat)) 
    # print(type(hhincome))
    predicted_range = getPredictedEarningsRange(sat,tution,age,hhincome)  
    predicted_val = getPredictedEarnings(sat,tution,age,hhincome)
    temp = []
    out_dict={} 
    out_dict['value'] = str(predicted_val)
    out_dict['range'] = predicted_range
    temp.append(out_dict)
    return jsonify(temp)

if __name__ == '__main__':
    app.run(debug=True)