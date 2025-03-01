import pygame 
from grille import Grille

class Afficheur:
    largeurColonne=155
    def init(self,gameManager):
        self.running=True        
        print("Coucou")
        pygame.init()
        pygame.display.set_caption("Puissance 4")
        self.ecran=pygame.display.set_mode((1920, 1080))
        self.plaque=pygame.image.load(r'.\Images\Plaque.png')
        self.jeton=pygame.image.load(r'.\Images\JetonRouge.png')
        self.gameManager=gameManager
    
    def affiche(self):
        while self.running :
            self.afficheGrille()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onClick()

    def afficheGrille(self):
        self.ecran.blit(self.plaque,(0,0))
        # self.ecran.blit(self.jeton,(15,33)) #en haut à gauche
        # self.ecran.blit(self.jeton,(15,791)) #en bas à gauche
        # self.ecran.blit(self.jeton,(938,791)) #en bas à droite

        # g=self.gameManager.grille
        # for ligne in range(Grille.nbLignes-1,-1,-1):
        #     for colonne in range (Grille.nbColonnes):
        #          print(g.tab[ligne][colonne], end=' ')


    def onClick(self):
        position = pygame.mouse.get_pos()
        colonne = position[0]//Afficheur.largeurColonne
        print(position,colonne)
        self.gameManager.ajouterJeton(colonne)
        