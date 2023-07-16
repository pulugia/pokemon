import numpy as np
import pandas as pd
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def print_res():
    data_path = os.environ.get('DATAPATH')
    if data_path is None:
        data_path = 'C:/Users/040/Desktop/docker/pokemon/data/'


    att_data = pd.read_csv(data_path + 'att_data.csv')
    def_data = pd.read_csv(data_path + 'def_data.csv')
    type_data = pd.read_csv(data_path + 'type_data.csv')

    att_type, att_class, att_dmg = att_data.iloc[len(att_data)-1, 1:]

    for t in def_data.iloc[len(def_data)-1, 1:3]:
        att_dmg *= type_data.loc[att_type, t]
        att_dmg = int(att_dmg)


    if att_class == 'physical':
        def_num = def_data.iloc[len(def_data)-1, 3]
        res = f'attack : {att_dmg} / defense : {def_num}'

    elif att_class == 'special':
        def_num = def_data.iloc[len(def_data)-1, 4]
        res = f'attack : {att_dmg} / defense : {def_num}'

    else:
        res = 'Error'

    return res

if __name__ == '__main__':
    app.run()