from gui import *

bullet_scale = pygame.transform.scale(assetLibrary['bullet'], (10, 10))


def main():
    while player.state == "play":
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        clock.tick(60)
        player.handle_input(current_map)
        
        screen.blit(image, (0, 0))
        for tile in tile_list:
            screen.blit(tile.image, tile.rect)
        screen.blit(door.image, door.rect)
        screen.blit(player.image,player.rect)
        
        for i in bullet_list:
            i.rect.x += i.direction
        for i in bullet_list:
            screen.blit(bullet_scale, i)
        
        for spikemonsters in spikemonster_list:
            if spikemonsters.direction == "x":
                spikemonsters.move(spikemonsters.speed, 0, current_map.tiles)
            if spikemonsters.direction == "y":
                spikemonsters.move(0, spikemonsters.speed, current_map.tiles)
        for spikemonsters in spikemonster_list:
            screen.blit(spikemonsters.image, spikemonsters.rect)
        onCollide()
        player.die()
        door.onChangeMap()
        pygame.display.flip()
        
        screen.fill(0)


def onCollide():
    for bullet in bullet_list:
        for spikemonsters in spikemonster_list:
            if bullet.rect.colliderect(spikemonsters.rect):
                spikemonsters.rect.x += 1000
                bullet.rect.x += 1000
        for monster in monster_list:
            if bullet.rect.colliderect(monster.rect):
                monster.rect.x += 1000
                bullet.rect.x += 1000
               

def Intro():
    screen.fill(0)
    cursor = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    background_image = pygame.transform.scale(assetLibrary['gameover'], (640, 480))
    screen.blit(background_image, (0, 0))
    if 255 + 110 > cursor[0] > 255 and 250 + 25 > cursor[1] > 250:
        pygame.draw.rect(screen, (255, 0, 0), (255, 250, 110, 25))
        if mouse[0] == 1:
            player.state = "play"
            mainloop()
    else:
        pygame.draw.rect(screen, (0,0,0), (255, 250, 110, 25))

    if 255 + 120 > cursor[0] > 255 and 300 + 25 > cursor[1] > 250:
        pygame.draw.rect(screen, (255, 0, 0), (255, 300, 110, 25))
    else:
        pygame.draw.rect(screen, (0, 0, 0), (255, 300, 110, 25))
    

    text2 = text('Play again', (0, 70, 255), 255, 250, 110, 25)
    text3 = text('How to play', (0, 70, 255), 255, 300, 120, 25)
    pygame.display.update()

def clear():
    global tile_list
    global spikemonster_list
    global player
    tile_list = []
    spikemonster_list = []
    del player

def map1():
    global tile_list
    global spikemonster_list
    tile_list = []
    spikemonster_list = []
    global current_map
    current_map = Map1()
    current_map.draw()
    tile_list = current_map.tiles
    spikemonster_list = current_map.spikeMonsters
    global image
    global door
    image = pygame.transform.scale(assetLibrary['sky'], (640, 480))
    door = Door((19*32,26*16), "1")

def map2():
    global tile_list
    global spikemonster_list
    global player
    global monster_list
    monster_list = []
    tile_list = []
    spikemonster_list = []
    global current_map
    current_map = Map2()
    current_map.draw()
    tile_list  = current_map.tiles
    spikemonster_list = current_map.spikemonster
    monster_list = current_map.monster
    global door
    door = Door((32,400), "2")

def mainloop():
    map1()
    main()
    if player.state == "finish1":
        map2()
        while player.state == "finish1":
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            clock.tick(60)
            player.handle_input(current_map)
            
            screen.blit(image, (0, 0))
            for tile in tile_list:
                screen.blit(tile.image, tile.rect)
            screen.blit(door.image, door.rect)
            screen.blit(player.image,player.rect)

            for i in bullet_list:
                i.rect.x += i.direction
            for i in bullet_list:
                screen.blit(bullet_scale, i)
            
            if player.rect.x < 210:
                for spikemonsters in spikemonster_list:
                    if spikemonsters.direction == "x":
                        spikemonsters.move(spikemonsters.speed, 0, current_map.tiles)
                    if spikemonsters.direction == "y":
                        spikemonsters.move(0, spikemonsters.speed, current_map.tiles)
                for spikemonsters in spikemonster_list:
                    screen.blit(spikemonsters.image, spikemonsters.rect)
            for monster in monster_list:
                monster.move(monster.direction,0, current_map.tiles)
                if monster.rect.bottom < 480:
                        monster.move(0,2, current_map.tiles)
            for monster in monster_list:
                screen.blit(monster.image,monster.rect)
            onCollide()
            player.die()
            door.onChangeMap()
            pygame.display.flip()
            
            screen.fill(0)
mainloop()

if player.state == "gameover":
    while player.state == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        Intro()





    

    

    
