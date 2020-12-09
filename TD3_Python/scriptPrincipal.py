import keras
import csv
import numpy as np
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense

#les listes
listeInput = np.zeros((9,7))
listeOutput = np.zeros(9)

#récupération des données
with open('donnees_segments.csv', newline='') as fichier:
    lignesRecupere = csv.reader(fichier, delimiter=' ', quotechar=' ')
    compteur=0
    compteur2=0
    for row in lignesRecupere:
        if compteur%2 == 0:
            for i in range(0,7):
                listeInput[compteur2][i] = row[i]
        else:
            listeOutput[compteur2]=row[0]
            compteur2 = compteur2 + 1
        compteur=compteur+1

print("Liste input : ")
def afficherListeInput():
    for element in listeInput:
        print(element)

print("Liste output : ")
def afficherListeOuput():
    for element in listeOutput:
        print(element)

afficherListeInput()
afficherListeOuput()

#--------------------------------------------------------------------
#début keras
listeOutput = keras.utils.to_categorical(listeOutput)
listeInput = np.reshape(listeInput,(9,1,7))

#teachers
#teacher = np.array([1,1,1,1,1,1,1])
learningRate = SGD(lr=0.001)

#modele type séquentiel
modele = Sequential()

modele.add(Dense(10, input_dim=7, activation='softmax'))
modele.summary()

modele.compile(optimizer=learningRate, loss='binary_crossentropy')
modele.fit(listeInput,listeOutput, epochs=100)


#PREDICTION
valeursAAvoir =  np.array([[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]])
predictions = modele.predict(valeursAAvoir)
print([v[0] for v in predictions])

#[[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
