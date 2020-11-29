class perceptron:

    def __init__(self, nbIpputs, nbEpochs, learningRate, listeInput, listeResult):
        self.nbIpputs=nbIpputs
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



    def predict(self, input1, input2):
        res = 0
        T = input1 * self.w1 +input2 * self.w2 + self.biais * self.w0
        if T<=0:
            res=0
        else:
            res=1

        return res

    def train(self, listeInputs, listeResult):

        for i in range(0, self.nbEpochs):
            for j in range(0, self.listeInputs):
                res = self.predict(self.listeInputs[j].__getitem__(0), self.listeInputs[j].__getitem__(1))
                if res == 1:
                    self.w1 = self.w1 + self.learningRate *(self.listeResult[j] - res) * self.listeInputs[j].__getitem__(0)
                    self.w2 = self.w2 + self.learningRate *(self.listeResult[j] - res) * self.listeInputs[j].__getitem__(1)


    def afficher(self):
        print(self.w1+" "+self.w2)