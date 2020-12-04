class perceptron:

    def __init__(self, nbIpputs, nbEpochs, learningRate, listeInput, listeResult):
        self.nbInputs = nbIpputs
        self.nbEpochs = nbEpochs
        self.learningRate = learningRate
        self.biais = 1

        # POIDS
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0
        self.w3 = 0
        self.w4 = 0
        self.w5 = 0
        self.w6 = 0
        self.w7 = 0
        self.wBiais = 0

        # ENTREES ET RESULT
        self.listeInputs = listeInput
        self.listeResult = listeResult

        self.listeDonnees = []