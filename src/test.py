import pygame, sys
pygame.init()
window=pygame.display.set_mode((1500, 800))
background=pygame.Surface((window.get_rect().width, window.get_rect().height))
background.fill((0, 0, 0))
image=pygame.image.load('asset/sky.gif')
image=image.convert()
image2=pygame.image.load('asset/menu.gif')
image2=image2.convert()
rect=image.get_rect()
rect2=image2.get_rect()
rect2.left=rect.width+1
i=1
while True:
    for event in pygame.event.get():
        if event.type==12:
            pygame.quit()
            sys.exit()
    image.set_alpha(255)
    image2.set_alpha(i)
    window.fill((255, 255, 255))
    window.blit(background, background.get_rect())
    window.blit(image, rect)
    window.blit(image2, rect2)
    pygame.time.delay(20)
    i+=1
    if i==255:
        i=1
    pygame.display.update()