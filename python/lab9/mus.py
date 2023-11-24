import pygame
import sys
import os
pygame.init()

WINDOW_SIZE = (500,500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("spotify na minimalkah")
pygame.display.set_icon(pygame.image.load("spotik.png"))
BLACK = (0,0,0)
songs_directory = "/Users/symbatbayanbayeva/Documents/python/lab9/songs"
images_directory = "/Users/symbatbayanbayeva/Documents/python/lab9/musplayer"
song_image_mapping = {
    "AHAP.mp3": "renaissance.jpeg",
    "sidewalks.mp3": "starboy.jpeg",
    "ABTD.mp3": "thegame.jpeg"
}

songs = [os.path.join(songs_directory, file) for file in os.listdir(songs_directory) if file.endswith(('.mp3'))]
backgrounds = {os.path.basename(song): os.path.join(images_directory, image) for song, image in song_image_mapping.items()}

pygame.mixer.init()
clock = pygame.time.Clock()
current_song = 0

def play_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()



def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                prev_song()

    current_song_name = os.path.basename(songs[current_song])
    image_path = backgrounds.get(current_song_name, None)

    screen.fill(BLACK)

    if image_path:
        background = pygame.image.load(image_path)
        background = pygame.transform.scale(background, (WINDOW_SIZE))
        screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(60)
