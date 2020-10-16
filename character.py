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
