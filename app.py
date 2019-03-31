from flask import Flask ,render_template, jsonify, request
import random
import base64
import json

import pickle
import sklearn
import pandas as pd
import numpy as np

app = Flask(__name__)

filename = 'saved_model.h5py'


def forge_make(X, Y, Z, Timestamp):
#     Pressure = np.random.randint(637, 737, (len(X), 1))
#     print(Pressure)
#     GripAngle = np.random.randint(1000, 1200, (len(X), 1))
    #Pressure = list(np.random.randint(637, 737, (len(X), 1)))
    #GripAngle = list(np.random.randint(1000, 1200, (len(X), 1)))
    
#     X = pd.DataFrame(X, columns = ['X'])
#     Y = pd.DataFrame(Y, columns = ['Y'])
#     Z = pd.DataFrame(Z, columns = ['Z'])
#     Pressure = pd.DataFrame(Pressure, columns = ['Pressure'])
#     GripAngle = pd.DataFrame(GripAngle, columns = ['GripAngle'])
#     Timestamp = pd.DataFrame(Timestamp, columns = ['Timestamp'])
    
    cols = {
        'X':X,
        'Y':Y,
        'Z':Z,
        #'Pressure':Pressure,
        #'GripAngle':GripAngle,
        'Timestamp':Timestamp
    }
#     print(cols)
    df = pd.DataFrame(cols)#,columns = ['X', 'Y', 'Z', 'Pressure', 'GripAngle', 'Timestamp'])
    
    return df

def load_model(X, Y, Z, Timestamp):
    x_test = forge_make(X, Y, Z, Timestamp)
    loaded_model = pickle.load(open(filename, 'rb'))
    #print(x_test)
    y_pred = loaded_model.predict_proba(x_test)
    return y_pred




@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        data = json.loads(data)
        print(data,end="\n###\n\n")
        X = []
        Y = []
        Z = [0]*len(data)
        TimeStamp = []
        for i in range(len(data)):
                X.append(data[i][0])
                Y.append(data[i][1])
                TimeStamp.append(data[i][2])
        # nodes = json.loads(nodes)
        a = load_model(X,Y,Z,TimeStamp)
        print(a[0])
        return a[0]
    else:
        return '<html>Hi</html>'
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = "5000",debug = True)
    # app.run(host='0.0.0.0')
