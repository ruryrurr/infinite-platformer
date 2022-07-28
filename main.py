import pygame
import sys
from pygame.locals import*

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

screen.fill((30, 0, 0))

sprite_list = pygame.sprite.Group()
platform = pygame.sprite.Group()


def main():
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



