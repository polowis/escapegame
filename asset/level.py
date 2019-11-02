import pygame
import os
class Player(object):

    def __init__(self,posx,posy):
        self.Image = pygame.image.load("mikenewright.gif")
        self.rect = pygame.Rect(posx,posy,16,30)
        self.jump = 0
        self.releasekey = True
        self.gameover = 0
        self.fall = 1
    def move(self,dx,dy):

        if dx != 0:
            if (self.rect.left + dx) > 0:
                if (self.rect.right + dx) < 640:
                    self.move_along_axis(dx,0)
                
        if dy != 0:
            if (self.rect.top + dy) > 0:
                if(self.rect.bottom + dy) < (screen.get_height() + 2):
                    self.move_along_axis(0,dy)
        if dx <0:
            self.Image = pygame.image.load("mikenewleft.gif")

        if dx > 0:
            self.Image = pygame.image.load("mikenewright.gif")
    def move_along_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if dx > 0:
                    self.rect.right = tile.rect.left
                elif dx < 0:
                    self.rect.left = tile.rect.right
                elif dy > 0:
                    self.rect.bottom = tile.rect.top
                    self.jump = 0
                    self.releasekey = False
                elif dy < 0:
                    self.rect.top = tile.rect.bottom

        for ramp in ramps:
            if self.rect.colliderect(ramp.rect):
                self.fall = 0
                if dx > 0 and ramp.ramp_sloped == "left":
                   self.rect.y -= 4
                if dx < 0 and ramp.ramp_sloped == "left":
                    self.rect.y += 2
                if dx > 0 and ramp.ramp_sloped == "right":
                    self.rect.y -= 2
                if dx < 0 and ramp.ramp_sloped == "right":
                    self.rect.y += 4
                
            else:
                self.fall = 1
                
    def check_death(self):
        for monster in monsters:
            if self.rect.colliderect(monster.rect):
                self.die()
        for trap in traps:
            if self.rect.colliderect(trap.rect):
                self.die()
        for spikemonster in spikemonsters:
            if self.rect.colliderect(spikemonster.rect):
                self.die()
        if self.rect.bottom >= 480:
            self.die()

    def die(self):
        for a in range (0,1000):
            screen.blit(game_over, (320,200))
        self.gameover = 1



class Monster(object):
    def __init__(self,posx,posy,imageR,imageL,rectx,recty):
        monsters.append(self)
        self.ImageL = imageL
        self.ImageR = imageR
        self.Image = pygame.image.load(self.ImageL)
        self.rect = pygame.Rect(posx,posy,rectx,recty)
        self.direction = 1
    def move(self,dx,dy):
        if dx != 0:
            if (self.rect.left + dx) > 0:
                if (self.rect.right + dx) < 640:
                    if dx > 0:
                        self.move_along_axis(dx,0)
                        self.Image = pygame.image.load(self.ImageL)
                    if dx < 0:
                        self.move_along_axis(dx,0)
                        self.Image = pygame.image.load(self.ImageR)
            if (self.rect.left + dx <= 0) or (self.rect.right + dx) >= 640:
                self.direction = -self.direction
        if dy != 0:
            self.move_along_axis(dx,dy)
            
    def move_along_axis(self,dx,dy):

        self.rect.x += dx
        self.rect.y += dy
        
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if dx > 0:
                    self.rect.right = tile.rect.left
                    self.direction = -self.direction
                elif dx < 0:
                    self.rect.left  = tile.rect.right
                    self.direction = -self.direction
                if dy > 0:
                    self.rect.bottom = tile.rect.top
                if dy < 0:
                    self.rect.top = tile.rect.bottom

        for ramp in ramps:
            if self.rect.colliderect(ramp.rect):
                self.fall = 0
                if dx > 0 and ramp.ramp_sloped == "left":
                    self.rect.y -= 4
                if dx < 0 and ramp.ramp_sloped == "left":
                    self.rect.y -= 1
                if dx > 0 and ramp.ramp_sloped == "right":
                    self.rect.y -= 0
                if dx < 0 and ramp.ramp_sloped == "right":
                    self.rect.y += 4
