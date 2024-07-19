# PyGame documentation: https://www.pygame.org/docs/

import sys
import pygame

pygame.init() # Initialize PyGame
pygame.joystick.init() # Initialize the joystick
pygame.mixer.init(channels=1) # Initialize the mixer (sound) with one channel
pygame.mouse.set_visible(False) # Hide the mouse cursor

DISPLAY_WIDTH = 1920 # The arcade cabinet monitor is 1920 x 1080
DISPLAY_HEIGHT = 1080 # The arcade cabinet monitor is 1920 x 1080

FPS = 60 # Frames per second
timer = pygame.time.Clock() # The clock for the game

sound_channel = pygame.mixer.Channel(0) # Create the mixer channel

# The buttons on the control panels have different ids depending on os
# so using a class so it doesn't have to be hardcoded everywhere.
class Buttons:
    ADMIN_LEFT = 8
    ADMIN_RIGHT = 9
    PLAYER_LEFT = 3
    PLAYER_RIGHT = 4

    if sys.platform.startswith('darwin'): # MacOS seems to have different button numbers
        PLAYER_LEFT = 2

def play_sound():
    
    # Play sound - play(loops=0, maxtime=0, fade_ms=0) loops is the number of times to play the sound after the first time
    sound_start = pygame.mixer.Sound('assets/sounds/game_start.mp3')
    sound_channel.play(sound_start, loops=0)
    pygame.time.delay(5000) # Be careful using delays within the while loop because it can mess up your timing.

    # Play sound indefinitely
    sound_chomp = pygame.mixer.Sound('assets/sounds/chomp.mp3')
    sound_channel.play(sound_chomp, loops=-1)
    pygame.time.delay(10000)

    # Stop the sound (mostly used if there is a loops=-1)
    sound_channel.stop()
    pygame.time.delay(5000)

    # Play background sound - play(loops=0, start=0.0, fade_ms=0)
    pygame.mixer.music.load('assets/sounds/background.mp3')
    pygame.mixer.music.play(-1)
    pygame.time.delay(5000)

    # Pause the background sound - When playing a sound on the channel, use the pause method so that the background sound does not play at the same time.
    pygame.mixer.music.pause()
    pygame.time.delay(3000)
    
    # Resume the background sound - After a sound on the channel is done playing, resume the background sound.
    pygame.mixer.music.unpause()

    # Play a sound one time while the background sound plays
    pygame.mixer.Sound.play(sound_start)

    # See https://www.pygame.org/docs/ref/mixer.html and https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Channel for more details

def draw_shapes(screen):
    # Line - line(surface, color, (start_x_pos, start_y_pos), (end_x_pos, end_y_pos), line_thickness)
    pygame.draw.line(screen, 'blue', (0, 20), (1920, 20), 3)

    # Rectangle - rect(surface, color, [top_left_x_pos, top_left_y_pos, width, height], line_thickness)
    pygame.draw.rect(screen, 'white', [50, 50, 500, 50], 0)

    # Circle - circle(surface, color, (center_x_pos, center_y_pos), radius, line_thickness)
    pygame.draw.circle(screen, 'purple', (500, 500), 300)

    # See https://www.pygame.org/docs/ref/draw.html for more draw options

def draw_images(screen):
    devnet_img = pygame.image.load('assets/images/Cisco_DevNet_Logo.png')
    screen.blit(devnet_img, (10, 150))
    
    # Scale the image to the size of 100 px x 131 px
    devnet_scaled_img = pygame.transform.scale(pygame.image.load('assets/images/Cisco_DevNet_Logo.png'), (100, 131))
    screen.blit(devnet_scaled_img, (1000, 150))

def write_text(screen):
    # Set up the font - Font(file_path, size)
    font_filepath = 'assets/fonts/CiscoSansTTRegular.ttf'
    font = pygame.font.Font(font_filepath, 30)

    # Only single line text is supported - render(text, antialias, color) - color can be a string from the standard list or (R, G, B)
    text = font.render(f'This is my text.', True, 'white')
    screen.blit(text, (300, 100))

    text_line1 = font.render(f'This is the first line.', True, (247, 150, 34))
    text_line2 = font.render(f'This is the second line.', True, (84, 100, 255))
    line1_y_coord = 300
    screen.blit(text_line1, (300, line1_y_coord))
    screen.blit(text_line2, (300, line1_y_coord + text_line1.get_height()))

