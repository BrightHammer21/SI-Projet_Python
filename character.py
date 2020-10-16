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
    def __repr__():
        print(nom+" "+prenom+" "+age+" "+profession+" "+boostMoral)

    #Accesseurs et mutateurs
    def getNom():
        return self.nom

    def getPrenom():
        return self.prenom

    def getAge():
        return self.age

    def getProfession():
        return self.profession

    def getBoostMoral():
        return self.boostMoral

    def setNom(nom):
        self.nom=nom

    def setPrenom(prenom):
        self.prenom=prenom

    def setAge(age):
        self.age=age

    def setProfession(prof):
        self.profession=prof

    def setBoostMoral(moral):
        self.boostMoral=moral
