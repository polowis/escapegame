from assets import *



while True:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    clock.tick(60)
    screen.fill(0)
    current_map = Map1()
    current_map.draw()
    player.handle_input(current_map)
    screen.blit(player.image,player.rect)
    for spikemonsters in lists:
        if spikemonsters.direction == "x":
            spikemonsters.move(spikemonsters.speed, 0 , current_map.tiles)
            screen.blit(spikemonsters.image, spikemonsters.rect)
    #for spikemonsters in lists:
    #screen.blit(spike_image, spike)
    
    pygame.display.flip()
   
    
    
   
    
    
            