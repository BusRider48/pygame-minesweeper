#pygame minesweeper
#Tyler Wong
#June 13, 2023

import pygame
import time
import sys
import random
pygame.init()

#sets up display, colour variable for tiles, lists used for the game grid
screen=pygame.display.set_mode([610,610])
screen.fill((127,127,127))
square=(195,195,195)
grid=[]
mines=[]
flags=[]

#sets up images
mines1=pygame.image.load("mines1.png")
mines2=pygame.image.load("mines2.png")
mines3=pygame.image.load("mines3.png")
mines4=pygame.image.load("mines4.png")
mines5=pygame.image.load("mines5.png")
mines6=pygame.image.load("mines6.png")
mines7=pygame.image.load("mines7.png")
mines8=pygame.image.load("mines8.png")
flag1=pygame.image.load("flag.png")

#generates a random list for placement of mines
x=10
y=10
while x and y < 600:
    while x<600:
        ran=random.randrange(1,5)
        if ran==1:
            mines.append("x")
        else:
            mines.append("0")
        x+=30
    y+=30
    if y<600:
        x=10
x=10
y=10
while x and y < 600:
    while x<600:
        flags.append("0")
        x+=30
    y+=30
    if y<600:
        x=10
x=10
y=10
while x and y < 600:
    while x<600:
        grid.append(pygame.Rect(x,y,20,20))
        x+=30
    y+=30
    if y<600:
        x=10

fpsClock=pygame.time.Clock()
running=True

while running==True:
    
    #draws the grid onto the screen from list, tells the user if they won by placing flags in the correct tiles
    for i in grid:
        pygame.draw.rect(screen,square,i)
        n=grid.index(i)
        if flags[n]=="x":
            pygame.Surface.blit(screen,flag1,i)
            #pygame.draw.rect(screen,(64,64,64),i)
        if flags==mines:
            print("you win")
            
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        #sets up variables for mouse control
        mousepos=pygame.mouse.get_pos()
        mousebut=pygame.mouse.get_pressed()
        
        for i in grid:
            #reveals tiles on left click. for adjacency, exceptions are made for edges to get the correct number of adjacent mines
            if mousebut[0]==True:
                if i.collidepoint(mousepos[0],mousepos[1])==True:
                    n=grid.index(i)
                    if mines[n]=="x":
                        pygame.draw.rect(screen,(0,0,0),i)
                    num=0
                    if n==19 or n==39 or n==59 or n==79 or n==99 or n==119 or n==139 or n==159 or n==179 or n==199 or n==219 or n==239 or n==259 or n==279 or n==299 or n==319 or n==339 or n==359 or n==379 or n==399:
                        pass
                    else:
                        try:
                            if mines[n+1]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    if n==0 or n==20 or n==40 or n==60 or n==80 or n==100 or n==120 or n==140 or n==160 or n==180 or n==200 or n==220 or n==240 or n==260 or n==280 or n==300 or n==320 or n==340 or n==360 or n==380:
                        pass
                    else:
                        try:
                            if mines[n-1]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    if n==0 or n==20 or n==40 or n==60 or n==80 or n==100 or n==120 or n==140 or n==160 or n==180 or n==200 or n==220 or n==240 or n==260 or n==280 or n==300 or n==320 or n==340 or n==360 or n==380:
                        pass
                    else:
                        try:
                            if mines[n+19]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    if n==19 or n==39 or n==59 or n==79 or n==99 or n==119 or n==139 or n==159 or n==179 or n==199 or n==219 or n==239 or n==259 or n==279 or n==299 or n==319 or n==339 or n==359 or n==379 or n==399:
                        pass
                    elif n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 or n==10 or n==11 or n==12 or n==13 or n==14 or n==15 or n==16 or n==17 or n==18 or n==19:
                        pass
                    else:
                        try:
                            if mines[n-19]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    try:
                        if mines[n+20]=='x' and mines[n]!='x':
                            num+=1
                    except IndexError:
                        pass
                    if n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 or n==10 or n==11 or n==12 or n==13 or n==14 or n==15 or n==16 or n==17 or n==18 or n==19:
                        pass
                    else:
                        try:
                            if mines[n-20]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    if n==19 or n==39 or n==59 or n==79 or n==99 or n==119 or n==139 or n==159 or n==179 or n==199 or n==219 or n==239 or n==259 or n==279 or n==299 or n==319 or n==339 or n==359 or n==379 or n==399:
                        pass
                    else:
                        try:
                            if mines[n+21]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    if n==0 or n==20 or n==40 or n==60 or n==80 or n==100 or n==120 or n==140 or n==160 or n==180 or n==200 or n==220 or n==240 or n==260 or n==280 or n==300 or n==320 or n==340 or n==360 or n==380:
                        pass
                    elif n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 or n==10 or n==11 or n==12 or n==13 or n==14 or n==15 or n==16 or n==17 or n==18 or n==19:
                        pass
                    else:
                        try:
                            if mines[n-21]=='x' and mines[n]!='x':
                                num+=1
                        except IndexError:
                            pass
                    #replaces the drawn tiles with an image for the number of adjacent mines. if the user clicks on a tile that happens to be a mine, they are told they lost the game
                    match num:
                        case 1:
                            pygame.Surface.blit(screen,mines1,i)
                            #pygame.draw.rect(screen,(136,0,21),i)
                        case 2:
                            pygame.Surface.blit(screen,mines2,i)
                            #pygame.draw.rect(screen,(237,28,36),i)
                        case 3:
                            pygame.Surface.blit(screen,mines3,i)
                            #pygame.draw.rect(screen,(255,127,39),i)
                        case 4:
                            pygame.Surface.blit(screen,mines4,i)
                            #pygame.draw.rect(screen,(255,242,0),i)
                        case 5:
                            pygame.Surface.blit(screen,mines5,i)
                            #pygame.draw.rect(screen,(34,177,76),i)
                        case 6:
                            pygame.Surface.blit(screen,mines6,i)
                            #pygame.draw.rect(screen,(0,162,232),i)
                        case 7:
                            pygame.Surface.blit(screen,mines7,i)
                            #pygame.draw.rect(screen,(63,72,204),i)
                        case 8:
                            pygame.Surface.blit(screen,mines8,i)
                            #pygame.draw.rect(screen,(163,73,164),i)
                    if num==0 and mines[n]!='x':
                        pygame.draw.rect(screen,(255,255,255),i)
                    if mines[n]=="x":
                        print("you lose")
                    grid[n]=pygame.Rect(0,0,1,1)
            #right click replaces the drawn tiles with an image of a flag for the purpose of noting where mines are. flags are used for the win check
            if mousebut[2]==True:
                if i.collidepoint(mousepos[0],mousepos[1])==True:
                    n=grid.index(i)
                    if flags[n]=="0":
                        flags[n]="x"
                    else:
                        flags[n]="0"
                        
    pygame.display.flip()
    fpsClock.tick(60)
pygame.quit()
sys.exit()