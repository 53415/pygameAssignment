'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:
https://stackoverflow.com/questions/64774900/how-to-get-velocity-x-and-y-from-angle-and-speed

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

import pygame
import math

pygame.init()

# *********SETUP**********

windowWidth = 1280
windowHeight = 720
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate
bahrainTrack = pygame.transform.scale(pygame.image.load("bahrain.png"), (12800,7200))
car = pygame.image.load("car.png")
speed = 10
trackX = -8150 
trackY = -6190
trackSize = 1
angle = 0
playerX = 500
playerY = 300



# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop
    
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
    
    # *********GAME LOGIC**********
    screen.blit(bahrainTrack, (trackX,trackY))
    screen.blit(pygame.transform.rotate(car, angle), (playerX, playerY))
    keys = pygame.key.get_pressed()


    if keys[pygame.K_a]:
        angle+=2

    if keys[pygame.K_d]:
        angle-=2

    angleRadians = math.radians(angle)
    xTravelled = speed * math.cos(angleRadians)
    yTravelled = speed * -math.sin(angleRadians)

    if keys[pygame.K_w]:
        trackX += xTravelled
        trackY += yTravelled
    elif keys[pygame.K_s]:
        trackX -= xTravelled
        trackY -= yTravelled

    print(angleRadians)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()