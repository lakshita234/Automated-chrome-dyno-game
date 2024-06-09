import pyautogui
import pyscreeze
import time
import keyboard

while True:
    im=pyautogui.screenshot()
    screen=im.getpixel((310,469))

    x1=im.getpixel((214,189))
    x2=im.getpixel((1026,469))
    x3=im.getpixel((723,489))
    x4=im.getpixel((610,521))

    y1=im.getpixel((609,441))
    y2=im.getpixel((952,432))
    y3=im.getpixel((745,470))
    y4=im.getpixel((656,469))

    if screen[0]==255:
        if x1[0]!=255 or x2[0]!=255 or x3[0]!=255 or x4[0]!=255 or y1[0]!=255 or y2[0]!=255 or y3[0]!=255 or y4[0]!=255:
            pyautogui.press('space')
            time.sleep(0.0001)

        if screen[0]==255:
            if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
                pyautogui.press('space')
                time.sleep(0.0001)

    if keyboard.is_pressed('s'):
        break

    else:
        pass













# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import pygame
# import random
# import threading
#
# # Initialize pygame
# pygame.init()
#
# # Screen dimensions
# WIDTH, HEIGHT = 800, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Dinosaur Game')
#
# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
#
# # Dinosaur
# dino_width, dino_height = 40, 40
# dino_x = 50
# dino_y = HEIGHT - dino_height
# dino_y_velocity = 0
# gravity = 1
#
# # Obstacles
# obstacle_width = 20
# obstacle_height = 40
# obstacle_x = WIDTH
# obstacle_y = HEIGHT - obstacle_height
# obstacle_speed = 10
#
# # Game variables
# clock = pygame.time.Clock()
# running = True
# jumping = False
# score = 0
#
# # Function to make the dinosaur jump
# def auto_jump():
#     global jumping, dino_y_velocity
#     while running:
#         if obstacle_x - dino_x < 100 and not jumping:
#             jumping = True
#             dino_y_velocity = -20
#         pygame.time.delay(10)
#
# # Start the auto jump thread
# threading.Thread(target=auto_jump).start()
#
# # Main game loop
# while running:
#     screen.fill(WHITE)
#
#     # Check for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Dinosaur jump logic
#     if jumping:
#         dino_y += dino_y_velocity
#         dino_y_velocity += gravity
#
#     if dino_y >= HEIGHT - dino_height:
#         dino_y = HEIGHT - dino_height
#         jumping = False
#
#     # Move obstacle
#     obstacle_x -= obstacle_speed
#     if obstacle_x < 0:
#         obstacle_x = WIDTH
#         score += 1
#
#     # Check for collision
#     if dino_x < obstacle_x < dino_x + dino_width and dino_y + dino_height > obstacle_y:
#         running = False
#
#     # Draw dinosaur
#     pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))
#
#     # Draw obstacle
#     pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
#
#     # Update display
#     pygame.display.flip()
#
#     # Set frame rate
#     clock.tick(30)
#
# pygame.quit()