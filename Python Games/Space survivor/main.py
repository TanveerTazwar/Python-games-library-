import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star fighter")

# Here we are bringing in the background image
BG = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))

#Size of the player character
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

#Speed of the player character's movement speed
PLAYER_VEL = 5
#Speed of the star's movement speed
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

#Size of the stars
STAR_WIDTH = 10
STAR_HEIGHT = 20

#This function basically is drawing up shapes and Background images as outputs for us to see
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"time: {round(elapsed_time)}s", 1, "blue")

    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN, "blue", player)

    for star in stars:
        pygame.draw.rect(WIN, "crimson", star)

    pygame.display.update()

#The main script for our game
def main():
    run = True

    clock = pygame.time.Clock()

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("You lost! Better luck next time ;)", 5, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        draw(player, elapsed_time, stars)
    pygame.quit()
if __name__ == "__main__":
    main()