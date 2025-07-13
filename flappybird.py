import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 30)

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Game Variables
gravity = 0.5
bird_movement = 0
bird = pygame.Rect(100, HEIGHT//2, 30, 30)

pipe_gap = 160
pipe_width = 60
pipe_velocity = 4
pipes = []

score = 0
high_score = 0
game_active = False

# Pipe Timer
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1300)

def create_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top, bottom

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= pipe_velocity
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(SCREEN, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        return False
    return True

def draw_text(text, y, color=WHITE):
    txt = FONT.render(text, True, color)
    rect = txt.get_rect(center=(WIDTH//2, y))
    SCREEN.blit(txt, rect)

def reset_game():
    global bird, bird_movement, pipes, score
    bird.y = HEIGHT // 2
    bird_movement = 0
    pipes.clear()
    score = 0

# Main Loop
while True:
    SCREEN.fill(BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement = -8
                else:
                    game_active = True
                    reset_game()

        if event.type == SPAWNPIPE and game_active:
            pipes.extend(create_pipe())

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird.y += int(bird_movement)
        pygame.draw.rect(SCREEN, WHITE, bird)

        # Pipes
        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        # Collision
        game_active = check_collision(pipes)

        # Score
        for pipe in pipes:
            if pipe.centerx == bird.centerx:
                score += 0.5  # For top and bottom pipe

        draw_text(f"Score: {int(score)}", 50)

    else:
        draw_text("Flappy Bird", 150)
        draw_text("Press SPACE to Start", 250)
        draw_text(f"High Score: {int(high_score)}", 450)

        if score > high_score:
            high_score = score

    pygame.display.update()
    CLOCK.tick(45)
