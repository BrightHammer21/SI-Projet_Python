class Character:

    #ATTRIBUTS
    nom=""
    prenom=""
    age=0
    profession=""
    boostMoral=0

    #constructeur
    def __init__(self, nom, prenom, age, profession, boostMoral):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.profession=profession
        self.boostMoral=boostMoral


    #surcharge méthode
    def __repr__(self):
        print(self.nom+" "+self.prenom+" "+self.age+" "+self.profession+" "+self.boostMoral)

    #Accesseurs et mutateurs
    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    def getBoostMoral(self):
        return self.boostMoral

    def setNom(self, nom):
        self.nom=nom

    def setPrenom(self, prenom):
        self.prenom=prenom

    def setAge(self, age):
        self.age=age

    def setProfession(self, prof):
        self.profession=prof

    def setBoostMoral(self, moral):
        self.boostMoral=moral
