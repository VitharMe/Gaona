#!/usr/bin/env python
import os
import pygame
import sys
from time import sleep
import RPi.GPIO as GPIO
from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    DISPLAY=pygame.display.set_mode((240,240),0,0)

    WHITE=(255,255,255)
    BLUE=(0,0,255)
    RED=(255,0,0)
    GREY=(220,220,220)
    HGREY=(105,105,105)
    DISPLAY.fill(WHITE)

    font = pygame.font.SysFont('Arial', 35)
    # First
    pygame.draw.rect(DISPLAY,HGREY,(25,15,200,50))
    pygame.draw.rect(DISPLAY,GREY,(20,10,200,50))
    DISPLAY.blit(font.render('Gaona\'s Bell', True, RED), (25, 15))
    FIRST='20,10'
    # Second
    pygame.draw.rect(DISPLAY,HGREY,(25,75,200,50))
    pygame.draw.rect(DISPLAY,GREY,(20,70,200,50))
    DISPLAY.blit(font.render('Second', True, RED), (25, 75))
    # Third
    pygame.draw.rect(DISPLAY,HGREY,(25,135,200,50))
    pygame.draw.rect(DISPLAY,GREY,(20,130,200,50))
    DISPLAY.blit(font.render('Third', True, RED), (25, 135))

    while True:
        UP = GPIO.input(23)
        DOWN = GPIO.input(24)
        if UP == False:
            pygame.draw.rect(DISPLAY, RED, (FIRST, 200, 50), 3)
        #if DOWN == False:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
