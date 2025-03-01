from grille import Grille
from joueur import Joueur
class GameManager:
    def __init__(self):
        self.grille = Grille()
        self.joueur1 = Joueur('Player 1', 1)
        self.joueur2 = Joueur('Player 2', 2)
        self.joueurActif = self.joueur1

    def ajouterJeton(self,colonne):
        print("Avant --------------")
        self.grille.affiche()

        ligne=0
        while self.grille.tab[ligne][colonne] != None and ligne<Grille.nbLignes-1:
            ligne+=1
        
        self.grille.tab[ligne][colonne]=self.joueurActif
        if self.joueurActif == self.joueur1:
            self.joueurActif = self.joueur2
        else:
            self.joueurActif = self.joueur1
        print("Après --------------")
        self.grille.affiche()
