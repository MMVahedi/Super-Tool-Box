#1 hafte moonde o kar tamoom shode:|
import os, time, datetime 
from bad import file_founder , mahdi, mahdi2
pages=0
import pygame
import sys
from random import randint
from time import sleep
import thread

larges = []
bads = []
logs = []
olds = []

pygame.init()
pygame.display.set_caption("super tool box")
screen=pygame.display.set_mode((580,380))                              
screen.fill((0,162,232))
tt=pygame.image.load("1.jpg")
k=pygame.image.load("3.jpg")
jj=pygame.image.load("4.jpg")
o=pygame.image.load("2.jpg")
v=pygame.image.load("1010.png")
e=pygame.image.load("15.png")
p=pygame.image.load("111.png")
aa=pygame.image.load("5.jpg")
bb=pygame.image.load("6.jpg")
cc=pygame.image.load("7.jpg")
dd=pygame.image.load("8.jpg")
ee=pygame.image.load("9.jpg")
ff=pygame.image.load("11.jpg")
gg=pygame.image.load("12.jpg")
hh=pygame.image.load("13.jpg")
vv=pygame.image.load("troian-virus-worm.jpg")
zz=pygame.image.load("1000.jpg")
ww=pygame.image.load("1.png")
uu=pygame.image.load("500.jpg")
nn=pygame.image.load("100.jpg")
mm=pygame.image.load("300.jpg")
qq=pygame.image.load("400.jpg")
ss=pygame.image.load("200.jpg")
loho=pygame.image.load("loh.png")
oo=pygame.image.load("fu.png")
page=0
t = pygame.transform.scale(tt, (70,64))
screen.blit(t,(5,10))
screen.blit(aa,(5,84))
screen.blit(cc,(5,158))
screen.blit(ee,(5,232))
screen.blit(gg,(5,306))
screen.blit(loho,(90,20))
a = 0
x = 0

larges = []
bads = []
logs = []
olds = []
flag = 0

pygame.display.update()
while 1==1:
    if a==1:
        x=x+5
    else:
        x=x-5
    if x>800:
        a=-1
    if x<0:
        a=1
    screen.fill((0,250,6))
    y=300
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()        
        if event.type==pygame.MOUSEBUTTONDOWN:
            #c=screen.fill((255,255,255)
            #d=screen.blit(v,(event.pos[0],event.pos[1]))
            m,n= event.pos[0],event.pos[1]
            for j in range (5):
                if 5<=m<=70 and 17+74.5*j<=n<=10+75*j+74.5:
                    page = j
                    if page ==0:
                        screen.fill((0,162,232))
                        screen.blit(p,(90,20))
                        screen.blit(e,(150,37))
                        screen.blit(k,(5,10))
                        screen.blit(aa,(5,85))
                        screen.blit(cc,(5,160))
                        screen.blit(ee,(5,235))
                        screen.blit(gg,(5,310))
                        screen.blit(uu,(450,290))
                        screen.blit(v,(150,220))
                        pygame.display.update()
                    if page ==1:
                        screen.fill((0,162,232))
                        screen.blit(p,(90,20))
                        screen.blit(zz,(150,80))
                        screen.blit(t,(5,10))
                        screen.blit(bb,(5,85))
                        screen.blit(cc,(5,160))
                        screen.blit(ee,(5,235))
                        screen.blit(gg,(5,310))
                        screen.blit(nn,(450,290))
                      
                        pygame.display.update()
                    if page ==2:
                        screen.fill((0,162,232))
                        screen.blit(p,(90,20))
                        screen.blit(vv,(130,69))
                        screen.blit(t,(5,10))
                        screen.blit(aa,(5,85))
                        screen.blit(dd,(5,160))
                        screen.blit(ee,(5,235))
                        screen.blit(gg,(5,310))
                        screen.blit(mm,(450,290))
                        
                        pygame.display.update()
                    if page ==3:
                        screen.fill((0,162,232))
                        screen.blit(p,(90,20))
                        screen.blit(ww,(150,37))
                        screen.blit(t,(5,10))
                        screen.blit(aa,(5,85))
                        screen.blit(cc,(5,160))
                        screen.blit(ff,(5,235))
                        screen.blit(gg,(5,310))
                        screen.blit(qq,(450,290))
                        screen.blit(v,(150,220))
                        pygame.display.update()
                    if page ==4:
                        screen.fill((0,162,232))
                        screen.blit(p,(90,20))
                        
                        screen.blit(t,(5,10))
                        screen.blit(aa,(5,85))
                        screen.blit(cc,(5,160))
                        screen.blit(ee,(5,235))
                        screen.blit(hh,(5,310))
                        screen.blit(ss,(450,290))
                        screen.blit(oo,(100,20))
                        pygame.display.update()
                        
                    
            print page
            if page==0:
                if 450<=m<=520 and 290<=n<=354:
                    print "btn0"
                    if flag==0:
                        thread.start_new_thread(mahdi, ("large", ".",larges,bads,logs,olds))
                        flag = 1
                    else:
                        mahdi2("large", ".",larges,bads,logs,olds)
    
            if page==1:
                if 450<=m<=520 and 290<=n<=354:
                    print "btn1"
                    if flag==0:
                        thread.start_new_thread(mahdi, ("old", ".",larges,bads,logs,olds))
                        flag = 1
                    else:
                        mahdi2("old", ".",larges,bads,logs,olds)
                    
            if page==2:
                if 450<=m<=520 and 290<=n<=354:
                    print "btn2"
                    if flag==0:
                        thread.start_new_thread(mahdi, ("bad", ".",larges,bads,logs,olds))
                        flag = 1
                    else:
                        mahdi2("bad", ".",larges,bads,logs,olds)                    

            if page==3:
                if 450<=m<=520 and 290<=n<=354:
                    print "btn3"
                    if flag==0:
                        thread.start_new_thread(mahdi, ("log", ".",larges,bads,logs,olds))
                        flag = 1
                    else:
                        mahdi2("log", ".",larges,bads,logs,olds)                    
            if page==4:
                if 450<=m<=520 and 290<=n<=354:
                    print "btn4"
                    if flag==0:
                        thread.start_new_thread(mahdi, ("all", ".",larges,bads,logs,olds))
                        flag = 1
                    else:
                        mahdi2("all", ".",larges,bads,logs,olds)
#the end
