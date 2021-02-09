# Beachball_game
from Beachball import Ball
from Player import Player
from Obstacles import Obstacles
import math
import pygame
#import time

class Beachball_game:
    def __init__(self,rect_init_info_ball_player):
        pygame.init()
        #creating ball and player1
        self.__ball = Ball()
        self.__player = Player()
        self.__ball.rect = rect_init_info_ball_player[0]
        self.__player.rect = rect_init_info_ball_player[1]
        self.__ball.initialize_position_velocity()
        self.__player.initialize_position_velocity()
        
        #creating Obstacles
        self.__wall_column_left = Obstacles()
        self.__wall_column_right = Obstacles()
        self.__wall_column_middle = Obstacles()
        self.__wall_beam_top = Obstacles()
        self.__wall_beam_middle = Obstacles()
        self.__deadzone = Obstacles()
        self.__trampoline = Obstacles()
        self.__wall_column_left.rect = pygame.Rect(0,0,30,770)
        self.__wall_column_right.rect = pygame.Rect(970,0,30,770)
        self.__wall_column_middle.rect = pygame.Rect(485,600,30,200)
        self.__wall_beam_top.rect = pygame.Rect(0,0,1000,45)
        self.__wall_beam_middle.rect = pygame.Rect(485,590,30,10)
        self.__deadzone.rect = pygame.Rect(30,770,455,30)
        self.__trampoline.rect = pygame.Rect(515,770,455,30)
        
        #grouping obstacles
        self.grouping_obstacles()
        
        #game factors
        self.__life = 50
        self.__score = 0
        
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        self.__score = score
        
    @property
    def life(self):
        return self.__life
    @life.setter
    def life(self,life):
        self.__life = life
        
            
    def grouping_obstacles(self):
        self.__group_column = pygame.sprite.Group()
        self.__group_column.add(self.__wall_column_left)
        self.__group_column.add(self.__wall_column_right)
        self.__group_column.add(self.__wall_column_middle)
        
        self.__group_beam = pygame.sprite.Group()
        self.__group_beam.add(self.__wall_beam_top)
        self.__group_beam.add(self.__wall_beam_middle)
        self.__group_deadzone = pygame.sprite.Group()
        self.__group_deadzone.add(self.__deadzone)
        
        self.__group_trampoline = pygame.sprite.Group()
        self.__group_trampoline.add(self.__trampoline)
        
        
        
    def game_run(self,command):    
        self.command_execute_player(command)
        collide_boolean = self.collide_check()
        self.collide_execute(collide_boolean)
        self.control_ball_max_speed()
        self.move_ball_player()
        self.__ball.gravity_accelerate()
        self.player_boundary_controller()
        self.__score = self.__score +1
        #give gui the info about position of ball,player and collide boolean
        return [self.__ball.rect,self.__player.rect,collide_boolean]
    
    def command_execute_player(self,command):
        if command == 'QUIT':
               pygame.quit()     
        elif command == 'UP':
              self.__player.ctrl_jump()
        elif command == 'LEFT':
              self.__player.ctrl_left()
        elif command == 'RIGHT':
              self.__player.ctrl_right()
              
        elif command == 'SMASH':
              distance_ball_player = self.distance_ball_player_calculator()
              if distance_ball_player < 200:
                 collide_angle = self.collide_angle_calculator()
                 self.__ball.smash(collide_angle)
                 
        elif command == 'HANDLING':
              distance_ball_player = self.distance_ball_player_calculator()
              if distance_ball_player < 200:
                  self.__ball.handling()
                  
        elif command == 'STOP_X_PLAYER':
            self.__player.zero_x_speed()
            
    def distance_ball_player_calculator(self):
        coordinate_ball = self.__ball.get_coordinate_ball_center()
        coordinate_player = self.__player.get_coordinate_center()
        distance_ball_player = math.sqrt((coordinate_ball[0]-coordinate_player[0])**2 + (coordinate_ball[1]-coordinate_player[1])**2)
        return distance_ball_player
    
    def collide_angle_calculator(self):
        coordinate_ball = self.__ball.get_coordinate_ball_center()
        coordinate_player = self.__player.get_coordinate_center()
        if coordinate_ball[0] - coordinate_player[0] == 0:
            return math.pi/2
        else:
            collide_angle = math.atan((coordinate_player[1]-coordinate_ball[1])/(coordinate_ball[0]-coordinate_player[0]))
            return collide_angle
                
    def collide_check(self):
        collide_boolean = [0,0,0,0] #column,beam,deadzone,trampoline 순
        cnt=0
        for checking_group in [self.__group_column,self.__group_beam,self.__group_deadzone,self.__group_trampoline]:
            if pygame.sprite.spritecollide(self.__ball,checking_group,False):
                collide_boolean[cnt] = 1
            cnt+=1
        return collide_boolean
    
    def collide_execute(self,collide_boolean):
        if collide_boolean[0] == 1:
            self.__ball.collide_column()
        if collide_boolean[1] == 1:
            self.__ball.collide_beam()
        if collide_boolean[2] == 1:
            self.collide_deadzone() #함수 이름 주의
        if collide_boolean[3] == 1:
            self.__ball.collide_trampoline()
            
    def collide_deadzone(self):
        #time.sleep(2.5)
        self.__life -= 1
        self.__ball.initialize_position_velocity()
        self.__player.initialize_position_velocity()
        if self.__life == 0:
            pygame.quit()
            
    def control_ball_max_speed(self):
        if self.__ball.speed[1] > 35:
            self.__ball.speed[1] = 35
        elif self.__ball.speed[1] < -35:
            self.__ball.speed[1] = -35
        else:
            return 0
        
        if self.__ball.speed[0] > 35:
            self.__ball.speed[0] = 35
        elif self.__ball.speed[0] < -35:
            self.__ball.speed[0] = -35
        
    def move_ball_player(self):
        self.__ball.move()
        self.__player.move()
        
    def player_boundary_controller(self):
        rect_player = self.__player.rect
        if rect_player.bottom < 550:
            self.__player.speed[1] = - self.__player.speed[1]
        if rect_player.bottom > 770:
            self.__player.speed[1] = 0
            self.__player.rect.bottom = 770
        if rect_player.left < 30 :
            self.__player.rect.left = 30
        if rect_player.right >= 485 :
            self.__player.rect.right = 480