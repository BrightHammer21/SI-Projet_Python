import csv
import character
import army
import perceptron
import EtLogique
from random import *
import numpy as np


characters_list = []

with open('characters.csv', newline='') as fichier:
    a = csv.reader(fichier, delimiter=',', quotechar=',')
    compteur =0
    for row in a:
        if (compteur!=0):
            characters_list.append(character.Character(*row))
        else:
            compteur = compteur +1


valTotal=0
for charac in characters_list:
    armee =army.Army(charac,uniform(20.0,100.0))
    valTotal=valTotal+armee.get_total_moral()

"""
print("Valeur totale des armées : "+str(valTotal))

valeurMoraleTroupes=np.array([uniform(20.0,100.0),uniform(20.0,100.0),uniform(20.0,100.0),uniform(20.0,100.0),uniform(20.0,100.0)])
boostMoralTroupe=np.array([uniform(0.1,10.0),uniform(0.1,10.0),uniform(0.1,10.0),uniform(0.1,10.0),uniform(0.1,10.0)])


print(valeurMoraleTroupes)
print(boostMoralTroupe)


et = EtLogique.EtLogique()
et.calcul()
et.afficherListe()

nbIpputs, nbEpochs, learningRate, listeInput, listeResult
"""

listeInput = [[0, 0], [0, 1], [1, 0], [1, 1]]
listeResult = [0, 0, 0, 1]

percept = perceptron.perceptron(2, 50, 0.01, listeInput, listeResult)
percept.train()