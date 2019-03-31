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
    fin = abs(100*(1-(DAH/100000)))
    if fin > 100:
       fin = random.randint(95, 99)
    return fin
    
    
    
