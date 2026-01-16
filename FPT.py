'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

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



# *********SETUP**********
import pygame
width,height=1000,667
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('images/nfbg.jpg')
frog = pygame.image.load('images/idle01.png')
saw = pygame.image.load('images/saw01.png')
scrollspeed= 3
clock=pygame.time.Clock()
# *********GAME LOOP**********
#exit loop
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    pygame.display.flip()


    # *********EVENTS**********

   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********
