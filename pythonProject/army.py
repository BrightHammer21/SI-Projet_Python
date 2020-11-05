class Army:
    # ATTRIBUTS
    chef = ""
    valeurMorale = 0

    # constructeur
    def __init__(self, chefNom, valeurM):
        self.chef = chefNom
        self.valeurMorale = valeurM

    # GETTER ET SETTER
    def getChef(self):
        return self.chef

    def getValeurMorale(self):
        return self.valeurMorale

    def setChef(self, newChef):
        self.chef = newChef

    def setValeurmorale(self, newValue):
        self.valeurMorale = newValue

