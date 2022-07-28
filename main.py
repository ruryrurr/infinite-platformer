import pygame
import sys
import random
from pygame.locals import*
from platforms import Platforms

sprite_list = pygame.sprite.Group()
platform = pygame.sprite.Group()

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

screen.fill((30, 0, 0))




def init():
  for i in range(height//100):
    for j in range(width//410):
      plat = Platforms((random.randint(5, (width - 50) // 10)* 10, 120 * i), 'images/grassHalf.png', 70, 40)
      platform.add(plat)



def main():
  init()
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



