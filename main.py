from assets import *






def main():
    print(player.rect)
    while player.state == "play":
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        clock.tick(60)
        player.handle_input(current_map)
        
        screen.blit(image, (0, 0))
        """for J in range(0,14):
            for k in range(0,20):
                screen.blit(assetLibrary['sky'], ((k*32),(J*32+128)))"""
        for tile in tile_list:
            screen.blit(tile.image, tile.rect)
        screen.blit(door.image, door.rect)
        screen.blit(player.image,player.rect)
        for i in bullet_list:
            if player.face == "right":
                i.x += 2
            if player.face == "left":
                i.x -= 2
        for i in bullet_list:
            screen.blit(assetLibrary['bullet'], i)
        
        for spikemonsters in spikemonster_list:
            if spikemonsters.direction == "x":
                spikemonsters.move(spikemonsters.speed, 0, current_map.tiles)
            if spikemonsters.direction == "y":
                spikemonsters.move(0, spikemonsters.speed, current_map.tiles)
        for spikemonsters in spikemonster_list:
            screen.blit(spikemonsters.image, spikemonsters.rect)
            
        door.onChangeMap()
        pygame.display.flip()
        
        screen.fill(0)

def black():
    while player.state == "play":
        screen.fill(0)
        pygame.display.update()

def Intro():
    screen.fill(0)
    button('hello', (0, 60, 255), 10, 10, 100, 100)
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
    global image
    global door
    image = pygame.transform.scale(assetLibrary['sky'], (640, 480))
    door = Door((19*32,26*16), "1")

def map2():
    global tile_list
    global spikemonster_list
    global player
    tile_list = []
    spikemonster_list = []
    global current_map
    current_map = Map2()
    current_map.draw()
    tile_list  = current_map.tiles
    global door
    door = Door((32,400), "2")

def Mainloop():
    while True:
        screen.fill(0)
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

        for spikemonsters in spikemonster_list:
            if spikemonsters.direction == "x":
                spikemonsters.move(spikemonsters.speed, 0, current_map.tiles)
            if spikemonsters.direction == "y":
                spikemonsters.move(0, spikemonsters.speed, current_map.tiles)
        for spikemonsters in spikemonster_list:
            screen.blit(spikemonsters.image, spikemonsters.rect)
            
        door.onChangeMap()
        pygame.display.flip()
        
        screen.fill(0)





    

    

    
            