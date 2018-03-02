import sys, pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # main loop
    while True:
        # watch for input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw screen on each pass through the loop
        screen.fill(bg_color)

        # make most recently drawn screen visible
        pygame.display.flip()

run_game()
