class perceptron:

    nbIpputs=0
    nbEpochs=0
    learningRate=0


    def __init__(self, nbIpputs, nbEpochs, learningRate):
        self.nbIpputs=nbIpputs
        self.nbEpochs=nbEpochs
        self.learningRate=learningRate