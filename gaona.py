#!/usr/bin/env python
def graph():
    import os
    import pygame
    from time import sleep
    import matplotlib
    # Execute without X
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    # Enable TFT
    os.putenv('SDL_FBDEV', '/dev/fb1')

    pygame.init()
    pygame.mouse.set_visible(False)
    lcd = pygame.display.set_mode((240, 240))

    while True:
        # Create some data
        x, y = [], []
        for line in open('last.txt', 'r'):
          values = [float(s) for s in line.split()]
          x.append(values[0])
          y.append(values[1])

        # Create a new figure, and set the style
        fig=plt.figure()
        plt.style.use('dark_background')


        # Plot the data and set the labels with title
        plt.plot(x,y,color='r')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gaona's Bell",color='r')

        # Resize
        figure = plt.gcf()
        figure.set_size_inches(2, 2)

        # Save the figure to a file
        plt.savefig("output.png", dpi=100)
        #os.system('kill -9 `pidof fbi`;fbi -T 2 -d /dev/fb1 -noverbose -a output.png')
        img = pygame.image.load('output.png')
        #lcd.blit(img, (0,0))
        lcd.blit(pygame.transform.scale(img, (240,240)), (0,0))
        pygame.display.update()
        sleep(0.1)

if __name__ == '__main__':
    graph()
