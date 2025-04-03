import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Program")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)
drawing = False
last_pos = None
brush_size = 5
color = BLACK

tool = 'brush'  # Options: 'brush', 'rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'diamond'
start_pos = None

font = pygame.font.SysFont(None, 24)

# Рисуем пользовательский интерфейс (кнопки для выбора инструментов)
def draw_ui():
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 800, 40))
    tools = ['Brush', 'Rect', 'Circle', 'Eraser', 'Square', 'Right Tri', 'Equilateral Tri', 'Diamond', 'Color']
    for i, t in enumerate(tools):
        text = font.render(t, True, BLACK)
        pygame.draw.rect(screen, (150, 150, 150), (10 + i * 90, 5, 80, 30))
        screen.blit(text, (20 + i * 90, 10))

# Получаем инструмент, на который нажали
def get_tool_click(pos):
    if pos[1] > 40:
        return None
    if 10 <= pos[0] < 90:
        return 'brush'
    elif 100 <= pos[0] < 180:
        return 'rectangle'
    elif 190 <= pos[0] < 270:
        return 'circle'
    elif 280 <= pos[0] < 360:
        return 'eraser'
    elif 370 <= pos[0] < 450:
        return 'square'
    elif 460 <= pos[0] < 540:
        return 'right_triangle'
    elif 550 <= pos[0] < 640:
        return 'equilateral_triangle'
    elif 650 <= pos[0] < 740:
        return 'diamond'
    elif 750 <= pos[0] < 830:
        return 'color'
    return None

# Функции для рисования различных форм
def draw_square(start, end, surface, color):
    side_length = abs(end[0] - start[0])
    pygame.draw.rect(surface, color, (start[0], start[1], side_length, side_length), width=2)

def draw_right_triangle(start, end, surface, color):
    pygame.draw.polygon(surface, color, [start, (end[0], start[1]), end], width=2)

def draw_equilateral_triangle(start, end, surface, color):
    side_length = int(((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5)
    height = int(side_length * math.sqrt(3) / 2)
    top = (start[0] + end[0]) // 2, start[1] - height
    pygame.draw.polygon(surface, color, [start, end, top], width=2)

def draw_diamond(start, end, surface, color):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    points = [
        (start[0] + width // 2, start[1]),
        (start[0] + width, start[1] + height // 2),
        (start[0] + width // 2, start[1] + height),
        (start[0], start[1] + height // 2)
    ]
    pygame.draw.polygon(surface, color, points, width=2)

# Основной цикл игры
running = True
while running:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tool_clicked = get_tool_click(event.pos)
            if tool_clicked:
                if tool_clicked == 'color':
                    color = pygame.color.THECOLORS[input("Enter color name (e.g., red, blue): ")] or BLACK
                else:
                    tool = tool_clicked
            else:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos
                if tool == 'brush':
                    pygame.draw.circle(screen, color, event.pos, brush_size)
                elif tool == 'eraser':
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and tool in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'diamond']:
                end_pos = event.pos
                if tool == 'rectangle':
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                       abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                    pygame.draw.rect(screen, color, rect, width=2)
                elif tool == 'circle':
                    radius = int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, width=2)
                elif tool == 'square':
                    draw_square(start_pos, end_pos, screen, color)
                elif tool == 'right_triangle':
                    draw_right_triangle(start_pos, end_pos, screen, color)
                elif tool == 'equilateral_triangle':
                    draw_equilateral_triangle(start_pos, end_pos, screen, color)
                elif tool == 'diamond':
                    draw_diamond(start_pos, end_pos, screen, color)
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == 'brush':
                pygame.draw.line(screen, color, last_pos, event.pos, brush_size * 2)
            elif tool == 'eraser':
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 2)
            last_pos = event.pos

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
