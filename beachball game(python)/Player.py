import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__rect =pygame.Rect(0,0,0,0)
        self.__speed = [0,0]
        
    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self,rect):
        self.__rect = rect
        
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,speed):
        self.__speed = speed
        
    #methods

    def ctrl_left(self):
        self.__speed[0] = -8
        
    def ctrl_right(self):
        self.__speed[0] = 8
        
    def ctrl_jump(self):
        if self.__speed[1] == 0:
           self.__speed[1] = -10
           
    def move(self):
        self.__rect = self.__rect.move(self.__speed)

    def initialize_position_velocity(self):
        self.__speed = [0,0]
        self.__rect.left = 250
        self.__rect.bottom = 770
        
    def get_coordinate_center(self):
        coordinate_player_head = [self.__rect.centerx,self.__rect.centery]
        return coordinate_player_head
    
    def zero_x_speed(self):
        self.__speed[0] = 0