from Beachball_game import Beachball_game
import pygame
import time

class Beachball_gui:
    def __init__(self):
        self.__screen = pygame.display.set_mode((1000,800))
        
        self.__image_ball = pygame.image.load("beachball.png")
        self.__image_player = pygame.image.load("player.png")
        self.__wall_color = [92,209,229]
        self.__deadzone_color = [255,0,0]
        self.__trampoline_color = [255,228,0]
        
        #give game the info about player's and ball's image size
        self.__beachball_game = Beachball_game([self.__image_ball.get_rect(),self.__image_player.get_rect()])
        
        #initializing clock
        self.__clock = pygame.time.Clock()
        self.__FPS = 60
        
        #selecting fonts
        self.__life_font = pygame.font.Font(None, 50)
        self.__life_pos = [10,10]
        
        self.__score_font = pygame.font.Font(None, 40)
        self.__score_pos = [10,60]
        
        #downloading sound
        pygame.mixer.init()
        self.__sound_hit_wall = pygame.mixer.Sound("hit_wall.wav")
        self.__sound_hit_deadzone = pygame.mixer.Sound("hit_deadzone.wav")
        self.__sound_hit_deadzone.set_volume(0.2)
        
    def run(self):
        while True:
            command = self.command_getter()
            game_info_ball_player_collide = self.__beachball_game.game_run(command)
            self.collide_sound(game_info_ball_player_collide[2])
            self.blit_main_object(game_info_ball_player_collide)
            self.blit_life_surface()
            self.blit_score_surface()
            pygame.display.flip()
            self.__clock.tick(self.__FPS)
    
    
    def command_getter(self):
        for event in pygame.event.get(): 
          if event.type == pygame.QUIT: 
                 return 'QUIT'
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:
                 return 'UP'
              elif event.key == pygame.K_LEFT:
                 return 'LEFT'
              elif event.key == pygame.K_RIGHT:
                 return 'RIGHT'
              elif event.key == pygame.K_a:
                 return 'SMASH'
              elif event.key == pygame.K_d:
                 return 'HANDLING'
          elif event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT:
                  return 'STOP_X_PLAYER'
              if event.key == pygame.K_RIGHT:
                  return 'STOP_X_PLAYER'
              
    def collide_sound(self,collide_boolean):
        if collide_boolean[0] == 1 or collide_boolean[1] ==1 or collide_boolean[3] == 1:
            self.__sound_hit_wall.play()
        elif collide_boolean[2] ==1:
            self.__sound_hit_deadzone.play()
            time.sleep(3)
              
    def blit_main_object(self,game_info_ball_player_collide):
        self.__screen.fill([255,255,255])
        self.__screen.fill(self.__wall_color, pygame.Rect(0,0,30,800))
        self.__screen.fill(self.__wall_color, pygame.Rect(970,0,30,800))
        self.__screen.fill(self.__wall_color, pygame.Rect(485,600,30,200))
        self.__screen.fill(self.__wall_color, pygame.Rect(0,0,1000,45))
        self.__screen.fill(self.__deadzone_color, pygame.Rect(30,770,455,30))
        self.__screen.fill(self.__trampoline_color, pygame.Rect(515,770,455,30))
        self.__screen.blit(self.__image_player, game_info_ball_player_collide[1])
        self.__screen.blit(self.__image_ball, game_info_ball_player_collide[0])         
                
    def blit_life_surface(self):
        life_surf = self.__life_font.render("LIFE : " + str(self.__beachball_game.life), 1, (255,0,0))
        self.__screen.blit(life_surf , self.__life_pos)
        
    def blit_score_surface(self):
        score_surf = self.__score_font.render("SCORE : " +str(self.__beachball_game.score), 1, (0,0,0))
        self.__screen.blit(score_surf, self.__score_pos)