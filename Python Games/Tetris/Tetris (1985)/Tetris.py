# I'll leave behind notes simply for my understanding
import pygame, sys  # We are importing the module we will be using to make the game
from game import Game
from colors import Colors

pygame.init()  # This initializes the game
pygame.font.init()

title_font = pygame.font.Font("Minecraft.ttf", 20)
title_font2 = pygame.font.Font("Minecraft.ttf", 13)
score_surface = title_font.render("Score", True, Colors.RusGreen)
next_surface = title_font.render("Next", True, Colors.RusGreen)
game_over_surface = title_font.render("GAME OVER", True, Colors.red)
history = title_font2.render("Designed by Alexey L. Pajitnov", True, Colors.RusGreen)
release = title_font2.render("1985", True, Colors.RusGreen)

score_rect = pygame.Rect(430, 55, 200, 60)
next_rect = pygame.Rect(500, 230, 200, 180)


# Now we need to create a screen or a display which is like a blank canvas. All the objects we draw
# will appear here. the display surface has a width and also a height. This is a must for all games

screen = pygame.display.set_mode((650, 910))  # This line of code creates a display surface.
# Takes tuple argument (width, height)
# In computer graphics, the coordinate system is used. Every point has a (x, y) value. But the origin in top left corner

# Now we give a caption to the game window
pygame.display.set_caption("TTP's Python Tetris")

# Clock object
clock = pygame.time.Clock()  # We need this clock object to control the frame rate of the game

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop, game-loop handles mainly three things
# (i) Event handling: checks for the changes and inputs from users
# (ii) Updating coordinates: Updates the coordinates of game objects
# (iii) Drawing objects: draws the objects in the new coordinates
while True:  # Our while loop will keep on running from the start till the end of the closing of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    # Drawing
    # colors in pygame are represented as tuple of three values (red, green, blue). Value for components
    # range from 0-255. For example red is (255, 0, 0)
    score_value_surface = title_font.render(str(game.score), True, Colors.RusGreen)
    screen.fill(Colors.black)  # Fill methods just fills the display surface of our canvas
    game.draw(screen)
    screen.blit(score_surface, (490, 20, 50, 50))
    screen.blit(next_surface, (500, 200, 50, 50))
    screen.blit(history, (450, 870, 50, 50))
    screen.blit(release, (450, 890, 50, 50))


    if game.game_over == True:
        screen.blit(game_over_surface, (450, 600, 50, 50))
    # pygame.draw.rect(screen, Colors.green, score_rect, 0, 10)
    # pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                  centery = score_rect.centery))


    pygame.display.update()
    clock.tick(60)  # Frame rate
