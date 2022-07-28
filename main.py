import pygame
import sys
import random
from pygame.locals import *
from platforms import Platforms
from player import Player



sprite_list = pygame.sprite.Group()
platform = pygame.sprite.Group()
player = ''



pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill((30, 0, 0))



def get_player_action():
  p1_action = {}
  p1_action['p1_jump'] = pygame.image.load("images/p1_jump.png").convert()
  p1_action['p1_jump'].set_colorkey((0,0,0))
  p1_action['p1_hurt'] = pygame.image.load("images/p1_hurt.png").convert()
  p1_action['p1_hurt'].set_colorkey((0,0,0))
  return p1_action
  


def init(p1_action):
  global player 
  for i in range(height//100):
    for j in range(width//410):
      plat = Platforms((random.randint(5, (width - 50) // 10)* 10, 120 * i), 'images/grassHalf.png', 70, 40)
      platform.add(plat)
  player = Player((platform.sprites()[-1].rect.centerx,platform.sprites()[-1].rect.centery-300), p1_action) 
  sprite_list.add(player)

  

def main():
  global player
  p1_action  = get_player_action()
  init(p1_action)
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_f:
          pygame.display.set_mode(size, FULLSCREEN)
        if event.key==pygame.K_ESCAPE:
          pygame.display.set_mode(size)
          

          
    screen.fill((30, 0, 30))
    platform.draw(screen)
    sprite_list.draw(screen)
    pygame.display.flip()



if __name__ == "__main__":
  main()



