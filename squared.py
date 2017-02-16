import pygame

class Square(object):
    def __init__(self,x,y):
        self.x = y
        self.y = y
    def update(self):
        self.x += 1
        self.y += 1
    def display(self,screen):
        pygame.draw.rect(
            screen,(90, 7, 97),(self.x,self.y,100,100),
        0)
def main():
    width = 500
    height = 500
    screen_color = (16, 107, 28)



    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()


    # Game initialization
    squares = [
    Square(200,200),
    Square(100,50),
    Square(10,300),
    Square(300,300),
    ]
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYUP:
                if event.key == 273:
                    y -= 1
                elif event.key == 274:
                    y += 1
                elif event.key == 276:
                    x -= 1
                elif event.key == 275:
                    x += 1
                    
            if event.type == pygame.QUIT:
                stop_game = True



        # Game logic
        for square in squares:
            square.update()
        # Draw background
        screen.fill(screen_color)

        # Game display
        for square in squares:
            square.display(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