class Spikemonster(object):

    def __init__(self, pos,direction,speed):
        spikemonsters.append(self)
        self.Image = pygame.image.load("spikeblock.gif")
        self.Image = self.Image.convert()
        self.rect = pygame.Rect(pos[0],pos[1], 21 , 21)
        self.speed = speed
        self.direction = direction

    def move(self, dx, dy):
        if dx != 0:
            self.move_along_axis(dx,0)
        if dy != 0:
            self.move_along_axis(0,dy)
        
    def move_along_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if dx > 0:
                    self.rect.right = tile.rect.left
                    self.speed = - self.speed
                elif dx < 0:
                    self.rect.left = tile.rect.right
                    self.speed = -self.speed
                elif dy > 0:
                    self.rect.bottom = tile.rect.top
                    self.speed = -self.speed
                elif dy < 0:
                    self.rect.top = tile.rect.bottom
                    self.speed = -self.speed

    
class Tile(object):

    def __init__(self, pos, image):
        tiles.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 16)
        self.Image = pygame.image.load(image)
        self.Image = self.Image.convert()

class Ramp(object):
    def __init__(self, pos, image, slope_dir):
        ramps.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.Image = pygame.image.load(image)
        self.Image = self.Image.convert()
        self.ramp_sloped = slope_dir

class Spike(object):
    def __init__(self, pos, image):
        traps.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32,8)
        self.Image = pygame.image.load("spikes2.gif")
        self.Image = self.Image.convert()

class Door(object):
    def __init__(self,pos,image,level_on):
        endpoints.append(self)
        self.rect = pygame.Rect(pos[0],pos[1], 32, 32)
        self.Image = pygame.image.load(image)
        self.Image = self.Image.convert()
        self.level = level_on
    def end_check(self):
        if self.rect.colliderect(player.rect):
            for a in range(0,1000):
                screen.blit(level_complete, (320,200))
            if self.level == "level1":
                global level1
                level1 = "complete"
            if self.level == "level2":
                global level2
                level2 = "complete"
            if self.level == "level3":
                global level3
                level3 = "complete"
            if self.level == "level4":
                global level4
                level4 = "complete"
            if self.level == "level5":
                global level5
                level5 = "complete"
            player.gameover = 1
                
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Get to the door!")

game_over = pygame.image.load("gameover.gif")
game_over = game_over.convert()

level_complete = pygame.image.load("levelcomplete.gif")
level_complete = level_complete.convert()
clock = pygame.time.Clock()


level1 = "incomplete"
def level1():
    pygame.display.set_caption("get to the door!  use arrow keys to move")
    global tiles
    tiles = []
    global ramps
    ramps = []
    global traps
    traps = []
    level = [
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000330",
            "00000000000000000440",
            "00000000000000033440",
            "00000000000000044440",
            "00000000000003344440",
            "00000000000004444440",
            "00000000000334444440",
            "00000000000444444440",
            "00000000033444444440",
            "00000000044444444440",
            "33333333344444444444",
            "44444444444444444444",
    ]
    x = y = 0
    for row in level:
        for col in row:
            if col == "3":
                Tile((x,y,),"tiletop2.gif")
            if col == "4":
                Tile((x,y,),"tilebottom3.gif")
            if col == "5":
                Ramp((x,y,),"rampright.gif","right")
            if col == "6":
                Ramp((x,y,),"rampleft.gif","left")
            x += 32
        y += 16
        x = 0

    global player
    player = Player(32,32*14)

    global monsters
    monsters = []

    global spikemonsters
    spikemonsters = []
    global spikemonster
    spikemonster = Spikemonster( (32,24*16), "x", 2)


    global endpoints
    endpoints = []
    global door
    door = Door((19*32,26*16), "door.gif","level1")

    global stars
    stars = pygame.image.load("stars.gif")
    stars = stars.convert()
    global stars2
    stars2 = pygame.image.load("stars2.gif")
    stars2 = stars2.convert()
    
    
level2 = "incomplete"
def level2():
    global tiles
    tiles = []
    global ramps
    ramps = []
    global traps
    traps = []
    level = [
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000003000000030000",
            "00000004444444440000",
            "00000300000000000000",
            "00000000000000000000",
            "00003000000000000300",
            "00000000000000000000",
            "33330000000000000033",
            "44440000000000000044",
        ]

    x = y = 0
    for row in level:
        for col in row:
            if col == "3":
                Tile((x,y,),"tiletop2.gif")
            if col == "4":
                Tile((x,y,),"tilebottom3.gif")
            if col == "5":
                Ramp((x,y,),"rampright.gif","right")
            if col == "6":
                Ramp((x,y,),"rampleft.gif","left")
            x += 32
        y += 16
        x = 0
        
    global player
    player = Player(32,32*14)

    global monsters
    monsters = []
    global monster
    monster = Monster(9*32,20*16,"dinosaur.gif","dinosaur small.gif",27,29)

    global spikemonsters
    spikemonsters = []

    global endpoints
    endpoints = []
    global door
    door = Door((19*32,13*32), "door.gif","level2")
    global stars
    stars = pygame.image.load("stars.gif")
    stars = stars.convert()
    global stars2
    stars2 = pygame.image.load("stars2.gif")
    stars2 = stars2.convert()

