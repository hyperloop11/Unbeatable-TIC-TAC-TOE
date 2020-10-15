import pygame   
import random
import math
from sys import exit

def draw_rectangle(x,y):
    return pygame.Rect(x,y,w//3,h//3)

def draw_X(coordinates):
    fontx = pygame.font.SysFont('corbel', 70, True)
    textx = fontx.render('X',1 , (0,255,0))
    win.blit(textx, coordinates)
        
def add_score(index):
    if flag==1:
        score[index]='X'
    else:
        score[index]='O'

def winner(index):
    if score[index]=='X':
        return 'X'
    if score[index]=='O':
        return 'O'

def check_win(): #returns winning char
    if score[0]!='':
        if score[0]==score[1] and score[0]==score[2]:
            return winner(0)
        if score[0]==score[3] and score[0]==score[6]:
            return winner(0)
    if score[4]!='':
        if score[1]==score[4] and score[4]==score[7]:
            return winner(4)
        if score[3]==score[4] and score[4]==score[5]:
            return winner(4)
        if score[0]==score[4] and score[4]==score[8]:
            return winner(4)
        if score[2]==score[4] and score[4]==score[6]:
            return winner(4)  
    if score[8]!='':
        if score[2]==score[8] and score[8]==score[5]:
            return winner(8)
        if score[6]==score[8] and score[8]==score[7]:
            return winner(8)
    if score.count('')==0:
        return 'TIE'
    else:
        return ''

def display_screen():
    global run, xWinScreen, oWinScreen, tieScreen
    TheWinner=check_win()
    if TheWinner=='X':
        xWinScreen=True
        run=False
    if TheWinner=='O':
        oWinScreen=True
        run=False
    if TheWinner=='TIE':
        tieScreen=True
        run=False


def comp_move():
    bestScore=-math.inf
    for i in range(9):
        if score[i]=='':
            score[i]='O'#o placed
            value=minimax(score,0,False)
            #value=minimax(score)
            score[i]=''
            if value>bestScore:
                bestScore=value
                bestMove=i
    score[bestMove]='O'
    fonto = pygame.font.SysFont('corbel', 70, True)
    texto = fonto.render('O',1 , (0,0,255))
    win.blit(texto, figpos[bestMove])
    global xTurn
    xTurn=True
    display_screen()
    #draw_figure(figpos[bestMove],1)


def minimax(score,depth,isMaximizing):
    result=check_win()
    if result!='':
        if result=='O':
            return 10
        if result=='X':
            return -10
        if result =='TIE':
            return 0
    if isMaximizing:
        bestScore=-math.inf
        for i in range(9):
            if score[i]=='':
                score[i]='O'#x plays
                value=minimax(score,depth+1,False)
                score[i]=''
                bestScore=max(value,bestScore)
        return bestScore
    else:
        bestScore=math.inf
        for i in range(9):
            if score[i]=='':
                score[i]='X'#x plays
                value=minimax(score,depth+1,True)
                score[i]=''
                bestScore=min(value,bestScore)
        return bestScore


def redrawWindow():
    #drawing lines of board.
    pygame.draw.line(win,(0,0,0),(w//3,0),(w//3,h),1)
    pygame.draw.line(win,(0,0,0),(2*w//3,0),(2*w//3,h),1)
    pygame.draw.line(win,(0,0,0),(0,h//3),(w,h//3),1)
    pygame.draw.line(win,(0,0,0),(0,2*h//3),(w,2*h//3),1)
    pygame.display.update()

pygame.init()

w=500
h=500
win=pygame.display.set_mode((w,h))

pygame.display.set_caption("TIC-TAC-TOE")
clock = pygame.time.Clock()

win.fill([255,255,255])

clock.tick(100)

rect1=draw_rectangle(0,0)
rect2=draw_rectangle(w//3,0)
rect3=draw_rectangle(2*w//3,0)
rect4=draw_rectangle(0,h//3)
rect5=draw_rectangle(w//3,h//3)
rect6=draw_rectangle(2*w//3,h//3)
rect7=draw_rectangle(0,2*h//3)
rect8=draw_rectangle(w//3,2*h//3)
rect9=draw_rectangle(2*w//3,2*h//3)

score=['' for i in range(9)]

figpos=[(50,50),(w//3+50,50),(2*w//3+50,50),(50,h//3+50),(w//3+50,h//3+50),
            (2*w//3+50,h//3+50),(50,2*h//3+50),(w//3+50,2*h//3+50),
            (2*w//3+50,2*h//3+50)]

flag=1
xTurn=True
run=True
xWinScreen=False
oWinScreen=False
tieScreen=False

while run:
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and xTurn:
            mousepos= pygame.mouse.get_pos()
            if rect1.collidepoint(mousepos) and score[0]=='':
                draw_X((50,50))
                add_score(0)
                xTurn=False
                display_screen()
                print(check_win())
                if score.count('')!=0:
                    comp_move()
            if rect2.collidepoint(mousepos) and score[1]=='':
                draw_X((w//3+50,50))
                add_score(1)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect3.collidepoint(mousepos) and score[2]=='':
                draw_X((2*w//3+50,50))
                add_score(2)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect4.collidepoint(mousepos) and score[3]=='':
                draw_X((50,h//3+50))
                add_score(3)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect5.collidepoint(mousepos) and score[4]=='':
                draw_X((w//3+50,h//3+50))
                add_score(4)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect6.collidepoint(mousepos) and score[5]=='':
                draw_X((2*w//3+50,h//3+50))
                add_score(5)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect7.collidepoint(mousepos) and score[6]=='':
                draw_X((50,2*h//3+50))
                add_score(6)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect8.collidepoint(mousepos) and score[7]=='':
                draw_X((w//3+50,2*h//3+50))
                add_score(7)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()
            if rect9.collidepoint(mousepos) and score[8]=='' :
                draw_X((2*w//3+50,2*h//3+50))
                add_score(8)
                xTurn=False
                print(check_win())
                display_screen()
                if score.count('')!=0:
                    comp_move()

win.fill([255,255,255])

while xWinScreen:
    font = pygame.font.SysFont('corbel', 30, True)
    text = font.render('The Winner Is X!',1 , (0,255,0))
    win.blit(text, (20,120))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            xWinScreen=False
            exit()

while oWinScreen:
    font = pygame.font.SysFont('corbel', 30, True)
    text = font.render('The Winner Is O!',1 , (0,0,255))
    win.blit(text, (20,120))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oWinSCreen=False
            exit()

while tieScreen:
    font = pygame.font.SysFont('corbel', 30, True)
    text = font.render('Its a draw!',1 , (0,0,0))
    win.blit(text, (20,120))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawScreen=False
            exit()

pygame.quit()
        
