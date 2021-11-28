import pygame
import random as rd
from pygame.locals import *
pygame.init()
FPS = 10
FramePerSec = pygame.time.Clock()
pygame.font.init()
pygame.display.set_caption("SNAKE")
surf = pygame.display.set_mode((600, 600))
myfont = pygame.font.SysFont('Comic Sans MS', 50)
myfont2 = pygame.font.SysFont('Comic Sans MS', 30)

class Snake:
    def __init__(self):
        self.location = [[0,0],[200,200]]
        self.x = 20
        self.y = 0
        self.step = 20
        self.ilo = 2
        self.tobreak = 0
        self.foodloc = [[rd.randrange(0, 580, 20), rd.randrange(0, 580, 20)]]

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.location[-1][1] > 0:
            if pressed_keys[K_UP]:
                self.y = (-1) * self.step
                self.x = 0
        if self.location[-1][1] < 580:
            if pressed_keys[K_DOWN]:
                self.y = self.step
                self.x = 0
        if self.location[-1][0] > 0:
            if pressed_keys[K_LEFT]:
                self.x = (-1) * self.step
                self.y = 0
        if self.location[-1][0] < 580:
            if pressed_keys[K_RIGHT]:
                self.x = self.step
                self.y = 0
        self.location.append([self.location[-1][0] + self.x, self.location[-1][1] + self.y])

    def limits(self):
        if self.location[-1][0] == -20 and self.x == -self.step or self.location[-1][0] == 600 and self.x == self.step:
            return 1
        if self.location[-1][1] == -20 and self.y == -self.step or self.location[-1][1] == 600 and self.y == self.step:
            return 1
        if self.location[-1] in self.location[-self.ilo:-1]:
            return 1
    def food(self):
        if self.location[-1] == self.foodloc[0]:
            self.foodloc = [[rd.randrange(0, 580, 20), rd.randrange(0, 580, 20)]]
            while self.foodloc[0] in self.location[-self.ilo:-1]:
                print("pentla")
                self.foodloc = [[rd.randrange(0, 580, 20), rd.randrange(0, 580, 20)]]
            self.ilo += 1
    def reset(self):
        self.location = [[0, 0], [200, 200]]
        self.x = 20
        self.y = 0
        self.step = 20
        self.ilo = 2
        self.tobreak = 0
        self.foodloc = [[rd.randrange(0, 580, 20), rd.randrange(0, 580, 20)]]

gameover = 0
snake1 = Snake()
while True:
    while gameover == 0:
        surf.fill('Black')
        snake1.move()
        snake1.food()
        if snake1.limits() == 1:
            break
        pygame.draw.rect(surf, 'BLUE', (snake1.foodloc[0][0], snake1.foodloc[0][1], 20, 20))
        for i in range(snake1.ilo):
            i += 1
            pygame.draw.rect(surf, 'GREEN', (snake1.location[-i][0], snake1.location[-i][1], 20, 20))
        pygame.display.update()
        FramePerSec.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    snake1.reset()
    gameover = 1
    textsurface = myfont.render('Game over', False, (255, 255, 255))
    textsurface2 = myfont2.render('To continue press Enter', False, (255, 255, 255))
    textsurface3 = myfont2.render('To exit press ESC', False, (255, 255, 255))
    surf.blit(textsurface, (180, 200))
    surf.blit(textsurface2, (120, 290))
    surf.blit(textsurface3, (120, 350))
    ppp = pygame.key.get_pressed()
    if ppp[K_RETURN]:
        gameover = 0
    if ppp[K_ESCAPE]:
        break
    pygame.display.update()
    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

