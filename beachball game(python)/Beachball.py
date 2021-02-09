import pygame
import math
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__rect = pygame.Rect(0,0,0,0)
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
       
    def collide_column(self):
        self.__speed[0] = - self.__speed[0]
        self.__speed[1] = self.__speed[1]
        
    def collide_beam(self):
        self.__speed[0] = self.__speed[0]
        self.__speed[1] = - self.__speed[1]
        
    def collide_trampoline(self):
        self.__speed[0] = self.__speed[0] + random.choice([-5,-4,-3,3,4,5])
        self.__speed[1] = - self.__speed[1]
        
    def handling(self):
        self.__speed[0] = random.choice(range(-5,5))
        self.__speed[1] = - random.choice(range(30,32))
        
        
    def smash(self, collide_angle):
        impact_smash = 35
        if collide_angle >0:
            self.__speed[0] = -self.__speed[0] + impact_smash * math.cos(collide_angle) + 10
            self.__speed[1] = self.__speed[1] - impact_smash * math.sin(collide_angle) - 5
        elif collide_angle < 0:
            self.__speed[0] = -self.__speed[0] - impact_smash * math.cos(collide_angle) - 10
            self.__speed[1] = self.__speed[1] + impact_smash * math.sin(collide_angle) - 5
          
       
    def initialize_position_velocity(self):
        self.__speed = [random.choice([-5,5]), random.choice([1,-1])]
        self.__rect.left = 700
        self.__rect.top = 400
        
    def move(self):
        self.__rect = self.__rect.move(self.__speed)
        
    def get_coordinate_ball_center(self):
        coordinate_ball_center = [self.__rect.centerx,self.__rect.centery]
        return coordinate_ball_center
    
    def gravity_accelerate(self):
        self.__speed[1] += 1.2 
        
        
        
#충돌각은 라디안 단위