#!/usr/bin/env python
import os
import pygame
import sys
from time import sleep
import RPi.GPIO as GPIO
from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')

button_map = {23:(255,0,0), 24:(0,255,0)}

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
    pygame.draw.rect(DISPLAY, RED, (20, 10, 200, 50), 3)

    while True:
        for (k) in button_map.items():
            if GPIO.input(k) == False:
                DISPLAY.fill(v)
                if k == 23:
                    text_surface = font_big.render('Up', True, WHITE)
                else:
                    text_surface = font_big.render('Down', True, WHITE)
                rect = text_surface.get_rect(center=(120,120))
                DISPLAY.blit(text_surface, rect)
                pygame.display.update()
        sleep(0.1)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
