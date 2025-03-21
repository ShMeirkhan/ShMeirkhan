import pygame
import os


pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")


songs = ["song1.mp3", "song2.mp3", "song3.mp3"]  
current_song = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 255)

def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, BUTTON_COLOR, (x, y, w, h))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, w, h)


def play_music():
    if not os.path.exists(songs[current_song]):
        print(f"Error: File {songs[current_song]} not found!")
        return
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    play_music()


def prev_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    play_music()


print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir(os.getcwd()))


running = True
while running:
    screen.fill(WHITE)
    
    
    play_button = draw_button("Play", 50, 200, 80, 50)
    stop_button = draw_button("Stop", 150, 200, 80, 50)
    next_button = draw_button("Next", 250, 200, 80, 50)
    prev_button = draw_button("Prev", 350, 200, 80, 50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_music()
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next
                next_song()
            elif event.key == pygame.K_b:  # Previous
                prev_song()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                play_music()
            elif stop_button.collidepoint(event.pos):
                stop_music()
            elif next_button.collidepoint(event.pos):
                next_song()
            elif prev_button.collidepoint(event.pos):
                prev_song()
    
    pygame.display.update()

pygame.quit()