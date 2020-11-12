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
        T = input1 * self.w1 +input2 * self.w2
        if T<=0:
            res=0
        else:
            res=1


        return res