import pygame
import pymunk
import sys
import random


def create_apple(space, pos):
    body = pymunk.Body(1,50,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,45)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)
        
def static_ball(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (random.randrange(0,800,50), random.randrange(0,800,50))
    shape = pymunk.Circle(body,10)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x, pos_y), 10)
        


pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,600)
png = pygame.image.load('orange.png')
apple_surface = pygame.transform.scale(png, (100,100))
apples = []

balls = []
for i in range(0,15):
    balls.append(static_ball(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))
            
    screen.fill((217,217,217))
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/100)
    pygame.display.update()
    clock.tick(144)
