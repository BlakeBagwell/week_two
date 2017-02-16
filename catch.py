import pygame
import math
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Character(object):
    def __init__(self, x, y,speed_x,speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = 16


    def wrap(self, width, height):
        if self.x > width + 15:
            self.x = -15
        if self.x < -15:
            self.x = width + 15
        if self.y < -16:
            self.y = height -16
        if self.y > height +16:
            self.y = -16

    def direction(self):
        angle = random.randint(0, 7)
        #north
        if angle == 0:
            self.speed_y = -5
            self.speed_x = 0
        #east
        elif angle == 1:
            self.speed_x = 5
            self.speed_y = 0
        #south
        elif angle == 2:
            self.speed_y = 5
            self.speed_x = 0
        #west
        elif angle == 3:
            self.speed_x = -5
            self.speed_y = 0
        #northeast
        elif angle == 4:
            self.speed_x = 5
            self.speed_y = -5
        #northwest
        elif angle == 5:
            self.speed_x = -5
            self.speed_y = -5
        #southeast
        elif angle == 6:
            self.speed_x = 5
            self.speed_y = 5
        #southwest
        elif angle == 7:
            self.speed_x = -5
            self.speed_y = -5

class Monster(Character):
    def __init__(self):
        self.x = 50
        self.y = 50
        self.speed_x = 5
        self.speed_y = 5

class Hero(Character):
    def __init__(self):
        self.x = 256
        self.y = 240
        self.speed_x = 0
        self.speed_y = 0


hero = Hero()
monster = Monster()

def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()



    # Game initialization
    count_down = 120

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down

                if event.key == KEY_DOWN:
                    hero.speed_y = 3
                elif event.key == KEY_UP:
                    hero.speed_y = -3
                elif event.key == KEY_LEFT:
                    hero.speed_x = -3
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 3

            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released

                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0


            if event.type == pygame.QUIT:
                stop_game = True




        # Game logic
        count_down -= 1
        if count_down == 0:
            monster.direction()
            count_down = 120


        monster.x += monster.speed_x
        monster.y += monster.speed_y


        hero.x += hero.speed_x
        hero.y += hero.speed_y

        # Draw background


        # Game display

        background_image = pygame.image.load('/Users/blakebagwell/digital_crafts/week_two/pygame-project/images/background.png').convert_alpha()
        hero_image = pygame.image.load ('/Users/blakebagwell/digital_crafts/week_two/pygame-project/images/hero.png').convert_alpha()
        monster_image = pygame.image.load ('/Users/blakebagwell/digital_crafts/week_two/pygame-project/images/monster.png').convert_alpha()
        screen.blit(background_image, (0, 0))
        screen.blit(monster_image, (monster.x, monster.y))
        # monster.move_right()
        # monster.move_left()
        # monster.move_down()
        monster.wrap(width, height)
        hero.wrap(width, height)
        screen.blit(hero_image, (hero.x,hero.y))
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()
