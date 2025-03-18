import pygame

pygame.init() # Initialize pygame modules

# Display/Surface Settings
DISPLAY_WIDTH = 1920 # Display is 1920 x 1080
DISPLAY_HEIGHT = 1080 # Display is 1920 x 1080

FPS = 60 # Frames per second (fps)
clock = pygame.time.Clock() # The clock helps track time

def run_game(surface):
    # The x and y position of the smiley face image
    smiley_face_x_pos = DISPLAY_WIDTH // 2
    smiley_face_y_pos = DISPLAY_HEIGHT // 2

    # Every iteration of the while loop is building a SINGLE frame to display
    run = True
    while run: # This loop runs forever until the run is set to False to exit
        # Keeps the game running at the right frames per second
        clock.tick(FPS)

        # Set the background of the surface to white (RGB)
        surface.fill(color=(255, 255, 255))

        # Draw lines and shapes to the surface
        # pygame.draw.line(surface, color, (start_pos_x, start_pos_y), (end_pos_x, end_pos_y), width)
        pygame.draw.line(surface, 'blue', (0, 100), (800, 100), 3)
        # pygame.draw.rect(surface, color, (left_x, top_y, rect_width, rect_height), width)
        pygame.draw.rect(surface, (173, 216, 230), (10, 15, 500, 20), 0)
        # pygame.draw.circle(surface, color, (center_x, center_y), radius)
        pygame.draw.circle(surface, 'green', (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2), 50)

        # Draw the image to the surface
        surface.blit(smiley_face_img, (smiley_face_x_pos, smiley_face_y_pos))

        # Update the display surface to the screen
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Ctrl + Q / Cmd + Q (MacOS)
                run = False
            elif event.type == pygame.KEYDOWN: # Pressed a key on the keyboard
                if event.key == pygame.K_UP: # Pressed up on the keyboard
                    smiley_face_y_pos -= 1
                elif event.key == pygame.K_DOWN: # Pressed down on the keyboard
                    smiley_face_y_pos += 1
                elif event.key == pygame.K_LEFT: # Pressed left on the keyboard
                    smiley_face_x_pos -= 1
                elif event.key == pygame.K_RIGHT: # Pressed right on the keyboard
                    smiley_face_x_pos += 1

if __name__ == '__main__':
    # Configure the surface with a specific width and height
    flags = pygame.FULLSCREEN
    surface = pygame.display.set_mode(size=(DISPLAY_WIDTH, DISPLAY_HEIGHT), flags=flags)

    # Configure how many events are sent when a key is held down on the keyboard
    pygame.key.set_repeat(30, 10)

    # Load the image to a surface
    smiley_face_img = pygame.image.load('assets/images/smiley_face.png')

    # The logic for the game
    run_game(surface)