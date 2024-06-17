import pygame 
import sys
import random


pygame.init()



global menuRun
menuRun = False
titleRun = False
        
        
        
        
#Get the random words    
#gets words with length 1,2 or 3
def convert123():
    f123= open("word123.txt","r")
    if f123.mode == 'r':
        contents = f123.read()           
    lst = [contents]
    split =  (lst[0].split())
    return split
#gets words with length 4,5,6
def convert456():
    f456= open("word456.txt","r")
    if f456.mode == 'r':
        contents = f456.read()
    lst = [contents]
    split = (lst[0].split())
    return split
#words with length 7,8,9
def convert789():
    f789= open("word789.txt","r")
    if f789.mode == 'r':
        contents = f789.read()
    lst = [contents]
    split = (lst[0].split())
    return split
#words with length 10,11,12
def convert101112():
    f101112 = open("word101112.txt","r")
    if f101112.mode == 'r':
        contents = f101112.read()
    lst = [contents]
    split=(lst[0].split())
    return split
#words with length 13,14,15
def convert131415():
    f131415 = open("word131415.txt","r")    
    if f131415.mode == 'r':
        contents = f131415.read()
    lst = [contents]
    split = (lst[0].split())
    return split


white = (255,255,255)

#run game boolean
run = True

#print points scored
global points2
points2 = 0

#make display /window
x = 1024
y=768
x1 = 0
y1 = 0
x2 = 150
y2 = 350
vel = 10
z=[x,y]
win = pygame.display
color = (255,255,255)
big = 50
win.set_caption('My Window')
surface = win.set_mode(z)
myfont10 = pygame.font.SysFont("monospace",50)




rx = 1050

ry = 500

myfont2 = pygame.font.SysFont("monospace",30)
myfont3 = pygame.font.SysFont("monospace",22) 

#rules of game
def rule():
    myfont11 = pygame.font.SysFont("monospace",25)
    
    backgroundSurface= pygame.image.load("space.jpg")
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)        
        
        surface.blit(backgroundSurface,(0,0))
        
        howToPlay = myfont10.render("How To Play",1,color)
        one = myfont2.render("Words you type will be at the bottom of the screen",1,color)        
        two = myfont2.render("Type the words at the top of the screen",1,color)
        three = myfont2.render("Type words correctly to change direction",1,color)
        four = myfont2.render("Hitting anything will make you lose",1,color)
        space = myfont11.render("Press space to continue",1,color)
        
        surface.blit(space,(340, 600))        
        surface.blit(one,(60,200))
        surface.blit(two,(150,275))
        surface.blit(three,(150,350))
        surface.blit(four,(200,425))
        surface.blit(howToPlay,(355,100))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  
            global run
            run=True
            game(ry)        
        
        win.update()
        
#title screen
def title():
    global titleRun
    titleRun=True
    tux = pygame.image.load('keyboarddark.jpg')
    tux = pygame.transform.scale(tux,(1024,768))
    myfont = pygame.font.SysFont("monospace",110)
    
    
    surface.fill(white)
    text1 = myfont.render("Typing",1,color)
    text3 = myfont2.render("By Steven Shi",1,color)
    text4 = myfont3.render("Press space to continue",1, color)
   
    surface.blit(tux,(0,0))
    
    
    surface.blit(text1,(323,180))
    surface.blit(text3,(340,320))
    surface.blit(text4,(370, 530))

   

#Main menu
   
