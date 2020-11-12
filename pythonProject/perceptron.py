class perceptron:

    nbIpputs=0
    nbEpochs=0
    learningRate=0
    biais=1


    def __init__(self, nbIpputs, nbEpochs, learningRate):
        self.nbIpputs=nbIpputs
        self.nbEpochs=nbEpochs
        self.learningRate=learningRate

    def predict(self, input1, input2):
        res = 0

        if T<=0:
            res=0
        else:
            res=1


        return res