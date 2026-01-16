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
import random
width,height=1000,667
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('images/nfbg.jpg')
frog = pygame.transform.scale(pygame.image.load('images/idle01.png'),(96,96))
saw_size=(random.randint(32,50))#Saw size
saw = pygame.transform.scale(pygame.image.load('images/saw01.png'),(saw_size,saw_size)) #Random saw size
title=pygame.image.load('images/title.png')
instructions = pygame.image.load('images/instructions.png')
instructions2 = pygame.image.load('images/instructions2.png')
scrollspeed= 3
clock=pygame.time.Clock()
cords=(random.randrange(200,800),(random.randint(200,600)))#Random cooridnates for saw
#minecraft=pygame.font.Font('fonts/minecraft.ttf')
# *********GAME LOOP**********
game_state= "MENU"
text='Press <s> to start'
#exit loop
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state=='MENU':
            screen.blit(background,(0,0))
            #screen.blit(text,(200,300))
            screen.blit(instructions,(00,500))
            screen.blit(instructions2,(500,500))
            screen.blit(title,(0,100))
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state='PLAY'
        if game_state == 'PLAY':
            screen.blit(background,(0,0))
            screen.blit(frog,(50,500))
            screen.blit(saw,cords)
    pygame.display.flip()


    # *********EVENTS**********

   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********