def menu():
    global menuRun
    menuRun=True
    
    menuGame = pygame.Rect((453,370,130,40))
    menuResult = pygame.Rect((453,430,130,40))
    menuExit = pygame.Rect((453,490,130,40))
    
    python = pygame.image.load("new.jpg")
    python = pygame.transform.scale(python,(1024,768))          
    surface.blit(python,(0,0))
    
    myfont4 = pygame.font.SysFont("monospace",90)        
    myfont5 = pygame.font.SysFont("monospace",30)
    
    text5 = myfont4.render("Main Menu",1, color)
    text8 = myfont5.render("GAME",1,(0,0,0))
    text9 = myfont5.render("RESULTS",1,(0,0,0))
    
    
    
    
    textX = myfont5.render("EXIT",1,(0,0,0))
    
    surface.blit(text5,(280,90))       
    
    
    #if mouse is hovered over button, change to yellow
    light = True
    while light:
        hoverx,hovery = pygame.mouse.get_pos()
    
        
    
        
    
        
        if menuGame.collidepoint(hoverx,hovery):
            pygame.draw.rect(surface,(255,255,0),menuGame)
        else:
            pygame.draw.rect(surface,(255,255,255),menuGame)
        surface.blit(text8,(480,375))  
    
       
    
        if menuExit.collidepoint(hoverx,hovery):
            pygame.draw.rect(surface,(255,255,0),menuExit)
        else:
            pygame.draw.rect(surface,(255,255,255),menuExit)
    
        surface.blit(textX,(480, 495))  
        
        #If button is pressed down
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if menuGame.collidepoint(mx,my):
                    rule()
                    global run
                    run=True
                    game(ry)
                    
                if menuExit.collidepoint(mx,my):
                    pygame.quit()
                    sys.exit(0)
                
       
        
        win.update()    
    
    

