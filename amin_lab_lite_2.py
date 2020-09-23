import pygame
import sys
import time
import random
import pickle
import math

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AIM_LAB_Lite")

x = random.randint(0, 750)
y = random.randint(0, 550)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
# bg = pygame.image.load("bg.jpg")
bgx = 0
bgy = 0

high_score_1 = 0
high_score_2 = 0
high_score_3 = 0

def mainwinnDrow():
    global i,j,k
    win.fill((0,0,0))
    ff = pygame.font.SysFont('comicsans', 100)
    tt = ff.render("AIM LAB", 1, (i, j, k))
    win.blit(tt, (250, 90))


    pygame.draw.rect(win, (0,255,0), (250, 200, 300, 40))
    f1 = pygame.font.SysFont('comicsans', 30)
    t1 = f1.render("EASY", 1, (255, 255, 255))
    win.blit(t1, ((250 + (150 - t1.get_width() // 2), 210)))
    pygame.draw.rect(win, (0,0,255), (250, 280, 300, 40))
    f2 = pygame.font.SysFont('comicsans', 30)
    t2 = f2.render("MEDIUM", 1, (255, 255, 255))
    win.blit(t2, ((250 + (150 - t2.get_width() // 2), 290)))
    pygame.draw.rect(win, (255,0,0), (250, 360, 300, 40))
    f3 = pygame.font.SysFont('comicsans', 30)
    t3 = f3.render("HARD", 1, (255, 255, 255))
    win.blit(t3, ((250 + (150 - t3.get_width() // 2), 370)))


def easy(win):
    global r,g,b,x,y,high_score_1,bgx,bgy
    pygame.mouse.set_visible(False)
    start_time = time.time()
    score = 0
    miss = 0
    # pygame.draw.rect(win, (r, g, b), (x, y, 50, 50))
    pygame.draw.circle(win, (r,g,b), (x,y), 25)
    win.fill((0,0,0))
    start_time = time.time()
    run = True
    while run:
        pygame.mouse.set_pos([400, 300])

        tx,ty = pygame.mouse.get_pos()
        x += ((400 - tx) * 1)
        y += ((300 - ty) * 1)
        bgx += ((400 - tx) * 0.5)
        bgy += ((300 - ty) * 0.5)
        win.fill((0,0,0))
                 
        # win.blit(bg, (bgx, bgy))
        pygame.draw.circle(win, (0,255,0), (x,y), 25)
        pygame.draw.circle(win, (255,255,0), (400,300), 3)

        fs = pygame.font.SysFont('comicsans', 25)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (650, 10))

        fh = pygame.font.SysFont('comicsans', 25)
        th = fh.render("HIGH SCORE: " + str(high_score_1), 1, (255, 255, 255))
        win.blit(th, (10, 10))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                # if x in range(350, 400) and y in range(250, 300):
                if math.sqrt((400 - x)**2 + (300 - y)**2) <= 25:
                    x = random.randint(0, 750)
                    y = random.randint(0, 550)
                    score += 1
                else:
                    miss += 1

        if time.time() - start_time > 60:
            run = False

        pygame.display.update()

    if score > high_score_1:
        high_score_1 = score

    win.fill((0,0,0))
    temp = True
    while temp:
        pygame.mouse.set_visible(True)
        fs = pygame.font.SysFont('comicsans', 50)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (400 - (ts.get_width() // 2), 200))

        fm = pygame.font.SysFont('comicsans', 30)
        tm = fm.render("MISS: " + str(miss), 1, (255, 255, 255))
        win.blit(tm, (400 - (tm.get_width() // 2), 250))

        fh = pygame.font.SysFont('comicsans', 30)
        th = fh.render("HIGH SCORE: " + str(high_score_1), 1, (255, 255, 255))
        win.blit(th, (400 - (th.get_width() // 2), 280))

        pygame.draw.rect(win, (255,0,0), (250, 360, 300, 40))
        f3 = pygame.font.SysFont('comicsans', 30)
        t3 = f3.render("HOME", 1, (255, 255, 255))
        win.blit(t3, ((250 + (150 - t3.get_width() // 2), 370)))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                if xx in range(250, 550) and yy in range(360, 400):
                    temp = False

        pygame.display.update()


def medium(win):
    global r,g,b,x,y,high_score_2
    pygame.mouse.set_visible(False)
    start_time = time.time()
    score = 0
    miss = 0
    # pygame.draw.rect(win, (r, g, b), (x, y, 50, 50))
    pygame.draw.circle(win, (r,g,b), (x,y), 12)
    win.fill((0,0,0))
    start_time = time.time()
    run = True
    while run:
        pygame.mouse.set_pos([400, 300])

        tx,ty = pygame.mouse.get_pos()
        x += ((400 - tx) * 1)
        y += ((300 - ty) * 1)
        win.fill((0,0,0))
        # pygame.draw.rect(win, (0,255,0), (x,y,50,50))
        pygame.draw.circle(win, (0,255,0), (x,y), 12)
        pygame.draw.circle(win, (255,255,0), (400,300), 3)

        fs = pygame.font.SysFont('comicsans', 25)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (650, 10))

        fh = pygame.font.SysFont('comicsans', 25)
        th = fh.render("HIGH SCORE: " + str(high_score_1), 1, (255, 255, 255))
        win.blit(th, (10, 10))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                # if x in range(350, 400) and y in range(250, 300):
                if math.sqrt((400 - x)**2 + (300 - y)**2) <= 12:
                    x = random.randint(0, 750)
                    y = random.randint(0, 550)
                    score += 1
                else:
                    miss += 1

        if time.time() - start_time > 60:
            run = False

        pygame.display.update()

    if score > high_score_2:
        high_score_2 = score

    win.fill((0,0,0))
    temp = True
    while temp:
        pygame.mouse.set_visible(True)
        fs = pygame.font.SysFont('comicsans', 50)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (400 - (ts.get_width() // 2), 200))

        fm = pygame.font.SysFont('comicsans', 30)
        tm = fm.render("MISS: " + str(miss), 1, (255, 255, 255))
        win.blit(tm, (400 - (tm.get_width() // 2), 250))

        fh = pygame.font.SysFont('comicsans', 30)
        th = fh.render("HIGH SCORE: " + str(high_score_1), 1, (255, 255, 255))
        win.blit(th, (400 - (th.get_width() // 2), 280))

        pygame.draw.rect(win, (255,0,0), (250, 360, 300, 40))
        f3 = pygame.font.SysFont('comicsans', 30)
        t3 = f3.render("HOME", 1, (255, 255, 255))
        win.blit(t3, ((250 + (150 - t3.get_width() // 2), 370)))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                if xx in range(250, 550) and yy in range(360, 400):
                    temp = False

        pygame.display.update()

    
def hard(win):
    global r,g,b,x,y,high_score_3
    pygame.mouse.set_visible(False)
    start_time = time.time()
    score = 0
    miss = 0
    # pygame.draw.rect(win, (r, g, b), (x, y, 50, 50))
    pygame.draw.circle(win, (r,g,b), (x,y), 7)
    win.fill((0,0,0))
    start_time = time.time()
    run = True
    while run:
        pygame.mouse.set_pos([400, 300])

        tx,ty = pygame.mouse.get_pos()
        x += ((400 - tx) * 1)
        y += ((300 - ty) * 1)
        win.fill((0,0,0))
        # pygame.draw.rect(win, (0,255,0), (x,y,50,50))
        pygame.draw.circle(win, (0,255,0), (x,y), 7)
        pygame.draw.circle(win, (255,255,0), (400,300), 3)

        fs = pygame.font.SysFont('comicsans', 25)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (650, 10))

        fh = pygame.font.SysFont('comicsans', 25)
        th = fh.render("HIGH SCORE: " + str(high_score_1), 1, (255, 255, 255))
        win.blit(th, (10, 10))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                # if x in range(350, 400) and y in range(250, 300):
                if math.sqrt((400 - x)**2 + (300 - y)**2) <= 7:
                    x = random.randint(0, 750)
                    y = random.randint(0, 550)
                    score += 1
                else:
                    miss += 1

        if time.time() - start_time > 60:
            run = False

        pygame.display.update()

    if score > high_score_3:
        high_score_3 = score

    win.fill((0,0,0))
    temp = True
    while temp:
        pygame.mouse.set_visible(True)
        fs = pygame.font.SysFont('comicsans', 50)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (400 - (ts.get_width() // 2), 200))

        fm = pygame.font.SysFont('comicsans', 30)
        tm = fm.render("MISS: " + str(miss), 1, (255, 255, 255))
        win.blit(tm, (400 - (tm.get_width() // 2), 250))

        fh = pygame.font.SysFont('comicsans', 30)
        th = fh.render("HIGH SCORE: " + str(high_score_1), 1, (255, 255, 255))
        win.blit(th, (400 - (th.get_width() // 2), 280))

        pygame.draw.rect(win, (255,0,0), (250, 360, 300, 40))
        f3 = pygame.font.SysFont('comicsans', 30)
        t3 = f3.render("HOME", 1, (255, 255, 255))
        win.blit(t3, ((250 + (150 - t3.get_width() // 2), 370)))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                if xx in range(250, 550) and yy in range(360, 400):
                    temp = False

        pygame.display.update()



start_time = time.time()
i,j,k =  10,245,10
t = 0
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            tx, ty = pygame.mouse.get_pos()
            if tx in range(250, 550) and ty in range(200, 240):
                x,y = random.randint(0,800),random.randint(0,600)
                easy(win)
            elif tx in range(250, 550) and ty in range(280, 320):
                x,y = random.randint(0,800),random.randint(0,600)
                medium(win)
            elif tx in range(250, 550) and ty in range(360, 400):
                x,y = random.randint(0,800),random.randint(0,600)
                hard(win)
            else:
                continue

    i = (i + 1) % 255
    j = (j + 2) % 255
    k = (k + 3) % 255

    mainwinnDrow()

    time.sleep(0.03)
    pygame.display.update()

pygame.quit()