#import keras
import csv
import numpy as np

'''
listeInput = []
listeOutput = []

with open('donnees_segments.csv', newline='') as fichier:
    lignesRecupere = csv.reader(fichier, delimiter=' ',quotechar=' ')
    compteur=0
    for row in lignesRecupere:
        if compteur%2==0:
            listeInput.append(row)
        else:
            listeOutput.append(*row)
        compteur=compteur+1

print("Liste input : ")
for element in listeInput:
    print(str(element)+" ")

print("Liste output : ")
for element in listeOutput:
    print(str(element)+" ")
'''


listeInput = np.zeros((9,7))
listeOutput = np.zeros(9)

with open('donnees_segments.csv', newline='') as fichier:
    lignesRecupere = csv.reader(fichier, delimiter=' ',quotechar=' ')
    compteur=0
    compteur2=0
    for row in lignesRecupere:
        if compteur%2==0:
            for i in range(0,7):
                listeInput[compteur2][i]=row[i]
        else:
            listeOutput[compteur2]=row[0]
        compteur=compteur+1
        compteur2=compteur2+1
