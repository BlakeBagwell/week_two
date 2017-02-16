import pygame

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    class Square(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def update(self):
            self.x += 1
            self.y += 1

        def display(self, screen):
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (square.x, square.y, 100, 100),
                0)

    squares = [
        Square(200, 200),
        Square(100, 50),
        Square(10, 300),
        Square(300, 300)
    ]

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        for square in squares:
            square.update()

        screen.fill((0, 0, 0))

        # Draw background
        screen.fill(blue_color)

        # Game display

        for square in squares:
            square.display(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
