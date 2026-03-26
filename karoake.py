import pygame
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# color list
colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE
]

# initialize pygame mixer
pygame.mixer.init()

# load and play song
pygame.mixer.music.load("paro.mp3")
pygame.mixer.music.play()

# read lyrics file
lyrics = []

with open("lyrics.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        timestamp = float(parts[0])
        word = " ".join(parts[1:])
        lyrics.append((timestamp, word))

start_time = time.time()

print("\n🎵 Karaoke Started...\n")

for timestamp, word in lyrics:

    # wait until timestamp
    while time.time() - start_time < timestamp:
        pass

    color = random.choice(colors)

    print(color + word + " ", end="", flush=True)

print("\n\nSong Finished 🎶")