level3 = "incomplete"
def level3():
    global tiles
    tiles = []
    global ramps
    ramps = []
    global traps
    traps = []
    level = [
            "44444444444444444444",
            "44000000000000000000",
            "44000000000000000000",
            "40004000000000000000",
            "40004000000000000000",
            "40304000063333500000",
            "40004000004444000000",
            "40004000644444450000",
            "43004000044444400000",
            "40004006444444445000",
            "40004000444444440000",
            "40304334444444444333",
            "40004000000000000000",
            "40004000000000000000",
            "43000000000000000000",
            "40000000000000030000",
            "40000000000000040000",
            "43333333333333340000",
            "44444444444444440030",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000003000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000003",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000300",
            "33333303300333000033",
            "44444404400444000044",
        ]

    x = y = 0
    for row in level:
        for col in row:
            if col == "3":
                Tile((x,y,),"tiletop2.gif")
            if col == "4":
                Tile((x,y,),"tilebottom3.gif")
            if col == "5":
                Ramp((x,y,),"rampright.gif","right")
            if col == "6":
                Ramp((x,y,),"rampleft.gif","left")
            x += 32
        y += 16
        x = 0
        
    global player
    player = Player(32,32*14)

    global monsters
    monsters = []
    global monster
    monster = Monster(3*32,17*16,"dinosaur.gif","dinosaur small.gif",27,29)

    global spikemonsters
    spikemonsters = []

    global endpoints
    endpoints = []
    global door
    door = Door((19*32,9*16), "door.gif","level3")
    global stars
    stars = pygame.image.load("stars.gif")
    stars = stars.convert()
    global stars2
    stars2 = pygame.image.load("stars2.gif")
    stars2 = stars2.convert()

level4 = "incomplete"
def level4():
    global tiles
    tiles = []
    global ramps
    ramps = []
    global traps
    traps = []
    global level
    level = [
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000000000",
            "00000000000000040000",
            "00000000000000043333",
            "00000000000000040000",
            "00000000000000040000",
            "00000000000000040040",
            "00000000000034040340",
            "00000000000304040040",
            "00004000000004040040",
            "40003333333334043040",
            "40000000000004040040",
            "43000000000004040040",
            "40000000000004040340",
            "40000000000004040040",
            "33333333330004040040",
            "00000000000004043040",
            "00000000000034040040",
            "00000000000004040040",
            "00000000000004000340",
            "33333333333333000040",
            "00000000000000333330",
            "00000000000000000000",
            "00033330000000000000",
            "00000043000000333000",
            "00000040000000000000",
            "33333333333333333333",
        ]

    x = y = 0
    for row in level:
        for col in row:
            if col == "3":
                Tile((x,y,),"stonefloor2.gif")
            if col == "4":
                Tile((x,y,),"tilebottom2dark.gif")
            if col == "5":
                Ramp((x,y,),"rampright.gif","right")
            if col == "6":
                Ramp((x,y,),"rampleft.gif","left")
                
            x += 32
        y += 16
        x = 0
        
    global player
    player = Player(32,16*21)
    global spike
    spike = Spike((8*32,282),"spikes.gif")
    spike2 = Spike((5*32,282),"spikes.gif")
    global monsters
    monsters = []
    global monster
    monster = Monster(12*32,28*16,"guardLEFT.gif","guardRIGHT.gif",16,31)
    monster = Monster(6*32,13*16,"guardLEFT.gif","guardRIGHT.gif",16,31)

    global spikemonsters
    spikemonsters = []
    
    global endpoints
    endpoints = []
    global door
    door = Door((5*32,27*16), "door.gif","level4")
    global stars
    stars = pygame.image.load("ivywall.gif")
    stars = stars.convert()
    global stars2
    stars2 = pygame.image.load("ivywall.gif")
    stars2 = stars2.convert()