#game
def game(ry):
    string = ""
    points = 0
    level = 0
    rx=1050
    rx2=1500
    rx3 = 1950
    
    l1 = random.randint(0, 348)
    l2 = random.randint(0, 348)
    l3 = random.randint(0,348)
    direction = -2
    ship = pygame.image.load("rocket3.png")
    ship = pygame.transform.scale(ship,(25,25))    
    backgroundSurface= pygame.image.load("space.jpg")
    backgroundSurface = pygame.transform.scale(backgroundSurface,(1024,768))   
    n = random.randint(0,89)
    n2 = random.randint(0,44) 
    pygame.mixer.music.load("videoplayback.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  
    
    global run
    
                  
        
    while run: 
        
        
        count=0
        y = 110
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
              
       
        if event.type == pygame.QUIT:
            run = False
        else:
            #move character
            ry+=direction
            
            #move obstacles
            rx-=2
            rx2-=2
            rx3-=2
            
            #spaces blocks and makes length of blocks random
            if rx<-6:
                rx = rx3+450
                l1 = random.randint(50,348)
            if rx2<-6:
                rx2=rx+450
                l2 = random.randint(50,348)
            if rx3<-6:
                rx3=rx2+450
                l3 = random.randint(50,348)
            
        
        #hitbox of character
        hitbox = pygame.draw.rect(surface,(255,0,0),(50,ry,25,25))        
        
        surface.blit(backgroundSurface, (0,0))
        collide1(rx,rx2,rx3,l1,l2,l3,hitbox,points)     
    
        #Top box
        top=pygame.draw.rect(surface,(0,0,0),(0,658,1024,110))
        #bottom box
        bottom=pygame.draw.rect(surface,(0,0,0),(0,0,1024,110))
        collide2(top,bottom,hitbox,points)
        
        #display typed words on screen
        text = myfont10.render(string, 1, color) 
        
        #Word to type to change direction
        wanted = ""
        #Generate random words. Words get harder as time goes on
        if points <=14:
            wanted += convert123()[n]
            
        if points >= 15 and points <= 44:
            wanted += convert456()[n]
            
        if points >= 45 and points <= 74:
            wanted += convert789()[n]
            
            
        if points >= 75 and points <= 104:
            wanted += convert101112()[n]
            
        if points >= 105:
            wanted = convert131415()[n2]
            
            
        want = myfont10.render(wanted,1,color)
        surface.blit(want,(25,50))
        
        
    
        surface.blit(text, (5,685))
        surface.blit(ship,(50,ry))
        
        #Gets typed words from user
        if event.type == pygame.KEYDOWN:
    
            key = pygame.key.name(event.key) 
    
            if len(key) == 1:  
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    
                    string += key.upper()
                else:
                    string += key
            
            elif keys[pygame.K_BACKSPACE]: 
                string = string[:len(string) - 1]
            #If typed word is correct
            if string == wanted:
                direction*=-1
                points+=1
                ship = pygame.transform.flip(ship,False,True)
                ry+=direction                    
                string = "" 
                n = random.randint(0,89)
                n2 = random.randint(0,44)   
                
        #How many words you typed correctly
        point = myfont10.render(str(points),1,color)
        surface.blit(point, (512,50))
        
        
     
        
            
        

            
        
        win.update()

    #death screen
    if run == False:
        pygame.mixer.music.stop()
        
        death(points2)
        
        
   
        

    
    
    
        
    
    
       


#checks if collides with obstacles       
def collide1(rx,rx2,rx3,l1,l2,l3,hitbox,points):
    
    r1=pygame.draw.rect(surface,(255,255,255),(rx,110,30,l1))
    r1b = pygame.draw.rect(surface,(255,255,255),(rx,110+200+l1 ,30,600))
    r2=pygame.draw.rect(surface,(255,255,255),(rx2,110,30,l2))
    r2b=pygame.draw.rect(surface,(255,255,255),(rx2,110+200+l2,30,600))
    r3=pygame.draw.rect(surface,(255,255,255),(rx3,110,30,l3))
    r3b=pygame.draw.rect(surface,(255,255,255),(rx3,110+200+l3,30,600))
    
    #declare list somewhere else
    val = []
    val.append(r1)
    val.append(r1b)
    val.append(r2)
    val.append(r2b)
    val.append(r3)
    val.append(r3b)
    
    global run
    
    if hitbox.collidelist(val)!=-1:
        global points2  
        #variable to display points on death screen
        points2+=points
        run = False
        
        
#checks if it collides with bottom or top of screen
def collide2(top,bottom,hitbox,points):
    global run
    
    if hitbox.colliderect(top)==True or hitbox.colliderect(bottom)==True:
        global points2  
        #variable to display points on death screen
        points2+=points
        run=False
    
    
   
    





#Death screen
def death(points):
    retryR = pygame.Rect(465,400,120,35)   
    menuR = pygame.Rect(465,470,120,35)     
    backgroundSurface= pygame.image.load("space.jpg")
    death = myfont10.render("YOU DIED",1,color)
    score = myfont10.render("Your Score Was "+str(points),1,color)
       
    
    
    
    surface.blit(backgroundSurface,(0,0))  
    
    retry=myfont2.render("Retry",1,(0,0,0)) 
    
    menuWords = myfont2.render("Menu",1,(0,0,0))
    
    surface.blit(death,(395,110))
    surface.blit(score,(300,250))
    
    global points2
    points2=0
   
    
    light = True
    while light:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if retryR.collidepoint(mx,my):
                    global run
                    run=True
                    game(ry)
                if menuR.collidepoint(mx,my):
                    menu()
                    
        hoverx,hovery = pygame.mouse.get_pos()
        if menuR.collidepoint(hoverx,hovery):
            pygame.draw.rect(surface,(255,255,0),menuR)
        else:
            pygame.draw.rect(surface,(255,255,255),menuR)
            
        if retryR.collidepoint(hoverx,hovery):
            pygame.draw.rect(surface,(255,255,0),retryR)
        else:
            pygame.draw.rect(surface,(255,255,255),retryR)
            
        surface.blit(retry,(480,400))             
        surface.blit(menuWords,(490,470))           
        win.update()

#run title screen
title()









#Main Method
window = True
stop = True


while window:
    
    pygame.time.delay(100)
    #Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit")
            window = False
        
        
    
    keys = pygame.key.get_pressed()
    #Exit main menu
    if keys[pygame.K_SPACE] and titleRun==True:  
        menu()
        

    
        
        
        
    
        
        
    
    
    
    win.update()
    

    
pygame.quit()




