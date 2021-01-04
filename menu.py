#!/usr/bin/env python
import os
import pygame
import sys
from time import sleep
import RPi.GPIO as GPIO
from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')

button_map = {23:(0,60), 24:(100,0)}
GPIO.setmode(GPIO.BCM)
for k in button_map.keys():
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
    # Second
    pygame.draw.rect(DISPLAY,HGREY,(25,75,200,50))
    pygame.draw.rect(DISPLAY,GREY,(20,70,200,50))
    DISPLAY.blit(font.render('Second', True, RED), (25, 75))
    # Third
    pygame.draw.rect(DISPLAY,HGREY,(25,135,200,50))
    pygame.draw.rect(DISPLAY,GREY,(20,130,200,50))
    DISPLAY.blit(font.render('Third', True, RED), (25, 135))
    # Select
    select = Rect(20, 10, 200, 50)
    while True:
        for (k,v) in button_map.items():
            if GPIO.input(k) == False:
                # First
                pygame.draw.rect(DISPLAY,HGREY,(25,15,200,50))
                pygame.draw.rect(DISPLAY,GREY,(20,10,200,50))
                DISPLAY.blit(font.render('Gaona\'s Bell', True, RED), (25, 15))
                # Second
                pygame.draw.rect(DISPLAY,HGREY,(25,75,200,50))
                pygame.draw.rect(DISPLAY,GREY,(20,70,200,50))
                DISPLAY.blit(font.render('Second', True, RED), (25, 75))
                # Third
                pygame.draw.rect(DISPLAY,HGREY,(25,135,200,50))
                pygame.draw.rect(DISPLAY,GREY,(20,130,200,50))
                DISPLAY.blit(font.render('Third', True, RED), (25, 135))               
                select.move_ip(v)
                pygame.draw.rect(DISPLAY, RED, select, 3)
        pygame.display.update()
        sleep(1)
main()

