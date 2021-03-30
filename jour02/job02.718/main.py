class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def sePresenter(self):
        print(self.nom)
        print(self.prenom)

class Livre:
    
    def __init__(self, titre):
        self.titre = titre

    def Auteur(self):
        print(self.titre)

class Auteur(Personne):

    oeuvres = []

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        Personne.__init__(self, nom, prenom)

    def ecrireUnLivre(self, titre):
        self.titre = titre
        self.oeuvres.append(self.titre)
    
    def listerOeuvre(self):
        print(self.oeuvres)
        print(self.titre)

auteur = Auteur('justine', 'Lesur')
auteur.ecrireUnLivre('coucou')
auteur.listerOeuvre()