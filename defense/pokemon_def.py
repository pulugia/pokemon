import numpy as np
import pandas as pd
import os


poke_name = 'Latios' # input("Who's that pokemon! : ")
IV = [31, 0, 31, 31, 31, 31] # list(map(int, input("IV? : ").split(',')))
EV = [6, 0, 0, 252, 0, 252]   # list(map(int, input("EV? : ").split(',')))
Personality_name = 'Modest' #input('What is your pokemon's PERSONALITY! : ')

data_path = os.environ.get('DATAPATH')
if data_path is None:
    data_path = 'C:/Users/040/Desktop/docker/pokemon/data/'

pokemon = pd.read_csv(data_path + 'pokemon.csv')
Personality_df = pd.read_csv(data_path + 'Personality.csv')
df = pokemon.copy()
df.drop(['number', 'total', 'generation', 'legendary'], axis=1, inplace=True)

poke_type, poke_stats = df[df['name'] == poke_name].iloc[:, 1:3], df[df['name'] == poke_name].iloc[:, 3:]

Personality = Personality_df[Personality_df['Personality'] == Personality_name].iloc[:, 1:]

real_stats = []
real_stats.append(int(poke_stats.iloc[0, 0] + (IV[0]/2) + (EV[0]/8) + 60))
for i in range(1, 6):
    stat = (poke_stats.iloc[0, i] + (IV[i]/2) + (EV[i]/8) + 5) * Personality.iloc[:, i]
    stat = int(stat.values[0])
    real_stats.append(stat)


weight = 1
# Additional weight(ex:item, Ability)
# add_weight = [2] # list(map(int, input("Additional Weight? : ").split(',')))
# 
# for i in add_weight:
#     weight *= i


def_num = {}

def_num['physical'] = int(real_stats[0] * real_stats[2] * weight / 0.411)
def_num['special'] = int(real_stats[0] * real_stats[4] * weight / 0.411)


sav_data = [poke_type.values[0][0], poke_type.values[0][1], def_num['physical'], def_num['special']]
def_data = pd.read_csv(data_path + 'def_data.csv')
def_data = def_data.iloc[:, 1:]
def_data.loc[len(def_data)] = sav_data
def_data.to_csv(data_path + 'def_data.csv')