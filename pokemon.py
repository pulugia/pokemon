import numpy as np
import pandas as pd

poke_name = 'Latios' # input("Who's that pokemon! : ")
skill_name = 'Draco Meteor' # input("Go pokemon! : ")
IV = [31, 0, 31, 31, 31, 31] # list(map(int, input("IV? : ").split(',')))
EV = [6, 0, 0, 252, 0, 252]   # list(map(int, input("EV? : ").split(',')))
Personality_name = 'Modest' #input('What is your pokemon's PERSONALITY! : ')

pokemon = pd.read_csv('C:/Users/040/Desktop/docker/pokemon/pokemon.csv')
Personality_df = pd.read_csv('C:/Users/040/Desktop/docker/pokemon/Personality.csv')
skill_df = pd.read_csv('C:/Users/040/Desktop/docker/pokemon/pokemon_skill.csv')
df = pokemon.copy()
df.drop(['number', 'total', 'generation', 'legendary'], axis=1, inplace=True)

poke_type, poke_stats = df[df['name'] == poke_name].iloc[:, 1:3], df[df['name'] == poke_name].iloc[:, 3:]
skill_type, skill_class, skill_dmg = skill_df[skill_df['name'] == skill_name].iloc[:, 1:].values[0]


Personality = Personality_df[Personality_df['Personality'] == Personality_name].iloc[:, 1:]
real_stats = []

real_stats.append(int(poke_stats.iloc[0, 0] + (IV[0]/2) + (EV[0]/8) + 60))

for i in range(1, 6):
    stat = (poke_stats.iloc[0, i] + (IV[i]/2) + (EV[i]/8) + 5) * Personality.iloc[:, i]
    stat = int(stat.values[0])
    real_stats.append(stat)


weight = 1

if skill_type in poke_type.values:
    weight *= 1.5

if skill_type not in poke_type.values:
    pass

# Additional weight(ex:item, Ability)
# add_weight = [2] # list(map(int, input("Additional Weight? : ").split(',')))
# 
# for i in add_weight:
#     weight *= i


if skill_class == 'physical':
    damage = int((real_stats[1] * int(skill_dmg)) * weight)

if skill_class == 'special':
    damage = int((real_stats[3] * int(skill_dmg)) * weight)

print(damage)