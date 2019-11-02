from gui import *






def main():
    while True:
        
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

        for spikemonsters in spikemonster_list:
            if spikemonsters.direction == "x":
                spikemonsters.move(spikemonsters.speed, 0, current_map.tiles)
            if spikemonsters.direction == "y":
                spikemonsters.move(0, spikemonsters.speed, current_map.tiles)
        for spikemonsters in spikemonster_list:
            screen.blit(spikemonsters.image, spikemonsters.rect)
        if player.die():
            Intro()
        door.onChangeMap()
        pygame.display.flip()
        
        screen.fill(0)
def Intro():
    button('hello', (0, 60, 255), 10, 10, 100, 100)

def map1():
    global current_map
    current_map = Map1()
    current_map.draw()
    global image
    global door
    image = pygame.transform.scale(assetLibrary['sky'], (640, 480))
    door = Door((19*32,26*16), "1")


map1()
main()

    

    
            