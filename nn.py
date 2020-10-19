import pandas as pd 
import numpy as np
import json

import plotly
import plotly.graph_objs as go

def model(df, feats_list, county):
    print(county)
    df_feats = df[feats_list + ['pos']].copy()
    for feat in feats_list:
        feat_mean = df_feats[feat].mean()
        feat_std = df_feats[feat].std()
        df_feats[feat] = (df_feats[feat] - feat_mean) / feat_std
    target = df_feats[df_feats['pos']==county][feats_list]
    distances = []
    for index, row in df_feats.iterrows():
        dist = 0
        for f in feats_list:
            dist += (float(target[f]) - float(row[f]))**2
        distances.append(np.sqrt(dist))
    df['distances'] = distances
    neighs = df[df['pos'] != county].sort_values('distances').iloc[:5]['pos'].to_list()
    return neighs 

    
