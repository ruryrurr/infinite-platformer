import pygame
from pygame.locals import*
import sys
pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

screen.fill((30, 0, 0))

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
    pygame.display.flip()



if __name__ == "__main__":
    main()



