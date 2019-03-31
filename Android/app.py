from flask import Flask ,render_template, jsonify, request
import random
import base64
import json

# import pickle
# import sklearn
# import pandas as pd
# import numpy as np

app = Flask(__name__)

filename = 'saved_model.h5py'


import pickle
import sklearn
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math

filename = 'saved_model.h5py'

# def forge_make(X, Y, Z, Timestamp):
#     cols = {
#         'X':X,
#         'Y':Y,
#         'Z':Z,
#         'Timestamp':Timestamp
#     }
#     df = pd.DataFrame(cols)
#     return df

# def get_probability(X, Y, Z, Timestamp):
#     x_test = forge_make(X, Y, Z, Timestamp)
#     print(x_test)
#     loaded_model = pickle.load(open(filename, 'rb'))
#     y_pred = loaded_model.predict_proba(x_test)
#     avg = 0.00
#     for p in y_pred:
#         avg+=p[0]
        
#     print(avg)
#     print(avg/len(y_pred))
#     return int(100*(avg/len(y_pred)))


def get_hsst(static_vals):
    V = []
    A = []
    for i in range(1, len(static_vals)):
        xt = static_vals[i][0]
        xt1 = static_vals[i-1][0]
        
        yt = static_vals[i][1]
        yt1 = static_vals[i][1]
        
        t = static_vals[i][3]
        t1 = static_vals[i][3]
        dt = max(0.5, t-t1)
        dx = (xt-xt1)/dt
        dy = (yt-yt1)/dt
        v = math.sqrt(dx**2+dy**2)
        V.append(v)
    
    for i in range(1, len(V)):
        a = (V[i]-V[i-1])/(max(static_vals[i][3]-static_vals[i-1][3],0.5))
        A.append(a)
        
    Hist = []
    A_set = list(set(A))
    for a in A_set:
        Hist.append((a,A.count(a)))
    
    return Hist


def get_dst(dynamic_vals):
    V = []
    A = []
    for i in range(1, len(dynamic_vals)):
        xt = dynamic_vals[i][0]
        xt1 = dynamic_vals[i-1][0]
        
        yt = dynamic_vals[i][1]
        yt1 = dynamic_vals[i][1]
        
        t = dynamic_vals[i][3]
        t1 = dynamic_vals[i][3]
        dt = max(0.5, t-t1)
        dx = (xt-xt1)/dt
        dy = (yt-yt1)/dt
        v = math.sqrt(dx**2+dy**2)
        V.append(v)
    
    for i in range(1, len(V)):
        a = (V[i]-V[i-1])/(max(dynamic_vals[i][3]-dynamic_vals[i-1][3], 0.5))
        A.append(a)
        
    
    Hist = []
    A_set = list(set(A))
    for a in A_set:
        Hist.append((a,A.count(a)))
    
    return Hist
    
def get_dah(Hsst, Hdst):
    ans = 0
    for i in range(min(len(Hsst), len(Hdst))):
        ans+=(Hsst[i][1]-Hdst[i][1])**2
    return ans/min(len(Hsst), len(Hdst))

def get_probability(static_vals, dynamic_vals, circle_vals):
    
    Hsst = get_hsst(static_vals)
    Hdst = get_dst(dynamic_vals)
    DAH = get_dah(Hsst, Hdst)
    print(DAH)
    if DAH<0.3:
        return "High chance"
    if DAH>=0.3 and 1.3>DAH:
        return "Medium chance"
    else:
        return "No to Low chance"




@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        data1 = request.form['data1']
        data1 = json.loads(data1)
        print(data1,end="\n###\n\n")

        data2 = request.form['data2']
        data2 = json.loads(data2)
        print(data2,end="\n###\n\n")

        data3 = request.form['data3']
        data3 = json.loads(data3)
        print(data3,end="\n###\n\n")
        
        # X = []
        # Y = []
        # Z = [0]*len(data)
        # TimeStamp = []
        # for i in range(len(data)):
        #         X.append(data[i][0])
        #         Y.append(data[i][1])
        #         TimeStamp.append(data[i][2])
        # nodes = json.loads(nodes)
        # a = load_model(X,Y,Z,TimeStamp)

        a = get_probability(data1,data2,data3)
        print(a)
        return str(a)
    else:
        return '<html>Hi</html>'
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = "5000",debug = True)
    # app.run(host='0.0.0.0')
