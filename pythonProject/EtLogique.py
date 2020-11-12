import matplotlib.pyplot as plt
class EtLogique:
    def __init__(self):
        self.listeInput = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.listeResult = [0, 0, 0, 1]

    def calcul(self):
        valErreurTotal = 0

        self.listeValeurErreur= [[0] * 10 for _ in range(10)]

        for w1 in range(-5, 5):
            for w2 in range(-5, 5):
                for i in range(0, 4):
                    T = self.listeInput[i].__getitem__(0) * w1 + self.listeInput[i].__getitem__(1) * w2
                    print(T)
                    if T <= 0:
                        y = 0
                    else:
                        y = 1
                    erreur = 0.5 * (y - self.listeResult[i]) * (y - self.listeResult[i])
                    #print(str(w1+5)+" , "+str(w2+5))
                    valErreurTotal = valErreurTotal + erreur
                    self.listeValeurErreur[w1+5][w2+5] = erreur



    def afficherListe(self):
        for e in self.listeValeurErreur:
            print(str(e) + " , ")

        plt.plot(self.listeValeurErreur)
        #plt.matshow(self.listeValeurErreur)
        plt.show()