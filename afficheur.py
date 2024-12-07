import pygame 


class Afficheur:
    largeurColonne=155
    def init(self,gameManager):
        self.running=True        
        print("Coucou")
        pygame.init()
        pygame.display.set_caption("Puissance 4")
        self.ecran=pygame.display.set_mode((1920, 1080))
        self.fond=pygame.image.load(r'.\Images\Plaque.png')
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
        self.ecran.blit(self.fond,(0,0))

    def onClick(self):
        position = pygame.mouse.get_pos()
        colonne = position[0]//Afficheur.largeurColonne
        print(position,colonne)
        self.gameManager.ajouterJeton(colonne)
        