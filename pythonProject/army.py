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

    def get_total_moral(self):
        return int(self.getValeurMorale())*self.chef.getBoostMoral()

#surcharge méthode
    def __repr__(self):
        print(self.chef.__repr__()+" \nValeur morale : "+self.valeurMorale+" \nTotal moral"+self.get_total_moral())
