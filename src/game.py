"""
Game: Use arrow keys to move, use space to shoot
This game has 3 levels in total
Pick up keys along the way to unlock the next door
The third level is the hardest. The player has to dodge incoming bullets
We represent the bullet in white circle and the player need to manage to get close to
the boss in order to kill him. Player can upgrade weapon damage in shop. 
Player can earn coin by killing monsters
"""


from gui import *
import random

bullet_scale = pygame.transform.scale(assetLibrary['bullet'], (10, 10))

def Menu():
    """Menu starting screen"""
    background_image = pygame.transform.scale(assetLibrary['menu'], (640, 480))
    background_x = background_image.get_rect()
    while player.state == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.set_caption("Escape game")
        clock.tick(60)
        cursor = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        background_image.set_alpha(1)
        screen.blit(background_image, (0, 0))
        text2 = text('Play', (0, 70, 255), 255, 250, 110, 25)
        text3 = text('How to play', (0, 70, 255), 255, 320, 120, 25)
        if 255 + 110 > cursor[0] > 255 and 250 + 25 > cursor[1] > 250:
            text2 = text("Play", (255, 0, 0), 255, 250, 110, 25)
            if mouse[0] == 1:
                player.state = "play"
                mainloop()
        else:
            text2 = text('Play', (0, 70, 255), 255, 250, 110, 25)

        if 255 + 120 > cursor[0] > 255 and 320 + 25 > cursor[1] > 320:
            text3 = text('How to play', (255, 0, 0), 255, 320, 120, 25)
            if mouse[0] == 1:
                player.state = "howtoplay"
                how_to_play()
        else:
            text3 = text('How to play', (0, 70, 255), 255, 320, 120, 25)
        
        if 255 + 110 > cursor[0] > 255 and 200 + 25 > cursor[1] > 200:
            text4 = text('Shop', (255, 0, 0), 255, 200, 110, 25)
            if mouse[0] == 1:
                player.state = "upgrade"
                upgrade()
        else:
            text4 = text('Shop', (0, 70, 255), 255, 200, 110, 25)
            
        

        
        pygame.display.update()
        screen.fill(0)

def make_bullet():
    """
    Function to make a new, random circle.
    """
    eBullet = Enemy_bullet()
    
    eBullet.x = random.randrange(10, width - 10)
    eBullet.y = random.randrange(10, height - 10)
 
    # Speed and direction of rectangle
    eBullet.change_x = random.randrange(-2, 3)
    eBullet.change_y = random.randrange(-2, 3)
 
    return eBullet       

def main():
    
    """map1"""
    while player.state == "play":
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        pygame.display.set_caption("Escape game")
        clock.tick(60)
        player.handle_input(current_map)
        
        screen.blit(image, (0, 0))
        for tile in tile_list:
            screen.blit(tile.image, tile.rect)
        screen.blit(door.image, door.rect)
        screen.blit(player.image,player.rect)
        screen.blit(key.image, key.rect)
        
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
            pygame.draw.rect(screen, (255, 0, 0), (spikemonsters.rect.x, spikemonsters.rect.y - 10, spikemonsters.rect.width, 5))
            screen.blit(spikemonsters.image, spikemonsters.rect)
        onCollide()
        if(player.die()):
                player.state = "gameover"
                Intro()
        door.onChangeMap()
        key.checkKey()
        pygame.display.flip()
        
        screen.fill(0)


def onCollide():
    """Check if bullet hit monster"""
    for bullet in bullet_list:
        for spikemonsters in spikemonster_list:
            spikemonsterHealthBar = pygame.draw.rect(screen, (255, 0, 0), (spikemonsters.rect.x, spikemonsters.rect.y - 10, spikemonsters.health, 5))
            if bullet.rect.colliderect(spikemonsters.rect):
                spikemonsterHealthBar.width -= 5
                spikemonsters.health -= player.damage
                if spikemonsters.die():
                    spikemonsters.kill()
                    player.coin += 1
                bullet.kill()
        for monster in monster_list:
            monsterHealthBar = pygame.draw.rect(screen, (255, 0, 0), (monster.rect.x, monster.rect.y - 10, monster.health, 5))
            if bullet.rect.colliderect(monster.rect):
                monsterHealthBar.width -= 5
                monster.health -= player.damage
                if monster.die():
                    monster.kill()
                    player.coin += 1
                bullet.kill()
        for boss in boss_list:
            bossHealthBar = pygame.draw.rect(screen, (255, 0, 0), (boss.rect.x, boss.rect.y -10, boss.health, 5))
            if bullet.rect.colliderect(boss.rect):
                bossHealthBar.width -= 5
                boss.health -= player.damage
                if boss.die():
                    player.coin += 1
                    boss.kill()
def upgrade():
    background_a = pygame.transform.scale(pygame.image.load('asset/howtoplay.jpg').convert(), (640, 480))
    while player.state == "upgrade":
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.blit(background_a, (0,0))
        pygame.display.set_caption("Escape game")
        cursor = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        clock.tick(60)
        text3 = text('player coin: ' + str(player.coin), (255, 0, 0), 255, 200, 110, 25)
        if 255 + 110 > cursor[0] > 255 and 250 + 25 > cursor[1] > 250:
            text4 = text('Click to upgrade damage', (255, 0, 0), 255, 250, 110, 25)
            if mouse[0] == 1:
                if player.coin - 1 > 0:
                    player.damage += 1
                else:
                    player.coin = 0
        else:
            text4 = text('Click to upgrade damage', (0, 70, 255), 255, 250, 110, 25)
        if 255 + 120 > cursor[0] > 255 and 320 + 25 > cursor[1] > 320:
            text5 = text('Back to menu', (255, 0, 0), 255, 320, 120, 25)
            if mouse[0] == 1:
                player.state = "start"
                Menu()
        else:
            text5 = text('Back to menu', (0, 70, 255), 255, 320, 120, 25)

        pygame.display.flip()   
        screen.fill(0)           

