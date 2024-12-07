from grille import Grille
from joueur import Joueur
class GameManager:
    def __init__(self):
        self.grille = Grille()
        self.joueur1 = Joueur()
        self.joueur2 = Joueur()

    def ajouterJeton(self,colonne):
        print("Avant --------------")
        self.grille.affiche()
        self.grille.tab[0][colonne]=1
        print("Après --------------")
        self.grille.affiche()
