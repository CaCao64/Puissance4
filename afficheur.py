import pygame 


class Afficheur:
    def init(self):
        self.running=True        
        print("Coucou")
        pygame.init()
        pygame.display.set_caption("Insérer le titre")
        pygame.display.set_mode((1920, 1080))
    
    def affiche(self):
        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
