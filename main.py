import pygame
    
def draw_rectangle(x,y):
    return pygame.Rect(x,y,w//3,h//3)

def collision(rect, pos):
        if rect.collidepoint(pos):
            return True
        else:
            return False

def draw_figure(coordinates,flag):
    #may cause problem
    if flag==1:#for x
        fontx = pygame.font.SysFont('corbel', 70, True)
        textx = fontx.render('X',1 , (0,255,0))
        win.blit(textx, coordinates)

    else:
        fonto = pygame.font.SysFont('corbel', 70, True)
        texto = fonto.render('O',1 , (0,0,255))
        win.blit(texto, coordinates)

def add_score(index):
    if flag==1:
        score[index]=1
    else:
        score[index]=0

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

score=[3 for i in range(9)]

flag=1

run=True
while run:
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousepos= pygame.mouse.get_pos()
            if collision(rect1,mousepos) and score[0]==3:
                draw_figure((50,50),flag)
                add_score(0)
            if collision(rect2,mousepos) and score[1]==3:
                draw_figure((w//3+50,50),flag)
                add_score(1)
            if collision(rect3,mousepos) and score[2]==3:
                draw_figure((2*w//3+50,50),flag)
                add_score(2)
            if collision(rect4,mousepos) and score[3]==3:
                draw_figure((50,h//3+50),flag)
                add_score(3)
            if collision(rect5,mousepos) and score[4]==3:
                draw_figure((w//3+50,h//3+50),flag)
                add_score(4)
            if collision(rect6,mousepos) and score[5]==3:
                draw_figure((2*w//3+50,h//3+50),flag)
                add_score(5)
            if collision(rect7,mousepos) and score[6]==3:
                draw_figure((50,2*h//3+50),flag)
                add_score(6)
            if collision(rect8,mousepos) and score[7]==3:
                draw_figure((w//3+50,2*h//3+50),flag)
                add_score(7)
            if collision(rect9,mousepos) and score[0]==3:
                draw_figure((2*w//3+50,2*h//3+50),flag)
                add_score(8)
            flag=flag*(-1)
            check_win()

pygame.quit()
