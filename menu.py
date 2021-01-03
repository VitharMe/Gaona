#!/usr/bin/env python
import os
import pygame
import sys
from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')
def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    DISPLAY=pygame.display.set_mode((240,240),0,0)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,BLUE,(20,20,150,200,))
    pygame.draw.rect(DISPLAY, (0, 100, 255), (50, 50, 162, 100), 3)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
