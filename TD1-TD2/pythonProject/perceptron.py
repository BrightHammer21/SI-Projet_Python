import csv
class perceptron:

    def __init__(self, nbIpputs, nbEpochs, learningRate, listeInput, listeResult):
        self.nbInputs=nbIpputs
        self.nbEpochs=nbEpochs
        self.learningRate=learningRate
        self.biais = 1

        #POIDS
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0

        #ENTREES ET RESULT
        self.listeInputs = listeInput
        self.listeResult = listeResult

        self.listeDonnees = []


    def predict(self, input1, input2):
        res = 0
        T = input1 * self.w1 +input2 * self.w2 + self.biais * self.w0
        if T <= 0:
            res = 0
        else:
            res = 1

        return res

    def train(self):
        for i in range(0, self.nbEpochs):
            for j in range(0, len(self.listeInputs)):
                res = self.predict(self.listeInputs[j].__getitem__(0), self.listeInputs[j].__getitem__(1))
                self.w1 = self.w1 + self.learningRate *(self.listeResult[j] - res) * self.listeInputs[j].__getitem__(0)
                self.w2 = self.w2 + self.learningRate *(self.listeResult[j] - res) * self.listeInputs[j].__getitem__(1)
                self.w0 = self.w0 + self.learningRate *(self.listeResult[j] - res) * self.biais
                self.listeDonnees.append(res)
                print(res)

        self.sauvegardeDonnees()


    def sauvegardeDonnees(self):
        with open('sauvegardePerceptron2.csv', newline='', mode='w') as fichier:
                spamwriter = csv.writer(fichier, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(self.listeDonnees)


    def afficher(self):
        print(str(self.w1)+" "+str(self.w2))