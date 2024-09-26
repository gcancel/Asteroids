import pygame, sys
from constants import *
from player import Player

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    fps = pygame.time.Clock()
    dt = 0
    
    player_pos_x = SCREEN_WIDTH / 2
    player_pos_y = SCREEN_HEIGHT /2
    ship = Player(player_pos_x, player_pos_y)
    
    
    while True:
        # enable quit for game 
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit();sys.exit()
                return
            
        # draw ship on screen        
        screen.fill('black')
        ship.draw(screen)
        pygame.display.flip()
        
        # limit framerate to 60 fps
        dt = fps.tick(FPS) / 1000

if __name__ =='__main__':
        main()