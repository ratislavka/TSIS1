import pygame

pygame.mixer.init()
pressed = pygame.key.get_pressed()
songs = ['', '', '']
song_index = 0

def PlaySong():
    pygame.mixer.music.play()

def StopSong():
    pygame.mixer.music.stop()

def NextSong():
    global song_index
    song_index += 1
    if song_index >= len(songs):
        song_index = 0
    pygame.mixer.music.load(songs[song_index])
    pygame.mixer.music.play()

def PreviousSong():
    global song_index
    song_index -= 1
    if song_index < 0:
        song_index = len(songs) - 1
    pygame.mixer.music.load(songs[song_index])
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_p]:
        PlaySong()
    if pressed[pygame.K_s]:
        StopSong()
    if pressed[pygame.K_RIGHT]:
        NextSong()
    if pressed[pygame.K_LEFT]:
        PreviousSong()

    pygame.time.wait(60)

pygame.quit()