import pygame
import random

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def generate_food(snake):
    while True:
        x, y = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake:
            weight = random.randint(1, 5)
            timer = random.randint(20, 40)
            return x, y, weight, timer

def game():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    food_x, food_y, food_weight, food_timer = generate_food(snake)
    food_time_remaining = food_timer
    running = True
    score = 0
    level = 1
    speed = 10

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            running = False
        
        if new_head in snake:
            running = False
        
        snake.insert(0, new_head)
        
        if new_head == (food_x, food_y):
            score += food_weight
            if score % 3 == 0:
                level += 1
                speed += 2
            food_x, food_y, food_weight, food_timer = generate_food(snake) 
            food_time_remaining = food_timer
        else:
            snake.pop()

        if food_time_remaining > 0:
            food_time_remaining -= 1
        else:
            food_x, food_y, food_weight, food_timer = generate_food(snake)
            food_time_remaining = food_timer

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, RED, (food_x, food_y, GRID_SIZE, GRID_SIZE))
        weight_text = font.render(str(food_weight), True, WHITE)
        screen.blit(weight_text, (food_x + GRID_SIZE // 4, food_y + GRID_SIZE // 4))

        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()

if __name__ == "__main__":
    game()