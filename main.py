from game import *

mainloop()
if player.state == "gameover":
    while player.state == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        Intro()