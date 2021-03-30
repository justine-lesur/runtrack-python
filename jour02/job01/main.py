class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def sePresenter(self):
        print(self.nom)
        print(self.prenom)

P1 = Personne('Lesur', 'Justine')

P1.sePresenter()