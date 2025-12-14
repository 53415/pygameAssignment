'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)
Reference #1: https://stackoverflow.com/questions/64774900/how-to-get-velocity-x-and-y-from-angle-and-speed

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
import os
import time
pygame.init()

# *********SETUP**********

windowWidth = 1280
windowHeight = 720
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate
bahrainTrack = pygame.transform.scale(pygame.image.load("bahrain.png"), (12800,7200))
bahrainMinimap = pygame.transform.scale(pygame.image.load("BahrainMinimap.png"), (256,144))

car = pygame.image.load("ferrari.png")

ferrari = pygame.image.load("ferrari.png")
Mclaren = pygame.image.load("Mclaren.png")
Redbull = pygame.image.load("Redbull.png")
Mercedes = pygame.image.load("Mercedes.png")
Williams = pygame.image.load("Williams.png")
VCARB = pygame.image.load("VCARB.png")
AstonMartin = pygame.image.load("AstonMartin.png")
Haas = pygame.image.load("Haas.png")
Alpine = pygame.image.load("Alpine.png")
Sauber = pygame.image.load("Sauber.png")

tyresG = pygame.transform.scale(pygame.image.load("tyresG.png"), (60.5,90.5))
tyresY = pygame.transform.scale(pygame.image.load("tyresY.png"), (60.5,90.5))
tyresR = pygame.transform.scale(pygame.image.load("tyresR.png"), (60.5,90.5))
tyres = tyresG

treads1 = pygame.image.load("treads1.png")
treads2 = pygame.image.load("treads2.png")

car2 = pygame.image.load("car2.png")

speed = 0
trackX = -6685 
trackY = -6261
trackSize = 1
angle = 0
lap = 0
crossing = False
maxSpeed = 11
script_dir = os.path.dirname(os.path.abspath(__file__))
time = 0
lap1time = 0
lap2time = 0
lap3time = 0
font = pygame.font.Font(os.path.join(script_dir, "font.otf"), 28)
DRS = False
carDRS = pygame.image.load("FerrariDRS.png")
FLTW = 99
FLTWC = tyresG

FRTW = 99
FRTWC = tyresG

RLTW = 99
RLTWC = tyresG

RRTW = 99
RRTWC = tyresG

