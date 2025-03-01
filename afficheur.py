import pygame 
from grille import Grille

class Afficheur:
    largeurColonne=153.83
    hauteurLigne=151.6
    offsetColonne=15
    offsetLigne=33

    def init(self,gameManager):
        self.running=True        
        pygame.init()
        pygame.display.set_caption("Puissance 4")
        self.ecran=pygame.display.set_mode((1920, 1080))
        self.imagePlaque=pygame.image.load(r'.\Images\Plaque.png')
        self.imageJetonRouge=pygame.image.load(r'.\Images\JetonRouge.png')
        self.imageJetonJaune=pygame.image.load(r'.\Images\JetonJaune.png')
        self.gameManager=gameManager
    
    def affiche(self):
        while self.running :
            self.afficheGrille(self.gameManager.grille)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onClick()

    def afficheGrille(self, grille):
        self.ecran.blit(self.imagePlaque,(0,0))

        for ligne in range(Grille.nbLignes-1,-1,-1):
            for colonne in range (Grille.nbColonnes):
                if grille.tab[ligne][colonne] != None:
                    self.afficheJeton(ligne,colonne,grille.tab[ligne][colonne])

    
    def afficheJeton(self,ligne,colonne,joueur):
        A=Afficheur
        x=A.offsetColonne+colonne*A.largeurColonne
        x=int(x)
        y=A.offsetLigne+(Grille.nbLignes-1-ligne)*A.hauteurLigne
        y=int(y)
        if joueur.numero == 1 :
            self.ecran.blit(self.imageJetonRouge,(x,y))
        else:
            self.ecran.blit(self.imageJetonJaune,(x,y))

    def onClick(self):
        position = pygame.mouse.get_pos()
        A=Afficheur
        colonne = int((position[0]-A.offsetColonne)//A.largeurColonne)
        print(position,colonne)
        self.gameManager.ajouterJeton(colonne)
        