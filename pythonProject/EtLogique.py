import matplotlib.pyplot as plt

import numpy as np

class EtLogique:
    def __init__(self):
        self.listeInput = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.listeResult = [0, 0, 0, 1]

    def calcul(self):
        valErreurTotal = 0
        self.listeValeurErreur =np.zeros((10,10))

        for w1 in range(-5, 5):
            for w2 in range(-5, 5):
                for i in range(0, 4):
                    T = self.listeInput[i].__getitem__(0) * w1 + self.listeInput[i].__getitem__(1) * w2

                    if T <= 0:
                        y = 0
                    else:
                        y = 1

                    erreur = 0.5 * (y - self.listeResult[i])**2
                    valErreurTotal = valErreurTotal + erreur
                    self.listeValeurErreur[w1][w2] = erreur



    def afficherListe(self):
        for e in self.listeValeurErreur:
           print(str(e) + " , ")

        #plt.plot(self.listeValeurErreur)
        plt.imshow(self.listeValeurErreur)
        plt.show()