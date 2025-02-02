from pygame.locals import *
import pygame
import time, os

pygame.init()
screen= pygame.display.set_mode((600, 600))
bg= pygame.image.load(os.path.join("images", "background.png"))
pygame.display.update()
keys=[False, False, False, False]
rocket= pygame.image.load(os.path.join("images", "rocket.png"))
pygame.display.update()

rocket_x= 300
rocket_y= 300

while rocket_y< 600:
    screen.blit(bg, (0, 0))
    screen.blit(rocket, (rocket_x, rocket_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            print("hello")
            if event.key == pygame.K_UP:
                print("hi")
                keys[0]= True
            elif event.key== pygame.K_LEFT:
                keys[1]= True
            elif event.key == pygame.K_DOWN:
                keys[2]= True
            elif event.key == pygame.K_RIGHT:
                keys[3]= True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0]= False
            elif event.key== pygame.K_LEFT:
                keys[1]= False
            elif event.key == pygame.K_DOWN:
                keys[2]= False
            elif event.key == pygame.K_RIGHT:
                keys[3]= False
    if keys[0]:
        if rocket_y> 0:
            rocket_y-= 5
    if keys[1]:
        if rocket_x> 0:
            rocket_x-= 2
    if keys[2]:
        if rocket_y< 600:
            rocket_y+= 5
    if keys[3]:
        if rocket_x< 600:
            rocket_x+= 2
    
    rocket_y+= 3
    time.sleep(0.05)

print("GAME OVER")