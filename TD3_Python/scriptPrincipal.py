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


def afficherListeInput():
    print("Liste input : ")
    for element in listeInput:
        print(element)




def afficherListeOuput():
    print("Liste output avant : ")
    for element in listeOutput:
        print(element)

afficherListeInput()


afficherListeOuput()

#--------------------------------------------------------------------
#début keras
listeOutput = keras.utils.to_categorical(listeOutput,10) #ajout du 10= nb de classes à encoder qu'on avait oublié
#listeInput = np.reshape(listeInput,(9,1,7))


print("\n------------------------------------\nlisteOutput avec to_categorical :")
print(listeOutput)

#teachers
#teacher = np.array([1,1,1,1,1,1,1])
learningRate = SGD(lr=0.001)

#modele type séquentiel
modele = Sequential()

#ajout des couches
modele.add(Dense(10, input_dim=7, activation='relu'))
modele.add(Dense(64, input_dim=10,activation='relu'))
modele.add(Dense(64, input_dim=64,activation='relu'))
modele.add(Dense(64, input_dim=64,activation='relu'))
modele.add(Dense(64, input_dim=10,activation='relu'))
modele.add(Dense(64, input_dim=64,activation='relu'))
modele.add(Dense(64, input_dim=64,activation='relu'))
modele.add(Dense(10, input_dim=64, activation='softmax'))
modele.summary()

modele.compile(optimizer=learningRate, loss='categorical_crossentropy')# mean_squared_error #binary_crossentropy
modele.fit(listeInput,listeOutput, epochs=8000, batch_size=8)


#PREDICTION
predictions = modele.predict(listeInput)
print("prédiction : ")
#print([v[0] for v in predictions])

for row in predictions:
    max_row = np.max(row)
    for j in range(0,10):
        if row[j]==max_row:
            row[j]=1
        else:
            row[j]=0

print(predictions)
#[[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
