class Grille:
    nbColonnes = 7
    nbLignes = 6
    
    def __init__(self):
        # self.tab=[[None]*Grille.nbColonnes]*Grille.nbLignes

        self.tab=[[None]*Grille.nbColonnes for _ in range(Grille.nbLignes)]
        # for ligne in range(Grille.nbLignes):
        #     for colonne in range (Grille.nbColonnes):
        #         self.tab[ligne][colonne]=None

    def affiche(self):
        for ligne in range(Grille.nbLignes-1,-1,-1):
            #ligne=Grille.nbLignes-1-i
            #print(f"ligne = {ligne}")
            for colonne in range (Grille.nbColonnes):
                print(self.tab[ligne][colonne], end=' ')
            print('')