level5 = "incomplete"
def level5():

    global tiles
    tiles = []
    global ramps
    ramps = []
    global traps
    traps = []
    global level
    level = [
            "00040000000000000003",
            "00040000000000000003",
            "03330000000000000003",
            "04000003030303030300",
            "04000444040404040400",
            "04000433333333333330",
            "04000400000000000040",
            "04003400000000000040",
            "04000400000000000040",
            "04300400000000000040",
            "04000400000000000040",
            "04003400000000000040",
            "04000400000000000040",
            "04300400000000000040",
            "04000400000000000040",
            "04003400000000000040",
            "04000400000000000040",
            "04300400000000000040",
            "04000400000000000040",
            "04003400000000000040",
            "04000400333333333340",
            "04300400000000000040",
            "04000430000000000040",
            "04003400000000000040",
            "04000403000000000040",
            "04300400000000000040",
            "04000430030003000040",
            "00003400000004300000",
            "000004sssssss4000000",
            "33333333333333333333",
        ]

    x = y = 0
    for row in level:
        for col in row:
            if col == "3":
                Tile((x,y,),"stonefloor2.gif")
            if col == "4":
                Tile((x,y,),"tilebottom2dark.gif")
            if col == "5":
                Ramp((x,y,),"rampright.gif","right")
            if col == "6":
                Ramp((x,y,),"rampleft.gif","left")
            if col == "s":
                Spike((x,y+8,),"spikes2.gif")
            x += 32
        y += 16
        x = 0
        
    global player
    player = Player(64,0)
    global spike
    
    global monsters
    monsters = []
    global monster

    global spikemonsters
    spikemonsters = []
    spikemonster = Spikemonster((32*3+6,32*3),"y",3)
    spikemonster = Spikemonster((32*6,26),"x",3)
    global endpoints
    endpoints = []
    global door
    door = Door((17*32,18*16), "door.gif","level5")
    global stars
    stars = pygame.image.load("ivywall.gif")
    stars = stars.convert()
    global stars2
    stars2 = pygame.image.load("ivywall.gif")
    stars2 = stars2.convert()

def deletelv1():
    for tile in tiles:
        del tile
    for ramp in ramps:
        del ramp
    del player
    for monster in monsters:
        del monster
    del stars
    del stars2
    for endpoint in endpoints:
        del endpoint
def gameloop():
    while player.gameover == 0:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2,0)
        if key[pygame.K_RIGHT]:
            player.move(2,0)
        if key[pygame.K_UP]:
            if player.releasekey: 
                if player.jump < 20:
                    player.move(0,-5)
                    player.jump += 1        
        if player.rect.bottom < 480:
                player.move(0,2.5)
        if key[pygame.K_UP] == False:
            player.releasekey = True

            
        screen.fill((0,0,0))
        for p in range(0,10):
            for s in range(0,20):
                screen.blit(stars, ((s*32),(p*32)))
        for J in range(0,14):
            for k in range(0,20):
                screen.blit(stars2, ((k*32),(J*32+128)))
        for tile in tiles:
            screen.blit(tile.Image, tile.rect)
        for ramp in ramps:
            screen.blit(ramp.Image, ramp.rect)
        for trap in traps:
            screen.blit(trap.Image, trap.rect)
        screen.blit(door.Image,door.rect)

        screen.blit(player.Image,player.rect)

        
        for monster in monsters:
            monster.move(monster.direction,0)
            if monster.rect.bottom < 480:
                    monster.move(0,2)
        for monster in monsters:
            screen.blit(monster.Image,monster.rect)

        for spikemonster in spikemonsters:
            if spikemonster.direction == "x":
                spikemonster.move(spikemonster.speed,0)
            if spikemonster.direction == "y":
                spikemonster.move(0,spikemonster.speed)
        for spikemonster in spikemonsters:
            screen.blit(spikemonster.Image,spikemonster.rect)
            
        player.check_death()
        door.end_check()
        pygame.display.flip()

world1 = "incomplete"
level1()
gameloop()

if level1 == "complete":
    level2()
    gameloop()
    if level2 == "complete":
        level3()
        gameloop()
        if level3 == "complete":
            world1 = "complete"
if world1 == "complete":
    level4()
    gameloop()
    if level4 == "complete":
        level5()
        gameloop()
            
