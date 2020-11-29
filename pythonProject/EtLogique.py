import matplotlib.pyplot as plt

import numpy as np

class EtLogique:
    def __init__(self):
        self.listeInput = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.listeResult = [0, 0, 0, 1]

    def calcul(self):
        valErreurTotal = 0
        self.listeValeurErreur =np.zeros((20,20))

        for w1 in range(-10, 10,1):
            for w2 in range(-10, 10,1):
                for i in range(0, 4):
                    T = self.listeInput[i].__getitem__(0) * w1 + self.listeInput[i].__getitem__(1) * w2

                    if T > 0:
                        y = 1
                    else:
                        y = 0

                    erreur = 0.5 * (y - self.listeResult[i])**2
                    valErreurTotal = valErreurTotal + erreur
                    self.listeValeurErreur[w1][w2] = erreur

                #self.listeValeurErreur[w1+10][w2+10] = (np.sum(0.5*((((node[0]*w1)+(node[1]*w2))>0)-self.listeResult[node[0]*2+node[1]])**2 for node in self.listeInput))


    def afficherListe(self):

        for e in self.listeValeurErreur:
           print(str(e) + " , ")

        #plt.plot(self.listeValeurErreur)
        plt.imshow(self.listeValeurErreur)
        plt.show()