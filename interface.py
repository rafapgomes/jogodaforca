import pygame as pg

branco = (255,255,255)
preto = (0,0,0)



    
def inicio():
    pg.display.init()
    screen = pg.display.set_mode(size=(900,500))
    return screen

def cabeca(screen):
    pg.draw.circle(screen,preto,(305,130),40,10)

def corpo(screen):
    pg.draw.line(screen,preto,(300,170),(300,300),10)


def braco1(screen):
    pg.draw.line(screen,preto,(295,190),(200,250),10)


def braco2(screen):
    pg.draw.line(screen,preto,(305,190),(405,250),10)


def perna1(screen):
     pg.draw.line(screen,preto,(300,280),(250,390),10)

def perna2(screen):
     pg.draw.line(screen,preto,(300,280),(350,390),10)


def forca(screen):
    pg.draw.rect(screen,branco,(0,0,1000,600))
    pg.draw.line(screen,preto,(100,400),(100,40),10)
    pg.draw.line(screen,preto,(100,40),(300,40),10)
    pg.draw.line(screen,preto,(300,40),(300,100),10)
        perna1(screen)

    pg.display.update()
    
   

screen = inicio()
while True:
    forca(screen)

    





