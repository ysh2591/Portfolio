import pygame

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__rect = pygame.Rect(0,0,0,0)
        
    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self,rect):
        self.__rect = rect