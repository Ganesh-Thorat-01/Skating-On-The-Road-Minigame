'''
env python3
Created on Fri Nov 06 2020
@author: Ganesh Thorat
-*-coding: utf-8 -*-

*Tip - To execute this program you should install pygame module in your machine.
        You can install it by following command in terminal "pip install pygame"
'''
#importing pygame module
import pygame
import random

#Creating main menu for game
def main_menu():
    global screen1
    

    pygame.init()
    pygame.display.set_caption("Skating On The Road")
    pygame.display.set_icon(pygame.image.load("Images\\icon.png"))
    screen1=pygame.display.set_mode((852,480))
    screen1.fill((0,0,0))

    font_menu=pygame.font.Font("freesansbold.ttf",30)
    text_menu=font_menu.render("M A I N   M E N U",True,"white")
    textRect_menu=text_menu.get_rect()
    textRect_menu.center=(426,200)

    font_start=pygame.font.Font("freesansbold.ttf",30)
    text_start=font_start.render("S T A R T",True,"white","sky blue")
    textRect_start=text_start.get_rect()
    textRect_start.center=(426,260)

    font_exit=pygame.font.Font("freesansbold.ttf",30)
    text_exit=font_exit.render("E X I T",True,"white","black")
    textRect_exit=text_exit.get_rect()
    textRect_exit.center=(426,300)


    running1=True
    while running1:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running1=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RIGHT and start_color=="sky blue" :
                    running1=False
                    gamestart()
                
                if event.key==pygame.K_DOWN:
                    running1=False
                    
        screen1.blit(text_menu,textRect_menu)
        screen1.blit(text_start,textRect_start)
        screen1.blit(text_exit,textRect_exit)
        
        pygame.display.update()

#creating game screen 
def gamestart():
    global screen
    pygame.init()
    pygame.display.set_caption("Skating On The Road")
    screen = pygame.display.set_mode((852, 480))
    gameloop()

#Handling Road Barrier movement and events
def Barrier():
    global barrier_x,barrier_x1
    global running,score,HI
    if barrier_x-barrier_x1<220 or barrier_x1-barrier_x<220:
        barrier_x-=1
        barrier_x1-=1
        bird_x=barrier_x1-160
        screen.blit(barrier,(barrier_x,320))
        screen.blit(barrier1,(barrier_x1,320))
        screen.blit(bird,(bird_x,170))
        if barrier_x<=-30:
            barrier_x=852
        if barrier_x1<=-30:
            barrier_x1=barrier_x+random.randrange(400,600)
        if barrier_x<186 and barrier_x>164 and y==260:
            if HI<score:
                HI=score
            score=0
            running=False
            gameover()

        elif barrier_x1<186 and barrier_x1>164 and y==260 :
            if HI<score:
                HI=score
            score=0
            running=False
            gameover()

        elif barrier_x1-140<=180 and barrier_x1-140>=140 and y==170:
            if HI<score:
                HI=score
            score=0
            running=False
            gameover()


#Creating Game over window having Game over text and score, when player strike to barrier  
def gameover():

    pygame.display.set_caption("Skating On The Road")
    screen3 = pygame.display.set_mode((852, 480))
    time1=5
    font_over=pygame.font.Font("freesansbold.ttf",30)
    text_over=font_over.render("G A M E  O V E R",True,"blue")
    textRect_over=text_over.get_rect()
    textRect_over.center=(426,200)
    running4=True
    while running4:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running4=False
        screen3.blit(bgimg,(0,0))
        screen3.blit(text_over,textRect_over)
        screen3.blit(text,(340,250))
        time1-=0.003
        if time1<=0:
            running4=False
            main_menu()
        pygame.display.update()

#displaying  player on game window
def player():
    global reg_player

    screen.blit(reg_player, (140, y))
    
#Displaying background image as its moving 
def background():
    global bgx
    global bgx1,barrier_x
    
    screen.blit(bgimg, (bgx, 0))
    screen.blit(bgimg1, (bgx1, 0))
    bgx -= 1
    bgx1 -= 1

    if bgx <= -852:
        bgx = 852
    if bgx1 <= -852:
        bgx1 = 852
    screen.blit(text,textRect)
    screen.blit(text1,textRect1)

#main game loop where all events of game will manage  
def gameloop():
    
    global running,bgimg,bgimg1,reg_player,barrier,barrier1,bgx,bgy,bgx1,y,barrier_x,barrier_x1,bird
    global text,textRect,score,text_over,textRect_over,text_start,textRect_start,HI,text1,textRect1
    bgx = 0
    bgy = 0
    bgx1 = 852
    barrier_x=852
    barrier_x1=852+random.randrange(200,500)
    y = 260
    score=0
    
    bgimg = pygame.image.load("Images\\bg.jpg").convert()
    bgimg1 = pygame.image.load("Images\\bg1.jpg").convert()

    reg_player = pygame.image.load("Images\\Player.png")
    reg_player = pygame.transform.scale(reg_player, (70, 140))

    barrier=pygame.image.load("Images\\barrier.png")
    barrier=pygame.transform.scale(barrier, (60, 110))

    barrier1=barrier
    
    bird=pygame.image.load("Images\\bird.png")
    bird=pygame.transform.scale(bird,(50,35))

    font=pygame.font.Font("freesansbold.ttf",30)
    text=font.render("SCORE : "+str(score),True,"red")
    textRect=text.get_rect()
    textRect.center=(550,50)

    font1=pygame.font.Font("freesansbold.ttf",30)
    text1=font1.render("HI : "+str(int(HI)),True,"red")
    textRect1=text1.get_rect()
    textRect1.center=(750,50)

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    
                    y=170

                if event.key==pygame.K_ESCAPE:
                    if score>HI:
                        HI=score
                    running=False
                    main_menu()
            if event.type == pygame.KEYUP:
                y = 260
            
        if score>HI:
            HI=score
        text=font.render("SCORE : "+str(int(score)),True,"red")
        text1=font1.render("HI : "+str(int(HI)),True,"red")
        score+=0.007
        background()
        player()
        Barrier()
        
        pygame.display.update()
        
HI=0
t=0

start_color="sky blue"
credit_color="black"
exit_color="black"
#calling main loop of game where game initialize
main_menu()