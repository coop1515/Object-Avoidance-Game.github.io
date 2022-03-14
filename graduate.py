import pygame
from pygame.locals import *
import time
import sys
from os import path
import random
import math
from tkinter import *
from tkinter import messagebox

pygame.init()

display_width = 800 #화면 디스플레이 해상도 설정
display_height = 600 #화면 디스플레이 해상도 설정

screen = pygame.display.set_mode((display_width,display_height))
white = (255,255,255) #색깔 지정
BLACK = (0, 0, 0)  # R, G, B
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY = (0,191,255) # 폰트 색깔 설정
timer_font = pygame.font.SysFont('modernno20', 64) #사용할 폰트와 글자 크기 설정.

 # R, G, B, Alpha(투명도, 255 : 완전 불투명)
#gameDisplay = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load("images/ch3.png") #백그라운드 이미지 로드
pygame.display.set_caption('Object Avoidance Game') #프로그램 실행창 이름 설정.
#이미지 로드
titleImg = pygame.image.load("images/GameTitle.png")
startImg = pygame.image.load("images/clickedStartIcon.png")
quitImg = pygame.image.load("images/clickedQuitIcon.png")
settingImg = pygame.image.load("images/setting.png")
clickSettingImg = pygame.image.load("images/setting.png")
clickStartImg = pygame.image.load("images/clickedStartIcon.png")
clickQuitImg = pygame.image.load("images/clickedQuitIcon.png")
Imgsource = pygame.image.load("images/출처.png")
st1Img = pygame.image.load("images/st1.png")
st2Img = pygame.image.load("images/st2.png")
st3Img = pygame.image.load("images/st3.png")
st4Img = pygame.image.load("images/st4.png")
st5Img = pygame.image.load("images/st5.png")
FinishImg = pygame.image.load("images/Clear.png")
FailImg = pygame.image.load("images/Fail.png")
soundImg = pygame.image.load("images/소리.png")
soundonImg = pygame.image.load("images/소리on.png")
soundoffImg = pygame.image.load("images/소리off.png")
ChoiceImg = pygame.image.load("images/Choice.png")
remainImg = pygame.image.load("images/reamin.png")
restartImg = pygame.image.load("images/다시하기.png")
nextImg = pygame.image.load("images/nextlevel.png")
onImg = pygame.image.load("images/on.png")
offImg = pygame.image.load("images/off.png")
normalImg = pygame.image.load("images/normal.png")
hardImg = pygame.image.load("images/hard.png")

pygame.display.flip()

#배경음악
pygame.mixer.init()
pygame.mixer.music.load('Colors.mp3') #배경 음악
#pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
pygame.mixer.music.stop()
clock = pygame.time.Clock()

#게임 내 버튼 구현 클래스
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()

def mainmenu():
    display_width = 800
    display_height = 600
    background = pygame.image.load("images/111.jpg")
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(titleImg, (130,70))
        startButton = Button(startImg,300,300,150,74,clickStartImg,300,290,choicemenu)
        settingButton = Button(settingImg,300,400,200,74,settingImg,300,390,setting)
        quitButton = Button(quitImg,300,500,200,74,clickQuitImg,300,490,quitgame)
        pygame.display.update()
        clock.tick(15)

            # 화면 세로 가장 하단



def remainmenu_1(): #단계별 다시하기 창.

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FailImg, (200,50))
        restartButton = Button(restartImg,300,300,200,74,restartImg,300,290,gamestage1)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def remainmenu_2():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FailImg, (200,50))
        restartButton = Button(restartImg,300,300,200,74,restartImg,300,290,gamestage2)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def remainmenu_3():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FailImg, (200,50))
        restartButton = Button(restartImg,300,300,200,74,restartImg,300,290,gamestage3)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def remainmenu_4():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FailImg, (200,50))
        restartButton = Button(restartImg,300,300,200,74,restartImg,300,290,gamestage4)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def remainmenu_5():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FailImg, (200,50))
        restartButton = Button(restartImg,300,300,200,74,restartImg,300,290,gamestage5)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def clearmenu_1(): #클리어시 나오는 화면

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False
    
        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FinishImg, (200,50))
        nextButton = Button(nextImg,300,300,200,74,nextImg,300,290,gamestage2)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def clearmenu_2():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FinishImg, (200,50))
        nextButton = Button(nextImg,300,300,200,74,nextImg,300,290,gamestage3)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def clearmenu_3():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FinishImg, (200,50))
        nextButton = Button(nextImg,300,300,200,74,nextImg,300,290,gamestage4)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def clearmenu_4():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FinishImg, (200,50))
        nextButton = Button(nextImg,300,300,200,74,nextImg,300,290,gamestage5)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def clearmenu_5():

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(FinishImg, (200,50))
        nextButton = Button(nextImg,300,300,200,74,nextImg,300,290,gamestage6)
        startButton = Button(startImg,300,400,200,74,clickStartImg,300,390,choicemenu)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)


def choicemenu(): #스테이지 선택 창
    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    background = pygame.image.load("images/ch3.png")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainmenu()
        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(ChoiceImg, (210,30))
        stage1Button = Button(st1Img,150,200,109,100,st1Img,150,210,gamestage1)
        stage2Button = Button(st2Img,350,200,109,100,st2Img,350,210,gamestage2)
        stage3Button = Button(st3Img,550,200,109,100,st3Img,550,210,gamestage3)
        stage4Button = Button(st4Img,150,400,109,100,st4Img,150,410,gamestage4)
        stage5Button = Button(st5Img,350,400,109,100,st5Img,350,410,gamestage5)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        pygame.display.update()
        clock.tick(15)



def setting(): #옵션 창
    background = pygame.image.load("images/111.jpg")
    run = True
    while run:
        for event in pygame.event.get():
        
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        screen.fill(white)
        screen.blit(background, (0, 0))
        titletext = screen.blit(soundImg, (100,150))
        SoundButton1 = Button(soundonImg,350,150,150,75,soundonImg,350,140,soundon)
        SoundButton2 = Button(soundoffImg,550,150,150,75,soundoffImg,550,140,soundoff)
        remainButton = Button(remainImg,550,450,200,100,remainImg,550,440,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def soundon():
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play(-1)
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Object Avoidance Game','음악이 커졌습니다.')

def soundoff():
    if pygame.mixer.music.get_busy() == True:
        pygame.mixer.music.stop()
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Object Avoidance Game','음악이 꺼졌습니다.')


#sprite_group

game_folder = path.dirname(__file__)
image_folder = path.join(game_folder,'images')
TILESIZE = 64

class Sea(pygame.sprite.Sprite): # 바깥 테두리 타일
# 타일의 위치를 지정하기 위해 col과 row를 인자로 받아 타일의 위치를 지정해줄 것이다.
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
    # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, '2323.jpg')).convert_alpha()
        self.rect = self.image.get_rect()
    # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
class Ground(pygame.sprite.Sprite): # 바닥 타일
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
    # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'floor.png')).convert_alpha()
        self.rect = self.image.get_rect()
    # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
            
class Tree(pygame.sprite.Sprite): # 장애물 타일
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'tree.png')).convert_alpha()
        self.rect = self.image.get_rect()
        # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y   

class Item(pygame.sprite.Sprite): # 별 타일
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'Star.png')).convert_alpha()
        self.rect = self.image.get_rect()
        # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

class Door(pygame.sprite.Sprite): # 열쇠를 먹게되면 열리는 문 타일
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'tree.png')).convert_alpha()
        self.rect = self.image.get_rect()
        # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

class Key(pygame.sprite.Sprite): # 열쇠 타일
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'key.png')).convert_alpha()
        self.rect = self.image.get_rect()
        # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

