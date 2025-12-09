import sys
import random
import pygame

black = pygame.Color(0, 0, 0)
gray = pygame.Color(128, 128, 128)
white = pygame.Color(255, 255, 255)

pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snow Game')

FPS = 60
clock = pygame.time.Clock()

falling_flakes = []
landed_flakes = []

score = 0
font = pygame.font.SysFont(None, 36)

bg_image = pygame.image.load('images/bg.jpg')
bg_image = pygame.transform.scale(bg_image, (width, height))

flake_width = flake_height = 50
flake_image = pygame.image.load('images/flake.png')
flake_image = pygame.transform.scale(flake_image, (flake_width, flake_height))

base_falling_speed = 1.4
speed_increment = 0.3
score_step_for_speedup = 10
current_falling_speed = base_falling_speed

def create_snowflake():
    x_flake_coord = random.randint(0, width - flake_width)
    flake_rect = pygame.Rect(x_flake_coord, -flake_height, flake_width, flake_height)
    falling_flakes.append(flake_rect)

def game_over_screen(score):
    screen.fill(black)
    font_large = pygame.font.SysFont(None, 75)
    game_over_text = font_large.render("GAME OVER", True, gray)
    game_over_rect = game_over_text.get_rect(center = (width // 2, height // 2 - 30))
    screen.blit(game_over_text, game_over_rect)

    font_small = pygame.font.SysFont(None, 50)
    score_text = font_small.render(f'Your score: {score}', True, gray)
    score_rect = score_text.get_rect(center = (width // 2, height // 2 + 30))
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print('__GAME OVER__')
                sys.exit()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_screen(score)   
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                game_over_screen(score)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos_x, mouse_pos_y = event.pos
            for flake in falling_flakes:
                if flake.collidepoint(mouse_pos_x, mouse_pos_y):
                    falling_flakes.remove(flake)
                    score += 1
                    print(f'Score: {score}')

    current_falling_speed = base_falling_speed + (score // score_step_for_speedup) * speed_increment

    if random.random() < 0.01:
        create_snowflake()

    for flake in falling_flakes:
        flake.y += current_falling_speed
        hit_landed_flake = None
        for lf in landed_flakes:
            if flake.move(0, current_falling_speed).colliderect(lf):
                hit_landed_flake = lf
                break

        if hit_landed_flake:
            flake.bottom = hit_landed_flake.top
            landed_flakes.append(flake)
            falling_flakes.remove(flake)
            continue
        
        if flake.bottom >= height:
            flake.bottom = height
            landed_flakes.append(flake)
            falling_flakes.remove(flake)
            continue

    for lf in landed_flakes:
        if lf.top <= 0:
            game_over_screen(score)
        
    screen.blit(bg_image, (0, 0))
    for f in falling_flakes:
        screen.blit(flake_image, f.topleft)

    for lf in landed_flakes:
        pygame.draw.rect(screen, white, lf)

    score_text = font.render(f'Score: {score}', True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
