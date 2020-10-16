class Army: 

    #ATTRIBUTS
    self.chef=""
    self.valeurMorale=0

    #constructeur
    def __init__(self, chefNom, valeurM ):
        self.chef= chefNom
        self.valeurMorale = valeurMorale


    #GETTER ET SETTER
    def getChef():
        return self.chef

    def getValeurMorale():
        return self.valeurMorale
    
    def setChef(newChef):
        self.chef = newChef

    def setValeurmorale(newValue):
        self.valeurMorale = newValue
    
