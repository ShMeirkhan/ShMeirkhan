
import psycopg2
import pygame
import sys
import random
import time

# Базамен байланыс
conn = psycopg2.connect(
    dbname='lab10',
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Таңдау: жаңа ойыншы ма, ескі ойыншы ма
mode = input("Жаңа ойыншы ма, әлде ескі ойыншы ма? (жаңа/ескі): ").strip().lower()
username = input("Атыңды енгіз: ").strip()

user_id = None
score = 0
level = 1

# Қолданушыны тексеру немесе жасау
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if mode == "жаңа":
    if not user:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    else:
        user_id = user[0]
    score = 0
    level = 1

elif mode == "ескі":
    if user:
        user_id = user[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
        row = cur.fetchone()
        score = row[0] if row else 0
        level = row[1] if row else 1
    else:
        print("Бұл қолданушы табылмады.")
        sys.exit()
else:
    print("Тек 'жаңа' немесе 'ескі' деп жазу керек!")
    sys.exit()
print("Ойын 7 секундтан кейін басталады...")
time.sleep(7)

# Pygame параметрлері
pygame.init()
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
speed = 10 + level * 2

def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake:
            return (x, y)

def game():
    global score, level, speed
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    food = generate_food(snake)
    running = True

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
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake):
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            if score % 3 == 0:
                level += 1
                speed += 2
            food = generate_food(snake)
        else:
            snake.pop()

        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        score_text = font.render(f"{username} | Ұпай: {score} | Деңгей: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    print("Ойын аяқталды. Ұпай базаға сақталды.")

game()
cur.close()
conn.close()