def run_game(screen):
    joystick = None

    play_sound()

    # Ever iteration of the while loop is building a SINGLE frame to display
    run = True
    while run:
        timer.tick(FPS) # Keeps the game running at the right frame refresh rate.
        screen.fill('black') # Make the background black.

        # draw_shapes(screen)
        # draw_images(screen)
        write_text(screen)

        pygame.display.flip() # Displays everything that was added/configured to the screen object.

        # Handle keyboard and joystick for games like pacman where the character
        # continues to move in that direction until the direction is changed
        # START ----------------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.JOYBUTTONDOWN and joystick and joystick.get_button(Buttons.ADMIN_LEFT) and joystick.get_button(Buttons.ADMIN_RIGHT)): # Pressed CMD + Q and CTRL + Q on the keyboard or both the admin left and right on the control panel
                pygame.mixer.music.stop() # Stop the background music
                sound_channel.stop() # Stop the music on the channel
                run = False # Make sure to exit the loop
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT) or \
                (event.type == pygame.JOYAXISMOTION and joystick and round(joystick.get_axis(0)) == 1): # Pressed the right arrow on the keyboard or moved the joystick to the right
                print("Right")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT) or \
                    (event.type == pygame.JOYAXISMOTION and joystick and round(joystick.get_axis(0)) == -1): # Pressed the left arrow on the keyboard or moved the joystick to the left
                print("Left")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or \
                    (event.type == pygame.JOYAXISMOTION and joystick and round(joystick.get_axis(1)) == -1): # Pressed the up arrow on the keyboard or moved the joystick to the up
                print("Up")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or \
                    (event.type == pygame.JOYAXISMOTION and joystick and round(joystick.get_axis(1)) == 1): # Pressed the down arrow on the keyboard or moved the joystick to the down
                print("Down")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                (event.type == pygame.JOYBUTTONDOWN and joystick and joystick.get_button(Buttons.PLAYER_LEFT)): # Pressed space on the keyboard or the player left button on the control panel
                print("Space or player left button")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_x) or \
                (event.type == pygame.JOYBUTTONDOWN and joystick and joystick.get_button(Buttons.PLAYER_RIGHT)): # Pressed x on the keyboard or the player right button on the control panel
                print("x or player right button")
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index) # Assign the joystick variable to the detected joystick
                joystick.init() # Initialize the joystick
            elif event.type == pygame.JOYDEVICEREMOVED:
                joystick = None # Clear the joystick variable since the joystick was removed
        # END ----------------------------------------------------------------------
        
        # Handle keyboard and joystick for games like tetris where the piece
        # should not move unless the player is actively pushing on the button/joystick.
        # Keyboard direction presses have one event per press while joystick will send
        # multiple events (inconsistent) when the joystick is moved a certain direction.
        # START ----------------------------------------------------------------------
        # Handle the keyboard events and the control panel button events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.JOYBUTTONDOWN and joystick and joystick.get_button(Buttons.ADMIN_LEFT) and joystick.get_button(Buttons.ADMIN_RIGHT)): # Pressed CMD + Q and CTRL + Q on the keyboard or both the admin left and right on the control panel
                pygame.mixer.music.stop() # Stop the background music
                sound_channel.stop() # Stop the music on the channel
                run = False # Make sure to exit the loop
            elif event.type == pygame.KEYDOWN: # Handle when there is a key press on the keyboard
                if event.key == pygame.K_LEFT: # Pressed the left arrow on the keyboard
                    print("Left on the keyboard")
                elif event.key == pygame.K_RIGHT: # Pressed the right arrow on the keyboard
                    print("Right on the keyboard")
                elif event.key == pygame.K_DOWN: # Pressed the down arrow on the keyboard
                    print("Down on the keyboard")
                elif event.key == pygame.K_UP: # Pressed the up arrow on the keyboard
                    print("Up on the keyboard")
            elif (event.type == pygame.JOYBUTTONDOWN and joystick and (joystick.get_button(Buttons.PLAYER_LEFT) or joystick.get_button(Buttons.PLAYER_RIGHT))): # Pressed the player left or right button on the control panel
                print("Player left or right button on the control panel")
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index) # Assign the joystick variable to the detected joystick
                joystick.init() # Initialize the joystick
            elif event.type == pygame.JOYDEVICEREMOVED:
                joystick = None # Clear the joystick variable since the joystick was removed

        # Handle the joystick events
        # Note, you will get multiple events of the same type for one joystick move.
        # It is not consistent in how many events per move.
        # Code needs to handle it properly.
        speed = 1
        if joystick:
            if joystick.get_button(Buttons.ADMIN_LEFT) and joystick.get_button(Buttons.ADMIN_RIGHT):
                run = False
            elif round(joystick.get_axis(0)) == -1: # Moved joystick left
                print("Left on the joystick")
            elif round(joystick.get_axis(0)) == 1: # Moved joystick right
                print("Right on the joystick")
            elif round(joystick.get_axis(1)) == -1: # Moved joystick up
                print("Up on the joystick")
            elif round(joystick.get_axis(1)) == 1: # Moved joystick down
                print("Down on the joystick")
            elif round(joystick.get_axis(0)) == 0 and round(joystick.get_axis(1)) == 0: # Joystick back to neutral/center
                print("Center/no direction on the joystick")
        # END ----------------------------------------------------------------------


if __name__ == '__main__':
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) # Not fullscreen - Useful during development.
    # flags = pygame.FULLSCREEN
    # screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), flags, vsync=1) # Fullscreen - Need to code in CMD + QUIT to exit.

    run_game(screen)

    pygame.joystick.quit() # Make sure to quit the joystick
    pygame.quit() # Make sure to quit PyGame