class Spin(pygame.sprite.Sprite): # 회전하는 장애물
    def __init__(self,col,row):
        pygame.sprite.Sprite.__init__(self)
        #player의 이미지를 받아온다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'move.png')).convert_alpha()
        #player를 감싸는 사각형을 생성한다
        self.rect = self.image.get_rect()
        #player의 회전을 구현하기 위함
        self.rotate_angle = 0
        #player의 회전 속도
        self.rotate_speed = 5
        
        #player가 도는 궤도의 반지름
        self.orbit_radius = 150
        #player의 위치
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
        #play가 도는 궤도 중심의 위치
        self.orbit_pos_x = self.rect.x
        self.orbit_pos_y = self.rect.y

    def update(self): # 각 스테이지마다 사용할 회전하는 장애물 update로 구현.
        self.orbit_pos_x = 640 #self.rect.x
        self.orbit_pos_y = 384 #self.rect.y
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)

    def update2(self):
        self.orbit_pos_x = 640 #self.rect.x
        self.orbit_pos_y = 384 #self.rect.y
        self.orbit_radius = 75
        self.rotate_speed = -10
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)

    def update3(self):
        self.orbit_pos_x = 928 #self.rect.x
        self.orbit_pos_y = 416 #self.rect.y
        self.orbit_radius = 75
        self.rotate_speed = 7
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)
    
    def update4(self):
        self.orbit_pos_x = 928 #self.rect.x
        self.orbit_pos_y = 416 #self.rect.y
        self.orbit_radius = - 75
        self.rotate_speed = 7
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)

    def update5(self):
        self.orbit_pos_x = 740 #self.rect.x
        self.orbit_pos_y = 384 #self.rect.y
        self.orbit_radius = 100
        self.rotate_speed = 5
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)
    
    def update6(self):
        self.orbit_pos_x = 740 #self.rect.x
        self.orbit_pos_y = 384 #self.rect.y
        self.orbit_radius = -100
        self.rotate_speed = 5
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)

    def update7(self):
        self.orbit_pos_x = 540 #self.rect.x
        self.orbit_pos_y = 384 #self.rect.y
        self.orbit_radius = 100
        self.rotate_speed = 5
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)

    def update8(self):
        self.orbit_pos_x = 540 #self.rect.x
        self.orbit_pos_y = 384 #self.rect.y
        self.orbit_radius = -100
        self.rotate_speed = 5
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)

    
class Rectangle(pygame.sprite.Sprite): # 네모형태로 움직이는 장애물
    def __init__(self,col,row):
        pygame.sprite.Sprite.__init__(self)
        #player의 이미지를 받아온다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'move.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update(self):
            
        if self.grid_x < TILESIZE * 18:
            self.grid_x += 5
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 18:
            #self.grid_x += 0
            self.grid_y -= 5
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 3:
            #self.grid_y += 0
            self.grid_x -= 10
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 16:
            self.grid_x -= 5
            self.grid_y += 5
                
        if self.grid_x < TILESIZE * 16 and self.grid_y > TILESIZE * 8:
            self.grid_x += 5
            

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    
    def update2(self):
            
        if self.grid_x < TILESIZE * 6:
            self.grid_x += 5
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 6:
            self.grid_x += 0
            self.grid_y -= 5
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 4:
            self.grid_y += 0
            self.grid_x -= 10
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 4:
            self.grid_x -= 5
            self.grid_y += 5
                
        if self.grid_x < TILESIZE * 4 and self.grid_y > TILESIZE * 7:
            self.grid_x += 5
            
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update3(self):
            
        if self.grid_x < TILESIZE * 11:
            self.grid_x += 5
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 11:
            self.grid_x += 0
            self.grid_y -= 5
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 4:
            self.grid_y += 0
            self.grid_x -= 10
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 10:
            self.grid_x -= 5
            self.grid_y += 5
                
        if self.grid_x < TILESIZE * 10 and self.grid_y > TILESIZE * 7:

            self.grid_x += 5
            
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    
    def update4(self):
        if self.grid_x > TILESIZE * 4:
            self.grid_x -= 5
        
        if self.grid_x < TILESIZE * 4:
            self.grid_x += 0
            self.grid_y += 5
        
        if self.grid_y > TILESIZE * 7:
            self.grid_x += 10
            self.grid_y += 0

        if self.grid_x > TILESIZE * 6:
            self.grid_x += 5 
            self.grid_y -= 5

        if self.grid_x > TILESIZE * 6 and self.grid_y < TILESIZE * 4:
            self.grid_x -= 5

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update5(self):
        if self.grid_x < TILESIZE * 16:
            self.grid_x += 10
        
        if self.grid_x >= TILESIZE * 16:
            self.grid_y += 10

        if self.grid_y > TILESIZE * 10:
            self.grid_x -= 20
        
        if self.grid_x < TILESIZE * 3:
            self.grid_x -= 10
            self.grid_y -= 10
        
        if self.grid_x < TILESIZE * 3 and self.grid_y < TILESIZE * 9:
            self.grid_x += 10

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update6(self):
        self.grid_y += 5
        if self.grid_y > TILESIZE * 7:
            self.grid_y = TILESIZE * 4
            self.grid_x = self.rect.x + TILESIZE
        
        if self.grid_x > TILESIZE * 13:
            self.grid_x = TILESIZE * 6

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y



class Move(pygame.sprite.Sprite):  #직선으로 움직이는 장애물
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
            # 타일 한개당 위치를 좌표로 본다
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load(path.join(image_folder, 'move.png')).convert_alpha()
        self.rect = self.image.get_rect()
            # 타일 생성위치를 좌표에 대입
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

        

    def update(self):
        self.grid_y -= 5
           
        if self.grid_y <= 1 * TILESIZE:
            self.grid_y = self.grid_y + (TILESIZE * 8) #704
    
        self.rect.y = self.grid_y

    def update_2(self):
        self.grid_y -= 5
           
        if self.grid_y <= 1 * TILESIZE:
            self.grid_y = self.grid_y + (TILESIZE * 8) #704
    
        self.rect.y = self.grid_y
        
    def update2(self):
        self.grid_y += 5
           
        if self.grid_y >= 10 * TILESIZE:
            self.grid_y = self.grid_y - (TILESIZE * 8) #704
    
        self.rect.y = self.grid_y

    def update2_2(self):
        self.grid_y += 5
           
        if self.grid_y >= 10 * TILESIZE:
            self.grid_y = self.grid_y - (TILESIZE * 8) #704
    
        self.rect.y = self.grid_y    
    
    def update3(self):
        
        if self.grid_x < TILESIZE * 14:
            self.grid_x += 7
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 14:
            self.grid_x += 0
            self.grid_y -= 1
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 1:
            self.grid_y += 0
            self.grid_x -= 14
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 5:
            self.grid_x -= 0
            self.grid_y += 1
        

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    
    def update4(self):
        
        if self.grid_x < TILESIZE * 14:
            self.grid_x += 5
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 14:
            self.grid_x += 0
            self.grid_y -= 1
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 2:
            self.grid_y += 0
            self.grid_x -= 10
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 5:
            self.grid_x -= 0
            self.grid_y += 1
        

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update5(self):
        
        if self.grid_x < TILESIZE * 14:
            self.grid_x += 5
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 14:
            self.grid_x += 0
            self.grid_y -= 1
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 9:
            self.grid_y += 0
            self.grid_x -= 10
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 5:
            self.grid_x -= 0
            self.grid_y += 1
        

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update6(self):
        
        if self.grid_x < TILESIZE * 14:
            self.grid_x += 7
            #self.rect.x = self.grid_x
            
        if self.grid_x > TILESIZE * 14:
            self.grid_x += 0
            self.grid_y -= 1
            #self.rect.y = self.grid_y
        if self.grid_y < TILESIZE * 10:
            self.grid_y += 0
            self.grid_x -= 14
            #self.rect.x = self.grid_x
        if self.grid_x < TILESIZE * 5:
            self.grid_x -= 0
            self.grid_y += 1
        

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update7(self):

        self.grid_y -= 5
        if self.grid_y < TILESIZE * 2:
            self.grid_y = TILESIZE * 8

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    
    def update8(self):
        self.grid_y += 5
        if self.grid_y > TILESIZE * 8:
            self.grid_y = TILESIZE * 2

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    
    def update9(self):
        self.grid_x += 4
        self.grid_y += 0.5
        if self.grid_x > TILESIZE * 16:
            self.grid_x = TILESIZE * 6
            self.grid_y = TILESIZE * 1

        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update10(self):
        self.grid_x -= 4
        self.grid_y += 0.5
        if self.grid_x < TILESIZE * 6:
            self.grid_x = TILESIZE * 16
            self.grid_y = TILESIZE * 1
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    
    def update11(self):
        self.grid_x -= 2
        self.grid_y += 0.6
        if self.grid_x < TILESIZE * 16:
            self.grid_x = TILESIZE * 19
            #self.rect.y = TILESIZE #* 1
        
        if self.grid_y > TILESIZE * 7:
            self.grid_y = TILESIZE * 3
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update12(self):
        self.grid_y += 7
        if self.grid_y > TILESIZE * 9:
            self.grid_y = TILESIZE * 3

        self.rect.y = self.grid_y
    
    def update13(self):
        self.grid_y -= 7
        if self.grid_y < TILESIZE * 3:
            self.grid_y = TILESIZE * 9
        self.rect.y = self.grid_y

