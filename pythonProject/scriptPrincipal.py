import csv
import character
import army
from random import *
import numpy as np


characters_list = []

with open('characters.csv', newline='') as fichier:
    a = csv.reader(fichier, delimiter=',', quotechar=',')
    for row in a:
       characters_list.append(character.Character(*row))

valTotal=0
for charac in characters_list:
    nb=uniform(20.0,100.0)
    armee =army.Army(charac,nb)
    valTotal+nb


print("Valeur totale des armées"+valTotal)
valeurMoraleTroupes=np.array([uniform(20.0,100.0),uniform(20.0,100.0),uniform(20.0,100.0),uniform(20.0,100.0),uniform(20.0,100.0)])
boostMoralTroupe=np.array([uniform(0.1,10.0),uniform(0.1,10.0),uniform(0.1,10.0),uniform(0.1,10.0),uniform(0.1,10.0)])


print(valeurMoraleTroupes)
print(boostMoralTroupe)