def how_to_play():
    
    background_a = pygame.transform.scale(pygame.image.load('asset/howtoplay.jpg').convert(), (640, 480))
    while player.state == "howtoplay":
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.blit(background_a, (0,0))
        pygame.display.set_caption("Escape game")
        cursor = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        clock.tick(60)
        text4 = text('Use arrow key to move, \n press space to shoot', (0, 70, 255), 255, 250, 110, 25)
        if 255 + 120 > cursor[0] > 255 and 320 + 25 > cursor[1] > 320:
            text5 = text('Back to menu', (255, 0, 0), 255, 320, 120, 25)
            if mouse[0] == 1:
                player.state = "start"
                Menu()
        else:
            text5 = text('Back to menu', (0, 70, 255), 255, 320, 120, 25)

        pygame.display.flip()   
        screen.fill(0)           

def Intro():
    """When player dies"""
    while player.state == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(0)
        cursor = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        background_image = pygame.transform.scale(assetLibrary['menu'], (640, 480))
        screen.blit(background_image, (0, 0))
        """get mouse position and check if the player click"""
        if 255 + 110 > cursor[0] > 255 and 250 + 25 > cursor[1] > 250:
            pygame.draw.rect(screen, (255, 0, 0), (255, 250, 110, 25))
            if mouse[0] == 1:
                player.state = "play"
                mainloop()
        else:
            pygame.draw.rect(screen, (0,0,0), (255, 250, 110, 25))

        if 255 + 120 > cursor[0] > 255 and 320 + 25 > cursor[1] > 320:
            pygame.draw.rect(screen, (255, 0, 0), (255, 320, 110, 25))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (255, 300, 110, 25))
            

        text2 = text('Play again', (0, 70, 255), 255, 250, 110, 25)
        text3 = text('How to play', (0, 70, 255), 255, 320, 120, 25)
        pygame.display.update()

def clear():
    """clear everything"""
    global tile_list
    global spikemonster_list
    global player
    tile_list = []
    spikemonster_list = []
    del player

def map1():
    """draw map1"""
    #clear all the lists and update new list
    global tile_list
    global spikemonster_list
    global boss_list
    boss_list = []
    tile_list = []
    spikemonster_list = []
    global current_map
    current_map = Map1()
    current_map.draw()
    tile_list = current_map.tiles
    spikemonster_list = current_map.spikeMonsters
    global image
    global door
    global key
    image = pygame.transform.scale(assetLibrary['sky'], (640, 480))
    door = Door((19*32,26*16), "1")
    key = Key((400, 300), "key1")

def map2():
    """draw map2"""
    global tile_list
    global spikemonster_list
    global player
    global monster_list
    global boss_list
    boss_list = []
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
    global key
    door = Door((32,400), "2")
    key = Key((400, 300), "key2")

def map3():
    """draw map3"""

    global tile_list
    global spikemonster_list
    global player
    global monster_list
    global image
    global boss_list
    monster_list = []
    tile_list = []
    spikemonster_list = []
    boss_list = []
    global current_map
    current_map = Map3()
    current_map.draw()
    tile_list  = current_map.tiles
    spikemonster_list = current_map.spikemonster
    monster_list = current_map.monster
    image = pygame.transform.scale(assetLibrary['dungeon'], (640, 480))
    boss_list = current_map.boss

def mainloop():
    """main loop of the game"""
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
            screen.blit(key.image, key.rect)
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
            if(player.die()):
                player.state = "gameover"
                Intro()
            door.onChangeMap()
            key.checkKey()
            pygame.display.flip()
            screen.fill(0)

        
        if player.state == "finish2":
            map3()
            speed = [2, 2]
            
            eBullet_list = []
 
            
            for i in range(10):
                eBullet = make_bullet()
                eBullet_list.append(eBullet)
            while player.state == "finish2":
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                clock.tick(60)
                player.handle_input(current_map)
                screen.blit(image,(0, 0))
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
                for boss in boss_list:
                    screen.blit(boss.image, boss.rect)
                for bullet in eBullet_list:
                    # Move the ball's center
                    bullet.x += bullet.change_x
                    bullet.y += bullet.change_y
        
                    # Bounce the ball if needed
                for bullet in eBullet_list:
                    if bullet.y > height - 10 or bullet.y < 10:
                        bullet.change_y *= -1
                    if bullet.x > width - 10 or bullet.x < 10:
                        bullet.change_x *= -1

                # Draw the balls
                for bullet in eBullet_list:
                    enemy_bullet = pygame.draw.circle(screen, (255, 255, 255), [bullet.x, bullet.y], 10)
                    if player.rect.colliderect(enemy_bullet):
                        player.state = "gameover"
                        Intro()
                onCollide()
                if(player.die()):
                    player.state = "gameover"
                    Intro()
                player.die()
                door.onChangeMap()
                pygame.display.flip()




    