i = 0
# *********GAME LOOP**********
while True:
    time += clock.get_time() / 1000

    keys = pygame.key.get_pressed()

    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop
    if ev.type == pygame.KEYDOWN:  
        if ev.key == pygame.K_SPACE:  
            if DRS == False:
                if car == ferrari:
                    carDRS = pygame.image.load("FerrariDRS.png")
                elif car == Mclaren:
                    carDRS = pygame.image.load("MclarenDRS.png")
                elif car == Redbull:
                    carDRS = pygame.image.load("RedbullDRS.png")
                elif car == Mercedes:
                    carDRS = pygame.image.load("MercedesDRS.png")
                elif car == Williams:
                    carDRS = pygame.image.load("WilliamsDRS.png")
                elif car == VCARB:
                    carDRS = pygame.image.load("VCARBDRS.png")
                elif car == AstonMartin:
                    carDRS = pygame.image.load("AstonMartinDRS.png")
                elif car == Haas:
                    carDRS = pygame.image.load("HaasDRS.png")
                elif car == Alpine:
                    carDRS = pygame.image.load("AlpineDRS.png")
                elif car == Sauber:
                    carDRS = pygame.image.load("SauberDRS.png")
                DRS = True
            else:
                DRS = False   
               
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
    
    # *********GAME LOGIC**********
    screen.blit(bahrainTrack, (trackX,trackY))
    

    keys = pygame.key.get_pressed()


    if keys[pygame.K_a]:
        angle+=3
        FLTW -= 0.01
    if keys[pygame.K_d]:
        angle-=3
        FRTW -= 0.01
    
    # Reference #1
    angleRadians = math.radians(angle)
    xTravelled = round(speed * math.cos(angleRadians) ,0)
    yTravelled = round(speed * -math.sin(angleRadians) ,0)
    # End Reference #1
    
    trackX += xTravelled
    trackY += yTravelled

    if keys[pygame.K_1]:
        car =   Mclaren
        maxSpeed = 15
    elif keys[pygame.K_2]:
        car = Mercedes
        maxSpeed = 14.5
    elif keys[pygame.K_3]:
        car = Redbull
        maxSpeed = 14
    elif keys[pygame.K_4]:
        car = VCARB
        maxSpeed = 13.5
    elif keys[pygame.K_5]:
        car = ferrari
        maxSpeed = 13
    elif keys[pygame.K_6]:
        car = Williams
        maxSpeed = 12.5
    elif keys[pygame.K_7]:
        car = AstonMartin
        maxSpeed = 12
    elif keys[pygame.K_8]:
        car = Haas
        maxSpeed = 11.5
    elif keys[pygame.K_9]:
        car = Sauber
        maxSpeed = 11
    elif keys[pygame.K_0]:
        car = Alpine
        maxSpeed = 10.5

    if keys[pygame.K_s]:
        if speed > 0:
            speed -= 0.1

    if keys[pygame.K_w]:
        if speed < maxSpeed:
            speed += 0.1
        if RRTW >= 0 and RLTW >= 0:
            RLTW -= 0.01
            RRTW -= 0.01
    else:
        if speed > 0:
            speed -= 0.1
    

    if DRS:
        if keys[pygame.K_w] and speed < maxSpeed +5:
            speed += 0.2
    else:
        if speed > maxSpeed:
            speed -= 0.1

    if (round(trackX,0)) < -6600.0 and (round(trackX,0)) > -6650.0 and trackY > -6347 and trackY < -6034 and not crossing:
        lap += 1
        crossing = True


    
    if lap == 1:
        lap1time = round( time,2)
    elif lap == 2:
        lap2time = round(time - lap1time,2)

    elif lap == 3:
        lap3time =  round(time - lap2time - lap1time,2)
    if not ((round(trackX,0)) < -6600.0 and (round(trackX,0)) > -6650.0 and trackY > -6347 and trackY < -6034):
        crossing = False


    screen.blit(font.render(("lap # " + str(lap)), True, (255, 255, 255)) , (20, 20)) 
    screen.blit(font.render((str(int(20*speed))) + " km/h", True, (255, 255, 255)) , (600, 20)) 
    
    screen.blit(font.render(("lap 1: " +str(lap1time)), True, ("white")) , (1050, 20))
    if lap2time > 0:
        screen.blit(font.render(("lap 2: " +str(lap2time)), True, ("white")) , (1050, 50))
    if lap3time > 0:
        screen.blit(font.render(("lap 3: " +str(lap3time)), True, ("white")) , (1050, 80)) 

    
    if lap == 2:
        if lap1time < lap2time:
            screen.blit(font.render(("lap 1: " +str(lap1time)), True, (85, 26, 139)) , (1050, 20))
        else:
            screen.blit(font.render(("lap 2: " +str(lap2time)), True, (85, 26, 139)) , (1050, 50))

    if lap >= 3 :
        if lap1time < lap2time and lap1time < lap3time:
            screen.blit(font.render(("lap 1: " +str(lap1time)), True, (85, 26, 139)) , (1050, 20))
        else:
            if lap2time < lap3time:
                screen.blit(font.render(("lap 2: " +str(lap2time)), True, (85, 26, 139)) , (1050, 50))
            else:
                screen.blit(font.render(("lap 3: " +str(lap3time)), True, (85, 26, 139)) , (1050, 80))
    
    
    if FLTW > 80:
        FLTWC = tyresG
    elif FLTW > 50:
        FLTWC = tyresY
    else:
        FLTWC = tyresR
    if FRTW > 80:
        FRTWC = tyresG
    elif FRTW > 50:
        FRTWC = tyresY
    else:
        FRTWC = tyresR
    if RLTW > 80:
        RLTWC = tyresG
    elif RLTW > 50:
        RLTWC = tyresY
    else:
        RLTWC = tyresR
    if RRTW > 80:
        RRTWC = tyresG
    elif RRTW > 50:
        RRTWC = tyresY
    else:
        RRTWC = tyresR
    
    screen.blit((FLTWC), (1118, 510))
    screen.blit((FRTWC), (1200, 510))
    screen.blit((RLTWC), (1118, 610))
    screen.blit((RRTWC), (1200, 610))

    screen.blit(font.render(str(int(FLTW)), True, (255, 255, 255)) , (1130, 530))
    screen.blit(font.render(str(int(FRTW)), True, (255, 255, 255)) , (1215, 530))
    screen.blit(font.render(str(int(RLTW)), True, (255, 255, 255)) , (1130, 640))
    screen.blit(font.render(str(int(RRTW)), True, (255, 255, 255)) , (1215, 640))

    screen.blit((bahrainMinimap), (20, 550))

    if i < 1:
        screen.blit(pygame.transform.rotate(treads1, angle), (500, 300))
        i += 0.1
    elif i < 2:
        screen.blit(pygame.transform.rotate(treads2, angle), (500, 300))
        i += 0.1
    else:
        i = 0  
    

    if DRS:
        screen.blit(pygame.transform.rotate(carDRS, angle), (500, 300))
    else:
        screen.blit(pygame.transform.rotate(car, angle), (500, 300))

    minimapX = trackX / -50 + 25
    minimapY = trackY / -50 + 560
    pygame.draw.circle(screen, (255,0,0),(minimapX,minimapY ), 7)
    speed = round(speed,1)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()