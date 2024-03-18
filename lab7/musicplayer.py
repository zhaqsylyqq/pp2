import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("musicPlayer")
icon = pygame.image.load("music_icon.png")
pygame.display.set_icon(icon)

path = [
    "mus1.mp3",
    "mus2.mp3",
    "mus3.mp3",
    "mus4.mp3",
    "mus5.mp3",
]

current_index = 0
pygame.mixer.music.load(path[current_index])


def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def play_next():
    global current_index
    current_index = (current_index + 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


def play_previous():
    global current_index
    current_index = (current_index - 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


sqaure = pygame.Surface((120, 100))
sqaure.fill("Black")

sqaure0 = pygame.Surface((120, 100))
sqaure0.fill("Black")

running = True
while running:
    
    pygame.draw.circle(screen, "black", (250, 150), 50)
    screen.blit(sqaure, (80, 100))
    screen.blit(sqaure, (300, 100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pause_music()
                else:
                    unpause_music()
            elif event.key == pygame.K_RIGHT:
                play_next()
            elif event.key == pygame.K_LEFT:
                play_previous()

    screen.fill((255, 255, 255))
    pygame.display.flip()
    

pygame.quit()