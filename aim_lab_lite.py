import pygame
import sys
import time
import random

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AIM_LAB_Lite")
x = random.randint(0, 750)
y = random.randint(0, 550)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
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
    # fh = pygame.font.SysFont('comicsans', 25)
    # th = fh.render("HIGH SCORE: " + str(high_score), 1, (255, 255, 255))
    # win.blit(th, (10, 550)) 

def easy(win):
    global r,g,b,x,y,high_score_1
    score = 0
    miss = 0
    pygame.draw.rect(win, (r, g, b), (x, y, 50, 50))
    win.fill((0,0,0))
    #print("hello")
    start_time = time.time()
    run = True
    while run:
        pygame.draw.rect(win, (r,g,b), (x,y,50,50))
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
                xx, yy = pygame.mouse.get_pos()
                # print(xx, yy)
                if xx in range(x, x+50) and yy in range(y, y+50):
                    x = random.randint(30, 750)
                    y = random.randint(30, 550)
                    r = random.randint(100, 255)
                    g = random.randint(100, 255)
                    b = random.randint(100, 255)
                    win.fill((0,0,0))   
                    score += 1     
                else:
                    # print("GAME OVER")
                    miss += 1

        if time.time() - start_time > 60:
            run = False

        pygame.display.update()

    if score > high_score_1:
        high_score_1 = score

    win.fill((0,0,0))
    temp = True
    while temp:
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
    score = 0
    miss = 0
    pygame.draw.rect(win, (r, g, b), (x, y, 35, 35))
    win.fill((0,0,0))
    # print("hello")
    start_time = time.time()
    run = True
    while run:
        pygame.draw.rect(win, (r,g,b), (x,y,35,35))
        fs = pygame.font.SysFont('comicsans', 25)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (650, 10))

        fh = pygame.font.SysFont('comicsans', 25)
        th = fh.render("HIGH SCORE: " + str(high_score_2), 1, (255, 255, 255))
        win.blit(th, (10, 10))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                # print(xx, yy)
                if xx in range(x, x+35) and yy in range(y, y+35):
                    x = random.randint(30, 750)
                    y = random.randint(30, 550)
                    r = random.randint(100, 255)
                    g = random.randint(100, 255)
                    b = random.randint(100, 255)
                    win.fill((0,0,0))        
                    score += 1
                else:
                    # print("GAME OVER")
                    miss += 1

        if time.time() - start_time > 60:
            run = False

        pygame.display.update()
    
    if score > high_score_2:
        high_score_2 = score

    win.fill((0,0,0))
    temp = True
    while temp:
        fs = pygame.font.SysFont('comicsans', 50)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (400 - (ts.get_width() // 2), 200))

        fm = pygame.font.SysFont('comicsans', 30)
        tm = fm.render("MISS: " + str(miss), 1, (255, 255, 255))
        win.blit(tm, (400 - (tm.get_width() // 2), 250))

        fh = pygame.font.SysFont('comicsans', 30)
        th = fh.render("HIGH SCORE: " + str(high_score_2), 1, (255, 255, 255))
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
    score = 0
    miss = 0
    pygame.draw.rect(win, (r, g, b), (x, y, 20, 20))
    win.fill((0,0,0))
    print("hard")
    start_time = time.time()
    run = True
    while run:
        pygame.draw.rect(win, (r,g,b), (x,y,20,20))
        fs = pygame.font.SysFont('comicsans', 25)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (650, 10))

        fh = pygame.font.SysFont('comicsans', 25)
        th = fh.render("HIGH SCORE: " + str(high_score_3), 1, (255, 255, 255))
        win.blit(th, (10, 10))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                # print(xx, yy)
                if xx in range(x, x+20) and yy in range(y, y+20):
                    x = random.randint(30, 750)
                    y = random.randint(30, 550)
                    r = random.randint(100, 255)
                    g = random.randint(100, 255)
                    b = random.randint(100, 255)
                    win.fill((0,0,0))  
                    score += 1      
                else:
                    # print("GAME OVER")
                    miss += 1

        if time.time() - start_time > 60:
            run = False

        pygame.display.update()    

    if score > high_score_3:
        high_score_3 = score

    win.fill((0,0,0))
    temp = True
    while temp:
        fs = pygame.font.SysFont('comicsans', 50)
        ts = fs.render("SCORE: " + str(score), 1, (255, 255, 255))
        win.blit(ts, (400 - (ts.get_width() // 2), 200))

        fm = pygame.font.SysFont('comicsans', 30)
        tm = fm.render("MISS: " + str(miss), 1, (255, 255, 255))
        win.blit(tm, (400 - (tm.get_width() // 2), 250))

        fh = pygame.font.SysFont('comicsans', 30)
        th = fh.render("HIGH SCORE: " + str(high_score_3), 1, (255, 255, 255))
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
        # if e.type == pygame.MOUSEBUTTONDOWN:
        #     xx, yy = pygame.mouse.get_pos()
        #     print(xx, yy)
        #     if xx in range(x, x+50) and yy in range(y, y+50):
        #         x = random.randint(0, 750)
        #         y = random.randint(0, 550)
        #         r = random.randint(0, 255)
        #         g = random.randint(0, 255)
        #         b = random.randint(0, 255)
        #         win.fill((0,0,0))        
        #     else:
        #         print("GAME OVER")
        if e.type == pygame.MOUSEBUTTONDOWN:
            tx, ty = pygame.mouse.get_pos()
            if tx in range(250, 550) and ty in range(200, 240):
                easy(win)
            elif tx in range(250, 550) and ty in range(280, 320):
                medium(win)
            elif tx in range(250, 550) and ty in range(360, 400):
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