import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bouncing Ball with Paddle')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball settings
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

# Paddle settings
paddle_width = 100
paddle_height = 20
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 40  # Positioned near the bottom
paddle_speed = 10

# Score variable
score = 0

# Font for displaying the score
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle with the mouse
    mouse_x, _ = pygame.mouse.get_pos()
    paddle_x = mouse_x - paddle_width // 2

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0:
        ball_speed_y = -ball_speed_y

    # Bounce the ball off the paddle
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y + ball_radius < paddle_y + paddle_height:
        ball_speed_y = -ball_speed_y
        score += 1  # Increase score when the ball hits the paddle

    # Reset ball if it falls below the paddle (lose condition, no score change)
    if ball_y - ball_radius > screen_height:
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_speed_y = -ball_speed_y
        score = 0  # Reset score



    # Fill the screen with white
    screen.fill(WHITE)

    try:
        with open('highscore.txt', 'r') as f:
            high_score = int(f.read())
    except:
        high_score = 0

    if score > high_score:
        high_score = score
        with open('highscore.txt', 'w') as f:
            f.write(str(high_score))

    # Display high score
    high_score_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
    screen.blit(high_score_text, (screen_width - 200, 10))


    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw the paddle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Display the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    clock.tick(60)
