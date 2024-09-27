import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    fps = pygame.time.Clock()
    dt = 0
    
        # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    
    # adding Asteroids!
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    # adding player object to group
    Player.containers = (updatable, drawable)
    
    #adding shots - BANG BANG!
    Shot.containers = (updatable, drawable, shots)
    
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
        ship.update(dt)
        
        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)
       
        for obj in updatable:
            obj.update(dt)
            
        for obj in asteroids:
            if obj.collision_detection(ship):
                print('Game Over!')
                return
            for bullet in shots:
                if bullet.collision_detection(obj):
                    obj.split()
                    bullet.kill()
        
                
        pygame.display.flip()
        
        # limit framerate to 60 fps
        dt = fps.tick(FPS) / 1000

if __name__ =='__main__':
        main()