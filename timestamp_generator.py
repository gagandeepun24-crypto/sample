import pygame
import time

# load song
pygame.mixer.init()
pygame.mixer.music.load("paro.mp3")
pygame.mixer.music.play()

print("Song started...")
print("Press ENTER each time the next lyric word should appear.\n")

lyrics = input("Paste the lyrics words separated by space:\n").split()

timestamps = []

start = time.time()

for word in lyrics:
    input(f"Press ENTER for: {word}")
    current_time = time.time() - start
    timestamps.append((current_time, word))

# save to file
with open("lyrics.txt", "w", encoding="utf-8") as f:
    for t, word in timestamps:
        f.write(f"{round(t,2)} {word}\n")

print("\nlyrics.txt created successfully!")