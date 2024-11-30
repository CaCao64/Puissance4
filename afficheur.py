import pygame 


class Afficheur:
    def init(self):
        self.running=True        
        print("Coucou")
        pygame.init()
        pygame.display.set_caption("Puissance 4")
        self.ecran=pygame.display.set_mode((1920, 1080))
    
    def affiche(self):
        while self.running :
            self.afficheGrille()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

    def afficheGrille(self):
        fond=pygame.image.load(r'C:\Caolan\Documents\Programmation\Puisssance4\Images\Plaque.png')
        self.ecran.blit(fond,(0,0))
