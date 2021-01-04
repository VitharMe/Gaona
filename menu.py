#!/usr/bin/env python
def start():
    import os
    import pygame
    import sys
    from time import sleep
    import RPi.GPIO as GPIO
    from pygame.locals import *
    import gaona
    os.putenv('SDL_FBDEV', '/dev/fb1')

    button_map = {23:(0,85), 24:(100,0)}
    GPIO.setmode(GPIO.BCM)
    for k in button_map.keys():
        GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    def names():
        DISPLAY.blit(font.render('Gaona\'s Bell', True, BLACK), (25, 15))
        DISPLAY.blit(font.render('Second', True, BLACK), (25, 100))
        DISPLAY.blit(font.render('Exit', True, BLACK), (25, 185))
    def draws():
        # First
        pygame.draw.rect(DISPLAY,HGREY,(25,15,200,50))
        pygame.draw.rect(DISPLAY,GREY,(20,10,200,50))
        # Second
        pygame.draw.rect(DISPLAY,HGREY,(25,100,200,50))
        pygame.draw.rect(DISPLAY,GREY,(20,95,200,50))
        # Third
        pygame.draw.rect(DISPLAY,HGREY,(25,185,200,50))
        pygame.draw.rect(DISPLAY,GREY,(20,180,200,50))
    def selection():
        pygame.draw.rect(DISPLAY, SGREY, select)
    def motion(v):
        select.move_ip(v)
        pygame.draw.rect(DISPLAY, SGREY, select)
    def foo():
	foo.counter += 1
	return foo.counter
    pygame.init()
    pygame.mouse.set_visible(False)
    DISPLAY=pygame.display.set_mode((240,240),0,0)

    WHITE=(255,255,255)
    BLACK=(0,0,0)
    ORANGE=(252, 163, 17)
    BLUE=(0,0,255)
    RED=(255,0,0)
    GREY=(220,220,220)
    SGREY=(169,169,169)
    HGREY=(105,105,105)
    DISPLAY.fill(BLACK)
    font = pygame.font.SysFont('Arial', 35)
    select = Rect(20, 10, 200, 50)
    foo.counter = 0
    draws()
    selection()
    names()
    while True:
        for (k,v) in button_map.items():
            if GPIO.input(k) == False:
                if GPIO.input(23) == GPIO.LOW:
                    draws()
                    motion(v)
		    foo()
                    names()
                    if foo.counter >= 3:
			select = Rect(20, 10, 200, 50)
			foo.counter = 0
                        draws()
			selection()
			names()
                if GPIO.input(24) == GPIO.LOW:
		    if foo.counter == 0:
			img = pygame.image.load('bell.png')
			DISPLAY.blit(img, (0,0))
			pygame.display.update()
			gaona.graph()
		    if foo.counter == 1:
                        print("2")
		    if foo.counter == 2:
                        quit()
        pygame.display.update()
        sleep(0.2)
if __name__ == '__main__':
    start()