def gamestage1(): #게임 스테이지1의 창.
    display_width = 1280
    display_height = 768
    TILESIZE = 64
    screen = pygame.display.set_mode((display_width, display_height))
# 화면 타이틀 설정
    pygame.display.set_caption("Avoidance Game") # 화면설정 screen변수로 선언
# FPS
    clock = pygame.time.Clock()

# 배경 이미지 불러오기
    background = pygame.image.load("images/ch3.png")
    to_x = 0
    to_y = 0    
    
    class Player(pygame.sprite.Sprite): #게임을 할 플레이어 구현 클래스
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #player의 이미지를 받아온다
            self.image = pygame.image.load("images/char.png")
            #player를 감싸는 사각형을 생성한다
            self.rect = self.image.get_rect() 
            #play가 도는 궤도 중심의 위치
            self.orbit_pos_x = 0
            self.orbit_pos_y = 0
            #플레이어의 체력이다.
            self.hp = 3
            self.count = 0
            self.Level = 1
        def update(self): #플레이어 움직임 구현
            
            self.rect.centerx = self.orbit_pos_x
            self.rect.centery = self.orbit_pos_y
            keys = pygame.key.get_pressed()

            if (keys[pygame.K_a]):
                self.orbit_pos_x -= 5
            if (keys[pygame.K_d]):
                self.orbit_pos_x += 5
            if (keys[pygame.K_w]):
                self.orbit_pos_y -= 5
            if (keys[pygame.K_s]):
                self.orbit_pos_y += 5

            self.orbit_pos_x += to_x * dt
            self.orbit_pos_y += to_y * dt
            
            if self.rect.left <= TILESIZE * 5:
                self.rect.left = TILESIZE * 5 + 1
            if self.rect.right >= display_width - TILESIZE * 5:
                self.rect.right = display_width - TILESIZE * 5 - 1
            if self.rect.top <= TILESIZE * 2:
                self.rect.top = TILESIZE * 2 + 1
            if self.rect.bottom >= display_height - TILESIZE * 2:
                self.rect.bottom = display_height - TILESIZE * 2 - 1

        def tree_collide(self):
            collide_tree = pygame.sprite.spritecollide(self, tree_group, False)
            if collide_tree:
                self.orbit_pos_x = TILESIZE #10
                self.orbit_pos_y = TILESIZE #10
                # 체력이 1 깎인다.
                self.hp -= 1
                pygame.time.delay(200)
                    
        def sea_collide(self):
            collide_sea = pygame.sprite.spritecollide(self, sea_group, False)
            if collide_sea:
                # 바다에 부딪히면 바로 피가 0이 된다.
                self.hp = 0
        
        def item_collide(self):
            collide_item = pygame.sprite.spritecollide(self, item_group, False)
            collide_item2 = pygame.sprite.spritecollide(self, item2_group, False)
            collide_item3 = pygame.sprite.spritecollide(self, item3_group, False)
            if collide_item:
                item.kill()
                self.count += 1
            elif collide_item2:
                item2.kill()
                self.count += 1
            elif collide_item3:
                item3.kill()
                self.count += 1

        
                
    class Hp(pygame.sprite.Sprite):   
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/hp3.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 32

        def update(self):
            # hp가 줄어들 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.hp == 3:
                self.image = pygame.image.load("images/hp3.png")
            elif player.hp == 2:
                self.image = pygame.image.load("images/hp2.png")
            elif player.hp == 1:
                self.image = pygame.image.load("images/hp1.png")
            elif player.hp <= 0:
                self.image = pygame.image.load("images/hp0.png")
                remainmenu_1()
    
    class Star(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/star0.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 80

        def update(self):
            #count가 늘어날 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.count == 3:
                self.image = pygame.image.load("images/star3.png")
                clearmenu_1()
            elif player.count == 2:
                self.image = pygame.image.load("images/star2.png")
            elif player.count == 1:
                self.image = pygame.image.load("images/star1.png")
            #elif player.count == 0:
             #   self.image = pygame.image.load("images/star1.png")
    
# player을 생성
    player = Player()
    hp = Hp()
    count = Star()
    # sprite_group로 선언된 sprite의 Group()에 player를 넣는다.
    sprite_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sea_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    tree_group = pygame.sprite.Group()
    item_group = pygame.sprite.Group()
    item2_group = pygame.sprite.Group()
    item3_group = pygame.sprite.Group()

    # player의 처음 위치를 화면의 중간으로 설정한다.
    player.rect.x = TILESIZE * 2
    player.rect.y = TILESIZE * 2
    # 처음 player가 생성되었을 때 궤도가 정해져있지 않으므로 지정해준다. 
    player.orbit_pos_x = player.rect.x
    player.orbit_pos_y = player.rect.y
    
    map_data = []
    # map_file을 읽는다
    with open('map_file.txt', 'r') as file:
        for line in file:
        # 마지막 줄바꿈 기호까자 출력되므로 strip을 이용해 없애준다.
        # 그리고 띄어쓰기를 기준으로 한 행을 하나의 리스트로 만든 다음 그 리스트를 map_data에 추가해 2차원 리스트로 만들어준다
            map_data.append(line.strip('\n').split(' '))
    for col in range(0,len(map_data)):
        for row in range(0,len(map_data[col])):
            if map_data[col][row] == "s":
                sea = Sea(col, row)
                sprite_group.add(sea)
                
            if map_data[col][row] == "g":
                ground = Ground(col, row)
                sprite_group.add(ground)

            if map_data[col][row] == "t":
                tree = Tree(col, row)
                sprite_group.add(tree)
                #각각의 그룹에 맞게 추가해준다.
                tree_group.add(tree) #tree_group 닿으면 hp소모.

            if map_data[col][row] == "i": # 아이템
                item = Item(col,row)
                sprite_group.add(item)
                item_group.add(item)

            if map_data[col][row] == "i2": # 아이템
                item2 = Item(col,row)
                sprite_group.add(item2)
                item2_group.add(item2)
            if map_data[col][row] == "i3": # 아이템
                item3 = Item(col,row)
                sprite_group.add(item3)
                item3_group.add(item3)

                
            
    sprite_group.add(player)
    sprite_group.add(hp)
    sprite_group.add(count)

    def draw_grid():
	#0부터 TILESIZE씩 건너뛰면서 display_width까지 라인을 그려준다
        for x in range(0, display_width, TILESIZE):
    	#첫번째 인자부터 screen(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
            pygame.draw.line(screen, (0, 0, 0, 50), (x, 0), (x, display_height))
        for y in range(0, display_height, TILESIZE):
            pygame.draw.line(screen, (0, 0, 0, 50), (0, y), (display_width, y))
    start_time = time.time()
    
        
    running = True
    while running:
        dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
        for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                mainmenu() # 게임이 진행중이 아님
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainmenu()

            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0


        
        
        screen.fill(white)
        draw_grid()
        screen.blit(background, (0, 0)) # 배경 그리기
        sprite_group.draw(screen)
        real = time.time()-start_time
        text = timer_font.render(str(int(real)), True, SKY)
        screen.blit(text, (608, 0))
        player.update()
        hp.update()
        count.update()
        player.sea_collide()
        player.tree_collide()
        player.item_collide()
        if pygame.mixer.music.get_busy() == False:
            offButton = Button(offImg,1216,0,64,32,offImg,1216,0,soundon)
        elif pygame.mixer.music.get_busy() == True:
            onButton = Button(onImg,1216,0,64,32,onImg,1216,0,soundoff)

        pygame.display.update() # 게임화면을 다시 그리기!

def gamestage2():
    display_width = 1280
    display_height = 768
    TILESIZE = 64
    screen = pygame.display.set_mode((display_width, display_height))
# 화면 타이틀 설정
    pygame.display.set_caption("Avoidance Game") # 화면설정 screen변수로 선언
    
    
# FPS
    clock = pygame.time.Clock()

# 배경 이미지 불러오기
    background = pygame.image.load("images/ch3.png")
    to_x = 0
    to_y = 0
    
    
    
    
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #player의 이미지를 받아온다
            self.image = pygame.image.load("images/char.png")
            #player를 감싸는 사각형을 생성한다
            self.rect = self.image.get_rect()
            #play가 도는 궤도 중심의 위치
            self.orbit_pos_x = 0
            self.orbit_pos_y = 0
            #플레이어의 체력이다.
            self.hp = 3
            self.count = 0

        def update(self):
            
            self.rect.centerx = self.orbit_pos_x
            self.rect.centery = self.orbit_pos_y
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a]):
                self.orbit_pos_x -= 5
            if (keys[pygame.K_d]):
                self.orbit_pos_x += 5
            if (keys[pygame.K_w]):
                self.orbit_pos_y -= 5
            if (keys[pygame.K_s]):
                self.orbit_pos_y += 5

            self.orbit_pos_x += to_x * dt
            self.orbit_pos_y += to_y * dt
            

            if self.rect.left <= TILESIZE * 4:
                self.rect.left = TILESIZE * 4 + 1
            if self.rect.right >= display_width - TILESIZE * 4:
                self.rect.right = display_width - TILESIZE * 4 - 1
            if self.rect.top <= TILESIZE:
                self.rect.top = TILESIZE + 1
            if self.rect.bottom >= display_height - TILESIZE:
                self.rect.bottom = display_height - TILESIZE - 1

        def tree_collide(self):
            collide_tree = pygame.sprite.spritecollide(self, tree_group, False)
            if collide_tree:
                
                self.orbit_pos_x = TILESIZE * 2 #10
                self.orbit_pos_y = TILESIZE * 2 #10
                # 체력이 1 깎인다.
                self.hp -= 1
                pygame.time.delay(200)
                    
        def sea_collide(self):
            collide_sea = pygame.sprite.spritecollide(self, sea_group, False)
            if collide_sea:
                # 바다에 부딪히면 바로 피가 0이 된다.
                self.hp = 0
        
        def item_collide(self):
            collide_item = pygame.sprite.spritecollide(self, item_group, False)
            collide_item2 = pygame.sprite.spritecollide(self, item2_group, False)
            collide_item3 = pygame.sprite.spritecollide(self, item3_group, False)
            if collide_item:
                item.kill()
                self.count += 1
            elif collide_item2:
                item2.kill()
                self.count += 1
            elif collide_item3:
                item3.kill()
                self.count += 1
        
        def key_collide(self):
            collide_key = pygame.sprite.spritecollide(self, key_group, False)
            if collide_key:
                door.kill()
                door2.kill()
                key.kill()

                
    class Hp(pygame.sprite.Sprite):   
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/hp3.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 32

        def update(self):
            # hp가 줄어들 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.hp == 3:
                self.image = pygame.image.load("images/hp3.png")
            elif player.hp == 2:
                self.image = pygame.image.load("images/hp2.png")
            elif player.hp == 1:
                self.image = pygame.image.load("images/hp1.png")
            elif player.hp <= 0:
                self.image = pygame.image.load("images/hp0.png")
                remainmenu_2()
    
    class Star(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/star0.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 80

        def update(self):
            #count가 늘어날 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.count == 3:
                self.image = pygame.image.load("images/star3.png")
                clearmenu_2()
            elif player.count == 2:
                self.image = pygame.image.load("images/star2.png")
            elif player.count == 1:
                self.image = pygame.image.load("images/star1.png")
            #elif player.count == 0:
             #   self.image = pygame.image.load("images/star1.png")
                

# player을 생성
    player = Player()
    hp = Hp()
    count = Star()
    # sprite_group로 선언된 sprite의 Group()에 player를 넣는다.
    sprite_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sea_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    tree_group = pygame.sprite.Group()
    item_group = pygame.sprite.Group()
    item2_group = pygame.sprite.Group()
    item3_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()
    key2_group = pygame.sprite.Group()

    # player의 처음 위치를 화면의 중간으로 설정한다.
    player.rect.x = TILESIZE * 2
    player.rect.y = TILESIZE * 2
    # 처음 player가 생성되었을 때 궤도가 정해져있지 않으므로 지정해준다. 
    player.orbit_pos_x = player.rect.x
    player.orbit_pos_y = player.rect.y
    
    

    


        
        
            
    map_data = []
    # map_file을 읽는다
    with open('map_file2.txt', 'r') as file:
        for line in file:
        # 마지막 줄바꿈 기호까자 출력되므로 strip을 이용해 없애준다.
        # 그리고 띄어쓰기를 기준으로 한 행을 하나의 리스트로 만든 다음 그 리스트를 map_data에 추가해 2차원 리스트로 만들어준다
            map_data.append(line.strip('\n').split(' '))
    for col in range(0,len(map_data)):
        for row in range(0,len(map_data[col])):
            if map_data[col][row] == "s":
                sea = Sea(col, row)
                sprite_group.add(sea)
                
            if map_data[col][row] == "g":
                ground = Ground(col, row)
                sprite_group.add(ground)

            if map_data[col][row] == "t":
                tree = Tree(col, row)
                sprite_group.add(tree)
                #각각의 그룹에 맞게 추가해준다.
                tree_group.add(tree) #tree_group 닿으면 hp소모.

            if map_data[col][row] == "m1": # 움직이는장애물 1
                move = Move(col,row)
                sprite_group.add(move)
                tree_group.add(move)

            if map_data[col][row] == "m2": # 움직이는 장애물 2
                move2 = Move(col, row)
                sprite_group.add(move2)
                tree_group.add(move2)

            if map_data[col][row] == "m3": # 움직이는 장애물 2
                move3 = Move(col, row)
                sprite_group.add(move3)
                tree_group.add(move3)

            if map_data[col][row] == "m4": # 움직이는 장애물 2
                move4 = Move(col, row)
                sprite_group.add(move4)
                tree_group.add(move4)

            if map_data[col][row] == "i": # 아이템
                item = Item(col,row)
                sprite_group.add(item)
                item_group.add(item)

            if map_data[col][row] == "i2": # 아이템
                item2 = Item(col,row)
                sprite_group.add(item2)
                item2_group.add(item2)
                
            if map_data[col][row] == "i3": # 아이템
                item3 = Item(col,row)
                sprite_group.add(item3)
                item3_group.add(item3)

            if map_data[col][row] == "d": # 문
                door = Door(col,row)
                sprite_group.add(door)
                tree_group.add(door)

            if map_data[col][row] == "d2": # 문2
                door2 = Door(col,row)
                sprite_group.add(door2)
                tree_group.add(door2)

            if map_data[col][row] == "k": # 열쇠
                key = Key(col,row)
                sprite_group.add(key)
                key_group.add(key)


                
            
    sprite_group.add(player)
    sprite_group.add(hp)
    sprite_group.add(count)
    

    def draw_grid():
	#0부터 TILESIZE씩 건너뛰면서 display_width까지 라인을 그려준다
        for x in range(0, display_width, TILESIZE):
    	#첫번째 인자부터 screen(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
            pygame.draw.line(screen, (0, 0, 0, 50), (x, 0), (x, display_height))
        for y in range(0, display_height, TILESIZE):
            pygame.draw.line(screen, (0, 0, 0, 50), (0, y), (display_width, y))
    start_time = time.time()

    running = True
    while running:
        dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
        for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                mainmenu() # 게임이 진행중이 아님
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainmenu()

            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0



        screen.fill(white)
        draw_grid()
        
        screen.blit(background, (0, 0)) # 배경 그리기
        sprite_group.draw(screen)
        player.update()
        hp.update()
        count.update()
        real = time.time()-start_time
        text = timer_font.render(str(int(real)), True, SKY)
        screen.blit(text, (608, 0))
        move.update()
        move2.update2()
        move3.update_2()
        move4.update2_2()
        player.sea_collide()
        player.tree_collide()
        player.item_collide()
        player.key_collide()
        if pygame.mixer.music.get_busy() == False:
            offButton = Button(offImg,1216,0,64,32,offImg,1216,0,soundon)
        elif pygame.mixer.music.get_busy() == True:
            onButton = Button(onImg,1216,0,64,32,onImg,1216,0,soundoff)
        pygame.display.update() # 게임화면을 다시 그리기!


def gamestage3():
    display_width = 1280
    display_height = 768
    TILESIZE = 64
    screen = pygame.display.set_mode((display_width, display_height))
# 화면 타이틀 설정
    pygame.display.set_caption("Avoidance Game") # 화면설정 screen변수로 선언
    
    
# FPS
    clock = pygame.time.Clock()

# 배경 이미지 불러오기
    background = pygame.image.load("images/ch3.png")
    to_x = 0
    to_y = 0
    
    
    
    
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #player의 이미지를 받아온다
            self.image = pygame.image.load("images/char.png")
            #player를 감싸는 사각형을 생성한다
            self.rect = self.image.get_rect()
            #play가 도는 궤도 중심의 위치
            self.orbit_pos_x = 0
            self.orbit_pos_y = 0
            #플레이어의 체력이다.
            self.hp = 3
            self.count = 0

        def update(self):
            
            self.rect.centerx = self.orbit_pos_x
            self.rect.centery = self.orbit_pos_y
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a]):
                self.orbit_pos_x -= 5
            if (keys[pygame.K_d]):
                self.orbit_pos_x += 5
            if (keys[pygame.K_w]):
                self.orbit_pos_y -= 5
            if (keys[pygame.K_s]):
                self.orbit_pos_y += 5

            self.orbit_pos_x += to_x * dt
            self.orbit_pos_y += to_y * dt
            
            if self.rect.left <= TILESIZE :
                self.rect.left = TILESIZE + 1
            if self.rect.right >= display_width - TILESIZE :
                self.rect.right = display_width - TILESIZE - 1
            if self.rect.top <= TILESIZE :
                self.rect.top = TILESIZE + 1
            if self.rect.bottom >= display_height - TILESIZE :
                self.rect.bottom = display_height - TILESIZE - 1

        def tree_collide(self):
            collide_tree = pygame.sprite.spritecollide(self, tree_group, False)
            if collide_tree:
                
                self.orbit_pos_x = TILESIZE * 2 #10
                self.orbit_pos_y = TILESIZE * 4 #10
                # 체력이 1 깎인다.
                self.hp -= 1
                pygame.time.delay(200)
                    
        def sea_collide(self):
            collide_sea = pygame.sprite.spritecollide(self, sea_group, False)
            if collide_sea:
                # 바다에 부딪히면 바로 피가 0이 된다.
                self.hp = 0
        
        def item_collide(self):
            collide_item = pygame.sprite.spritecollide(self, item_group, False)
            collide_item2 = pygame.sprite.spritecollide(self, item2_group, False)
            collide_item3 = pygame.sprite.spritecollide(self, item3_group, False)
            if collide_item:
                item.kill()
                self.count += 1
            elif collide_item2:
                item2.kill()
                self.count += 1
            elif collide_item3:
                item3.kill()
                self.count += 1

        def key_collide(self):
            collide_key = pygame.sprite.spritecollide(self, key_group, False)
            collide_key2 = pygame.sprite.spritecollide(self, key2_group, False)
            if collide_key:
                door.kill()
                door2.kill()
                key.kill()

            elif collide_key2:
                door3.kill()
                door4.kill()
                key2.kill()
        
                
    class Hp(pygame.sprite.Sprite):   
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/hp3.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 32

        def update(self):
            # hp가 줄어들 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.hp == 3:
                self.image = pygame.image.load("images/hp3.png")
            elif player.hp == 2:
                self.image = pygame.image.load("images/hp2.png")
            elif player.hp == 1:
                self.image = pygame.image.load("images/hp1.png")
            elif player.hp <= 0:
                self.image = pygame.image.load("images/hp0.png")
                remainmenu_3()
    
    class Star(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/star0.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 80

        def update(self):
            #count가 늘어날 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.count == 3:
                self.image = pygame.image.load("images/star3.png")
                clearmenu_3()
            elif player.count == 2:
                self.image = pygame.image.load("images/star2.png")
            elif player.count == 1:
                self.image = pygame.image.load("images/star1.png")
            #elif player.count == 0:
             #   self.image = pygame.image.load("images/star1.png")
                

# player을 생성
    player = Player()
    hp = Hp()
    count = Star()
    # sprite_group로 선언된 sprite의 Group()에 player를 넣는다.
    sprite_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sea_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    tree_group = pygame.sprite.Group()
    item_group = pygame.sprite.Group()
    item2_group = pygame.sprite.Group()
    item3_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()
    key2_group = pygame.sprite.Group()

    # player의 처음 위치를 화면의 중간으로 설정한다.
    player.rect.x = TILESIZE * 2
    player.rect.y = TILESIZE * 4
    # 처음 player가 생성되었을 때 궤도가 정해져있지 않으므로 지정해준다. 
    player.orbit_pos_x = player.rect.x
    player.orbit_pos_y = player.rect.y
     
    map_data = []
    # map_file을 읽는다
    with open('map_file3.txt', 'r') as file:
        for line in file:
        # 마지막 줄바꿈 기호까자 출력되므로 strip을 이용해 없애준다.
        # 그리고 띄어쓰기를 기준으로 한 행을 하나의 리스트로 만든 다음 그 리스트를 map_data에 추가해 2차원 리스트로 만들어준다
            map_data.append(line.strip('\n').split(' '))
    for col in range(0,len(map_data)):
        for row in range(0,len(map_data[col])):
            if map_data[col][row] == "s":
                sea = Sea(col, row)
                sprite_group.add(sea)
                
            if map_data[col][row] == "g":
                ground = Ground(col, row)
                sprite_group.add(ground)

            if map_data[col][row] == "t":
                tree = Tree(col, row)
                sprite_group.add(tree)
                #각각의 그룹에 맞게 추가해준다.
                tree_group.add(tree) #tree_group 닿으면 hp소모.

            if map_data[col][row] == "m1": # 움직이는장애물 1
                move = Move(col,row)
                sprite_group.add(move)
                tree_group.add(move)

            if map_data[col][row] == "m2": # 움직이는 장애물 2
                move2 = Move(col, row)
                sprite_group.add(move2)
                tree_group.add(move2)

            if map_data[col][row] == "i": # 아이템
                item = Item(col,row)
                sprite_group.add(item)
                item_group.add(item)

            if map_data[col][row] == "i2": # 아이템
                item2 = Item(col,row)
                sprite_group.add(item2)
                item2_group.add(item2)
                
            if map_data[col][row] == "i3": # 아이템
                item3 = Item(col,row)
                sprite_group.add(item3)
                item3_group.add(item3)
            
            if map_data[col][row] == "sp":
                spin = Spin(col,row)
                sprite_group.add(spin)
                tree_group.add(spin)
            
            if map_data[col][row] == "sp2":
                spin2 = Spin(col,row)
                sprite_group.add(spin2)
                tree_group.add(spin2)
            
            if map_data[col][row] == "d": # 문
                door = Door(col,row)
                sprite_group.add(door)
                tree_group.add(door)

            if map_data[col][row] == "d2": # 문2
                door2 = Door(col,row)
                sprite_group.add(door2)
                tree_group.add(door2)

            if map_data[col][row] == "d3": # 문2
                door3 = Door(col,row)
                sprite_group.add(door3)
                tree_group.add(door3)
            
            if map_data[col][row] == "d4": # 문2
                door4 = Door(col,row)
                sprite_group.add(door4)
                tree_group.add(door4)

            if map_data[col][row] == "k": # 열쇠
                key = Key(col,row)
                sprite_group.add(key)
                key_group.add(key)
            
            if map_data[col][row] == "k2": # 열쇠
                key2 = Key(col,row)
                sprite_group.add(key2)
                key2_group.add(key2)
            
            if map_data[col][row] == "r1": # 열쇠
                rec = Rectangle(col,row)
                sprite_group.add(rec)
                tree_group.add(rec)



                
            
    sprite_group.add(player)
    sprite_group.add(hp)
    sprite_group.add(count)
    

    def draw_grid():
	#0부터 TILESIZE씩 건너뛰면서 display_width까지 라인을 그려준다
        for x in range(0, display_width, TILESIZE):
    	#첫번째 인자부터 screen(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
            pygame.draw.line(screen, (0, 0, 0, 50), (x, 0), (x, display_height))
        for y in range(0, display_height, TILESIZE):
            pygame.draw.line(screen, (0, 0, 0, 50), (0, y), (display_width, y))
    start_time = time.time()

    running = True
    while running:
        dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
        for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                mainmenu() # 게임이 진행중이 아님
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainmenu()


            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0



        screen.fill(white)
        draw_grid()
        
        screen.blit(background, (0, 0)) # 배경 그리기
        sprite_group.draw(screen)
        player.update()
        hp.update()
        count.update()
        real = time.time()-start_time
        text = timer_font.render(str(int(real)), True, SKY)
        screen.blit(text, (608, 0))
        move.update12()
        move2.update13()
        spin.update()
        spin2.update2()
        rec.update()
        player.sea_collide()
        player.tree_collide()
        player.item_collide()
        player.key_collide()
        if pygame.mixer.music.get_busy() == False:
            offButton = Button(offImg,1216,0,64,32,offImg,1216,0,soundon)
        elif pygame.mixer.music.get_busy() == True:
            onButton = Button(onImg,1216,0,64,32,onImg,1216,0,soundoff)
        pygame.display.update() # 게임화면을 다시 그리기!

def gamestage4():
    display_width = 1280
    display_height = 768
    TILESIZE = 64
    screen = pygame.display.set_mode((display_width, display_height))
# 화면 타이틀 설정
    pygame.display.set_caption("Avoidance Game") # 화면설정 screen변수로 선언
    
    
# FPS
    clock = pygame.time.Clock()

# 배경 이미지 불러오기
    background = pygame.image.load("images/ch3.png")
    to_x = 0
    to_y = 0
    
    
    
    
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #player의 이미지를 받아온다
            self.image = pygame.image.load("images/char.png")
            #player를 감싸는 사각형을 생성한다
            self.rect = self.image.get_rect()
            #play가 도는 궤도 중심의 위치
            self.orbit_pos_x = 0
            self.orbit_pos_y = 0
            #플레이어의 체력이다.
            self.hp = 3
            self.count = 0

        def update(self):
            
            self.rect.centerx = self.orbit_pos_x
            self.rect.centery = self.orbit_pos_y
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a]):
                self.orbit_pos_x -= 5
            if (keys[pygame.K_d]):
                self.orbit_pos_x += 5
            if (keys[pygame.K_w]):
                self.orbit_pos_y -= 5
            if (keys[pygame.K_s]):
                self.orbit_pos_y += 5

            self.orbit_pos_x += to_x * dt
            self.orbit_pos_y += to_y * dt
            
            if self.rect.left <= TILESIZE :
                self.rect.left = TILESIZE + 1
            if self.rect.right >= display_width - TILESIZE :
                self.rect.right = display_width - TILESIZE - 1
            if self.rect.top <= TILESIZE :
                self.rect.top = TILESIZE + 1
            if self.rect.bottom >= display_height - TILESIZE :
                self.rect.bottom = display_height - TILESIZE - 1

        def tree_collide(self):
            collide_tree = pygame.sprite.spritecollide(self, tree_group, False)
            if collide_tree:
                
                self.orbit_pos_x = TILESIZE * 2 #10
                self.orbit_pos_y = TILESIZE * 6 #10
                # 체력이 1 깎인다.
                self.hp -= 1
                pygame.time.delay(200)
                    
        def sea_collide(self):
            collide_sea = pygame.sprite.spritecollide(self, sea_group, False)
            if collide_sea:
                # 바다에 부딪히면 바로 피가 0이 된다.
                self.hp = 0
        
        def item_collide(self):
            collide_item = pygame.sprite.spritecollide(self, item_group, False)
            collide_item2 = pygame.sprite.spritecollide(self, item2_group, False)
            collide_item3 = pygame.sprite.spritecollide(self, item3_group, False)
            if collide_item:
                item.kill()
                self.count += 1
            elif collide_item2:
                item2.kill()
                self.count += 1
            elif collide_item3:
                item3.kill()
                self.count += 1

        def key_collide(self):
            collide_key = pygame.sprite.spritecollide(self, key_group, False)
            collide_key2 = pygame.sprite.spritecollide(self, key2_group, False)
            if collide_key:
                door.kill()
                door2.kill()
                key.kill()

            elif collide_key2:
                door3.kill()
                door4.kill()
                key2.kill()
        
                
    class Hp(pygame.sprite.Sprite):   
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/hp3.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 32

        def update(self):
            # hp가 줄어들 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.hp == 3:
                self.image = pygame.image.load("images/hp3.png")
            elif player.hp == 2:
                self.image = pygame.image.load("images/hp2.png")
            elif player.hp == 1:
                self.image = pygame.image.load("images/hp1.png")
            elif player.hp <= 0:
                self.image = pygame.image.load("images/hp0.png")
                remainmenu_4()
    
    class Star(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/star0.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 80

        def update(self):
            #count가 늘어날 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.count == 3:
                self.image = pygame.image.load("images/star3.png")
                clearmenu_4()
            elif player.count == 2:
                self.image = pygame.image.load("images/star2.png")
            elif player.count == 1:
                self.image = pygame.image.load("images/star1.png")
            #elif player.count == 0:
             #   self.image = pygame.image.load("images/star1.png")
                

# player을 생성
    player = Player()
    hp = Hp()
    count = Star()
    # sprite_group로 선언된 sprite의 Group()에 player를 넣는다.
    sprite_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sea_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    tree_group = pygame.sprite.Group()
    item_group = pygame.sprite.Group()
    item2_group = pygame.sprite.Group()
    item3_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()
    key2_group = pygame.sprite.Group()

    # player의 처음 위치를 화면의 중간으로 설정한다.
    player.rect.x = TILESIZE * 2
    player.rect.y = TILESIZE * 6
    # 처음 player가 생성되었을 때 궤도가 정해져있지 않으므로 지정해준다. 
    player.orbit_pos_x = player.rect.x
    player.orbit_pos_y = player.rect.y
     
    map_data = []
    # map_file을 읽는다
    with open('map_file4.txt', 'r') as file:
        for line in file:
        # 마지막 줄바꿈 기호까자 출력되므로 strip을 이용해 없애준다.
        # 그리고 띄어쓰기를 기준으로 한 행을 하나의 리스트로 만든 다음 그 리스트를 map_data에 추가해 2차원 리스트로 만들어준다
            map_data.append(line.strip('\n').split(' '))
    for col in range(0,len(map_data)):
        for row in range(0,len(map_data[col])):
            if map_data[col][row] == "s":
                sea = Sea(col, row)
                sprite_group.add(sea)
                
            if map_data[col][row] == "g":
                ground = Ground(col, row)
                sprite_group.add(ground)

            if map_data[col][row] == "t":
                tree = Tree(col, row)
                sprite_group.add(tree)
                #각각의 그룹에 맞게 추가해준다.
                tree_group.add(tree) #tree_group 닿으면 hp소모.

            if map_data[col][row] == "m1": # 움직이는장애물 1
                move = Move(col,row)
                sprite_group.add(move)
                tree_group.add(move)

            if map_data[col][row] == "m2": # 움직이는 장애물 2
                move2 = Move(col, row)
                sprite_group.add(move2)
                tree_group.add(move2)

            if map_data[col][row] == "m3": # 움직이는 장애물 2
                move3 = Move(col, row)
                sprite_group.add(move3)
                tree_group.add(move3)

            if map_data[col][row] == "m4": # 움직이는 장애물 2
                move4 = Move(col, row)
                sprite_group.add(move4)
                tree_group.add(move4)

            if map_data[col][row] == "i": # 아이템
                item = Item(col,row)
                sprite_group.add(item)
                item_group.add(item)

            if map_data[col][row] == "i2": # 아이템
                item2 = Item(col,row)
                sprite_group.add(item2)
                item2_group.add(item2)
                
            if map_data[col][row] == "i3": # 아이템
                item3 = Item(col,row)
                sprite_group.add(item3)
                item3_group.add(item3)
            
            if map_data[col][row] == "sp":
                spin = Spin(col,row)
                sprite_group.add(spin)
                tree_group.add(spin)
            
            if map_data[col][row] == "sp2":
                spin2 = Spin(col,row)
                sprite_group.add(spin2)
                tree_group.add(spin2)

            if map_data[col][row] == "sp3":
                spin3 = Spin(col,row)
                sprite_group.add(spin3)
                tree_group.add(spin3)

            if map_data[col][row] == "sp4":
                spin4 = Spin(col,row)
                sprite_group.add(spin4)
                tree_group.add(spin4)
            
            if map_data[col][row] == "d": # 문
                door = Door(col,row)
                sprite_group.add(door)
                tree_group.add(door)

            if map_data[col][row] == "d2": # 문2
                door2 = Door(col,row)
                sprite_group.add(door2)
                tree_group.add(door2)

            if map_data[col][row] == "d3": # 문2
                door3 = Door(col,row)
                sprite_group.add(door3)
                tree_group.add(door3)
            
            if map_data[col][row] == "d4": # 문2
                door4 = Door(col,row)
                sprite_group.add(door4)
                tree_group.add(door4)

            if map_data[col][row] == "k": # 열쇠
                key = Key(col,row)
                sprite_group.add(key)
                key_group.add(key)
            



                
            
    sprite_group.add(player)
    sprite_group.add(hp)
    sprite_group.add(count)
    

    def draw_grid():
	#0부터 TILESIZE씩 건너뛰면서 display_width까지 라인을 그려준다
        for x in range(0, display_width, TILESIZE):
    	#첫번째 인자부터 screen(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
            pygame.draw.line(screen, (0, 0, 0, 50), (x, 0), (x, display_height))
        for y in range(0, display_height, TILESIZE):
            pygame.draw.line(screen, (0, 0, 0, 50), (0, y), (display_width, y))
    start_time = time.time()

    running = True
    while running:
        dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
        for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                mainmenu() # 게임이 진행중이 아님
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainmenu()


            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0



        screen.fill(white)
        draw_grid()
        
        screen.blit(background, (0, 0)) # 배경 그리기
        sprite_group.draw(screen)
        player.update()
        hp.update()
        count.update()
        real = time.time()-start_time
        text = timer_font.render(str(int(real)), True, SKY)
        screen.blit(text, (608, 0))
        move.update3()
        move2.update4()
        move3.update5()
        move4.update6()
        spin.update5()
        spin2.update6()
        spin3.update7()
        spin4.update8()
        player.sea_collide()
        player.tree_collide()
        player.item_collide()
        player.key_collide()
        if pygame.mixer.music.get_busy() == False:
            offButton = Button(offImg,1216,0,64,32,offImg,1216,0,soundon)
        elif pygame.mixer.music.get_busy() == True:
            onButton = Button(onImg,1216,0,64,32,onImg,1216,0,soundoff)
        pygame.display.update() # 게임화면을 다시 그리기!

def gamestage5(): #게임 스테이지 구현 창.
    display_width = 1280
    display_height = 768
    TILESIZE = 64
    screen = pygame.display.set_mode((display_width, display_height))
# 화면 타이틀 설정
    pygame.display.set_caption("Avoidance Game") # 화면설정 screen변수로 선언
    
    
# FPS
    clock = pygame.time.Clock()

# 배경 이미지 불러오기
    background = pygame.image.load("images/ch3.png")
    to_x = 0
    to_y = 0
    
    
    
    
    class Player(pygame.sprite.Sprite): #플레이어 구현 클래스
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #player의 이미지를 받아온다
            self.image = pygame.image.load("images/char.png")
            #player를 감싸는 사각형을 생성한다
            self.rect = self.image.get_rect()
            #play가 도는 궤도 중심의 위치
            self.orbit_pos_x = 0
            self.orbit_pos_y = 0
            #플레이어의 체력이다.
            self.hp = 3
            self.count = 0
            
        def update(self): #플레아어 움직임 구현
            
            self.rect.centerx = self.orbit_pos_x
            self.rect.centery = self.orbit_pos_y
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a]):
                self.orbit_pos_x -= 5
            if (keys[pygame.K_d]):
                self.orbit_pos_x += 5
            if (keys[pygame.K_w]):
                self.orbit_pos_y -= 5
            if (keys[pygame.K_s]):
                self.orbit_pos_y += 5

            self.orbit_pos_x += to_x * dt
            self.orbit_pos_y += to_y * dt
            
            if self.rect.left <= TILESIZE :
                self.rect.left = TILESIZE + 1
            if self.rect.right >= display_width - TILESIZE :
                self.rect.right = display_width - TILESIZE - 1
            if self.rect.top <= TILESIZE :
                self.rect.top = TILESIZE + 1
            if self.rect.bottom >= display_height - TILESIZE :
                self.rect.bottom = display_height - TILESIZE - 1

        def tree_collide(self): #장애물에 닿게되었을 때 실행되는 함수
            collide_tree = pygame.sprite.spritecollide(self, tree_group, False)
            if collide_tree:
                
                self.orbit_pos_x = TILESIZE * 2 #10
                self.orbit_pos_y = TILESIZE * 10 #10
                # 체력이 1 깎인다.
                self.hp -= 1
                pygame.time.delay(200)
                    
        def sea_collide(self):
            collide_sea = pygame.sprite.spritecollide(self, sea_group, False)
            if collide_sea:
                # 바다에 부딪히면 바로 피가 0이 된다.
                self.hp = 0
        
        def item_collide(self): #아이템(별)을 먹었을때 실행되는 함수
            collide_item = pygame.sprite.spritecollide(self, item_group, False)
            collide_item2 = pygame.sprite.spritecollide(self, item2_group, False)
            collide_item3 = pygame.sprite.spritecollide(self, item3_group, False)
            if collide_item:
                item.kill()
                self.count += 1
            elif collide_item2:
                item2.kill()
                self.count += 1
            elif collide_item3:
                item3.kill()
                self.count += 1

        def key_collide(self): # 열쇠를 먹었을 때 실행되는 함수
            collide_key = pygame.sprite.spritecollide(self, key_group, False)
            collide_key2 = pygame.sprite.spritecollide(self, key2_group, False)
            collide_key3 = pygame.sprite.spritecollide(self, key3_group, False)
            collide_key4 = pygame.sprite.spritecollide(self, key4_group, False)
            collide_key5 = pygame.sprite.spritecollide(self, key5_group, False)
            if collide_key:
                door.kill()
                door2.kill()
                door3.kill()
                key.kill()

            elif collide_key2:
                door5.kill()
                door4.kill()
                key2.kill()
            
            elif collide_key3:
                door6.kill()
                door7.kill()
                key3.kill()

            elif collide_key4:
                door8.kill()
                door9.kill()
                key4.kill()

            elif collide_key5:
                door10.kill()
                key5.kill()
        
                
    class Hp(pygame.sprite.Sprite): # Hp 구현 클래스
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #처음에는 체력이 3으로 시작한다.
            self.image = pygame.image.load("images/hp3.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 32

        def update(self):
            # hp가 줄어들 때마다 그 체력에 맞는 체력이미지를 불러온다.
            if player.hp == 3:
                self.image = pygame.image.load("images/hp3.png")
            elif player.hp == 2:
                self.image = pygame.image.load("images/hp2.png")
            elif player.hp == 1:
                self.image = pygame.image.load("images/hp1.png")
            elif player.hp <= 0:
                self.image = pygame.image.load("images/hp0.png")
                remainmenu_5()
    
    class Star(pygame.sprite.Sprite): # 별 구현 클래스
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("images/star0.png")
            self.rect = self.image.get_rect()
            self.rect.x = 32
            self.rect.y = 80

        def update(self):
            #count가 늘어날 때마다 그에 맞는 별 이미지를 불러온다.
            if player.count == 3:
                self.image = pygame.image.load("images/star3.png")
                clearmenu_5()
            elif player.count == 2:
                self.image = pygame.image.load("images/star2.png")
            elif player.count == 1:
                self.image = pygame.image.load("images/star1.png")
            #elif player.count == 0:
             #   self.image = pygame.image.load("images/star1.png")
                

# player을 생성
    player = Player()
    hp = Hp()
    count = Star()
    # sprite_group로 선언된 sprite의 Group()에 player를 넣는다.
    sprite_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sea_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    tree_group = pygame.sprite.Group()
    item_group = pygame.sprite.Group()
    item2_group = pygame.sprite.Group()
    item3_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()
    key2_group = pygame.sprite.Group()
    key3_group = pygame.sprite.Group()
    key4_group = pygame.sprite.Group()
    key5_group = pygame.sprite.Group()

    # player의 처음 위치를 화면의 중간으로 설정한다.
    player.rect.x = TILESIZE * 2
    player.rect.y = TILESIZE * 10
    # 처음 player가 생성되었을 때 궤도가 정해져있지 않으므로 지정해준다. 
    player.orbit_pos_x = player.rect.x
    player.orbit_pos_y = player.rect.y
     
    map_data = []
    # map_file을 읽는다
    with open('map_file5.txt', 'r') as file:
        for line in file:
        # 마지막 줄바꿈 기호까자 출력되므로 strip을 이용해 없애준다.
        # 그리고 띄어쓰기를 기준으로 한 행을 하나의 리스트로 만든 다음 그 리스트를 map_data에 추가해 2차원 리스트로 만들어준다
            map_data.append(line.strip('\n').split(' '))
    for col in range(0,len(map_data)):
        for row in range(0,len(map_data[col])):
            if map_data[col][row] == "s":
                sea = Sea(col, row)
                sprite_group.add(sea)
                
            if map_data[col][row] == "g":
                ground = Ground(col, row)
                sprite_group.add(ground)

            if map_data[col][row] == "t":
                tree = Tree(col, row)
                sprite_group.add(tree)
                #각각의 그룹에 맞게 추가해준다.
                tree_group.add(tree) #tree_group 닿으면 hp소모.

            if map_data[col][row] == "m1": # 움직이는장애물 1
                move = Move(col,row)
                sprite_group.add(move)
                tree_group.add(move)

            if map_data[col][row] == "m2": # 움직이는 장애물 2
                move2 = Move(col, row)
                sprite_group.add(move2)
                tree_group.add(move2)

            if map_data[col][row] == "m3": # 움직이는 장애물 2
                move3 = Move(col, row)
                sprite_group.add(move3)
                tree_group.add(move3)

            if map_data[col][row] == "m4": # 움직이는 장애물 2
                move4 = Move(col, row)
                sprite_group.add(move4)
                tree_group.add(move4)

            if map_data[col][row] == "m5": # 움직이는 장애물 2
                move5 = Move(col, row)
                sprite_group.add(move5)
                tree_group.add(move5)

            if map_data[col][row] == "i": # 아이템
                item = Item(col,row)
                sprite_group.add(item)
                item_group.add(item)

            if map_data[col][row] == "i2": # 아이템
                item2 = Item(col,row)
                sprite_group.add(item2)
                item2_group.add(item2)
                
            if map_data[col][row] == "i3": # 아이템
                item3 = Item(col,row)
                sprite_group.add(item3)
                item3_group.add(item3)
            
            if map_data[col][row] == "sp": #회전하는 장애물
                spin = Spin(col,row)
                sprite_group.add(spin)
                tree_group.add(spin)
            
            if map_data[col][row] == "sp2":
                spin2 = Spin(col,row)
                sprite_group.add(spin2)
                tree_group.add(spin2)
            
            if map_data[col][row] == "d": # 문
                door = Door(col,row)
                sprite_group.add(door)
                tree_group.add(door)

            if map_data[col][row] == "d2": 
                door2 = Door(col,row)
                sprite_group.add(door2)
                tree_group.add(door2)

            if map_data[col][row] == "d3": # 
                door3 = Door(col,row)
                sprite_group.add(door3)
                tree_group.add(door3)
            
            if map_data[col][row] == "d4": # 
                door4 = Door(col,row)
                sprite_group.add(door4)
                tree_group.add(door4)
            
            if map_data[col][row] == "d5": # 
                door5 = Door(col,row)
                sprite_group.add(door5)
                tree_group.add(door5)

            if map_data[col][row] == "d6": # 
                door6 = Door(col,row)
                sprite_group.add(door6)
                tree_group.add(door6)

            if map_data[col][row] == "d7": # 
                door7 = Door(col,row)
                sprite_group.add(door7)
                tree_group.add(door7)

            if map_data[col][row] == "d8": # 
                door8 = Door(col,row)
                sprite_group.add(door8)
                tree_group.add(door8)

            if map_data[col][row] == "d9": # 
                door9 = Door(col,row)
                sprite_group.add(door9)
                tree_group.add(door9)

            if map_data[col][row] == "d10": # 
                door10 = Door(col,row)
                sprite_group.add(door10)
                tree_group.add(door10)

            if map_data[col][row] == "k": # 열쇠
                key = Key(col,row)
                sprite_group.add(key)
                key_group.add(key)
            
            if map_data[col][row] == "k2": # 열쇠
                key2 = Key(col,row)
                sprite_group.add(key2)
                key2_group.add(key2)
            
            if map_data[col][row] == "k3": # 열쇠
                key3 = Key(col,row)
                sprite_group.add(key3)
                key3_group.add(key3)

            if map_data[col][row] == "k4": # 열쇠
                key4 = Key(col,row)
                sprite_group.add(key4)
                key4_group.add(key4)

            if map_data[col][row] == "k5": # 열쇠
                key5 = Key(col,row)
                sprite_group.add(key5)
                key5_group.add(key5)
            
            if map_data[col][row] == "r1": #네모로 움직이는 장애물
                rec = Rectangle(col,row)
                sprite_group.add(rec)
                tree_group.add(rec)
            
            if map_data[col][row] == "r2":
                rec2 = Rectangle(col,row)
                sprite_group.add(rec2)
                tree_group.add(rec2)
            
            if map_data[col][row] == "r3":
                rec3 = Rectangle(col,row)
                sprite_group.add(rec3)
                tree_group.add(rec3)
            
            if map_data[col][row] == "r4":
                rec4 = Rectangle(col,row)
                sprite_group.add(rec4)
                tree_group.add(rec4)





                
            
    sprite_group.add(player)
    sprite_group.add(hp)
    sprite_group.add(count)
    

    def draw_grid():
	#0부터 TILESIZE씩 건너뛰면서 display_width까지 라인을 그려준다
        for x in range(0, display_width, TILESIZE):
    	#첫번째 인자부터 screen(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
            pygame.draw.line(screen, (0, 0, 0, 50), (x, 0), (x, display_height))
        for y in range(0, display_height, TILESIZE):
            pygame.draw.line(screen, (0, 0, 0, 50), (0, y), (display_width, y))
    start_time = time.time()

    running = True
    while running:
        dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
        for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                mainmenu() # 게임이 진행중이 아님
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainmenu()


            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0



        screen.fill(white)
        draw_grid()
        screen.blit(background, (0, 0)) # 배경 그리기
        sprite_group.draw(screen)
        player.update()
        hp.update() 
        count.update()
        real = time.time()-start_time
        text = timer_font.render(str(int(real)), True, SKY)
        screen.blit(text, (608, 0))
        # 이번 스테이지에 맞는 장애물 함수update
        move.update7() 
        move2.update8()
        move3.update9()
        move4.update10()
        move5.update11()
        spin.update3()
        spin2.update4()
        rec.update2()
        rec2.update3()
        rec3.update4()
        rec4.update5()
        player.sea_collide()
        player.tree_collide() # 플레이어가 장애물에 닿게되면 실행될 함수 구현.
        player.item_collide()
        player.key_collide()
        if pygame.mixer.music.get_busy() == False: #게임 내 음악 실행버튼 구현
            offButton = Button(offImg,1216,0,64,32,offImg,1216,0,soundon)
        elif pygame.mixer.music.get_busy() == True:
            onButton = Button(onImg,1216,0,64,32,onImg,1216,0,soundoff)
        pygame.display.update() # 게임화면을 다시 그리기!

mainmenu()
pygame.quit()