import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Program")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [BLACK, RED, GREEN, BLUE] 
screen.fill(WHITE)

drawing = False
last_pos = None
brush_size = 5
color = BLACK

tool = 'brush'
start_pos = None

font = pygame.font.SysFont(None, 24)

def draw_ui():
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 800, 40))
    tools = ['Brush', 'Rect', 'Circle', 'Eraser', 'Color']
    for i, t in enumerate(tools):
        text = font.render(t, True, BLACK)
        pygame.draw.rect(screen, (150, 150, 150), (10 + i * 100, 5, 80, 30))
        screen.blit(text, (20 + i * 100, 10))

    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i * 50, 45, 40, 40))

def get_tool_click(pos):
    if pos[1] > 40: 
        return None
    if 10 <= pos[0] < 90:
        return 'brush'
    elif 110 <= pos[0] < 190:
        return 'rectangle'
    elif 210 <= pos[0] < 290:
        return 'circle'
    elif 310 <= pos[0] < 390:
        return 'eraser'
    elif 410 <= pos[0] < 490:
        return 'color'
    return None

def get_color_click(pos):
    if 45 <= pos[1] < 85:
        index = (pos[0] - 10) // 50 
        if 0 <= index < len(colors):
            return colors[index]
    return None

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
                    selected_color = get_color_click(event.pos)
                    if selected_color:
                        color = selected_color
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
            if drawing and tool in ['rectangle', 'circle']:
                end_pos = event.pos
                if tool == 'rectangle':
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                       min(start_pos[1], end_pos[1]),
                                       abs(start_pos[0] - end_pos[0]),
                                       abs(start_pos[1] - end_pos[1]))
                    pygame.draw.rect(screen, color, rect, width=2)
                elif tool == 'circle':
                    radius = int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, width=2)
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
