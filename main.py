import pygame
    
def draw_rectangle(x,y):
    return pygame.Rect(x,y,w//3,h//3)

def collision(rect, pos):
        if rect.collidepoint(pos):
            return True
        else:
            return False

def draw_figure(coordinates,flag):
    if flag==1:#for x
        fontx = pygame.font.SysFont('corbel', 70, True)
        textx = fontx.render('X',1 , (0,255,0))
        win.blit(textx, coordinates)

    if flag==-1:
        fonto = pygame.font.SysFont('corbel', 70, True)
        texto = fonto.render('O',1 , (0,0,255))
        win.blit(texto, coordinates)
    
    


def add_score(index):
    if flag==1:
        score[index]=True#true at x's turn
    if flag==-1:
        score[index]=False

def xwins(index):
    if score[index]:
        return True
    if score[index]==False:
        return False
    if score[index]==None:
        return None
    

def check_win(): #returns bool true if x wins
    if score[0]!=None:
        if score[0]==score[1] and score[0]==score[2]:
            return xwins(0)
        if score[0]==score[3] and score[0]==score[6]:
            return xwins(0)
    if score[4]!=None:
        if score[1]==score[4] and score[4]==score[7]:
            return xwins(4)
        if score[3]==score[4] and score[4]==score[5]:
            return xwins(4)
        if score[0]==score[4] and score[4]==score[8]:
            return xwins(4)
        if score[2]==score[4] and score[4]==score[6]:
            return xwins(4)
        
    if score[8]!=None:
        if score[2]==score[8] and score[8]==score[5]:
            return xwins(8)
        if score[6]==score[8] and score[8]==score[7]:
            return xwins(8)
    
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

score=[None for i in range(9)]

flag=1

xWinScreen=False
oWinSCreen=False
drawScreen=False

run=True
while run:
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousepos= pygame.mouse.get_pos()
            if collision(rect1,mousepos) and score[0]==None:
                draw_figure((50,50),flag)
                add_score(0)
                flag*=-1
            if collision(rect2,mousepos) and score[1]==None:
                draw_figure((w//3+50,50),flag)
                add_score(1)
                flag*=-1
            if collision(rect3,mousepos) and score[2]==None:
                draw_figure((2*w//3+50,50),flag)
                add_score(2)
                flag*=-1
            if collision(rect4,mousepos) and score[3]==None:
                draw_figure((50,h//3+50),flag)
                add_score(3)
                flag*=-1
            if collision(rect5,mousepos) and score[4]==None:
                draw_figure((w//3+50,h//3+50),flag)
                add_score(4)
                flag*=-1
            if collision(rect6,mousepos) and score[5]==None:
                draw_figure((2*w//3+50,h//3+50),flag)
                add_score(5)
                flag*=-1
            if collision(rect7,mousepos) and score[6]==None:
                draw_figure((50,2*h//3+50),flag)
                add_score(6)
                flag*=-1
            if collision(rect8,mousepos) and score[7]==None:
                draw_figure((w//3+50,2*h//3+50),flag)
                add_score(7)
                flag*=-1
            if collision(rect9,mousepos) and score[8]==None:
                draw_figure((2*w//3+50,2*h//3+50),flag)
                add_score(8)
                flag*=-1
            x=check_win()
            if x:
                #x wins screen.
                xWinScreen=True
                run=False
            if x==False:
                #o wins
                oWinSCreen=True
                run=False
            if x==None:
                continue

win.fill([255,255,255])
while xWinScreen:
    font = pygame.font.SysFont('corbel', 30, True)
    text = font.render('The Winner Is X!',1 , (0,255,0))
    win.blit(text, (20,120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            xWinScreen=False
    
    pygame.display.update()

while oWinSCreen:
    font = pygame.font.SysFont('corbel', 30, True)
    text = font.render('The Winner Is O!',1 , (0,0,255))
    win.blit(text, (20,120))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oWinSCreen=False

    pygame.display.update()

pygame.quit()
