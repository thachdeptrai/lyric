import pygame  # type: ignore
import time
import os
import random

def read_lyrics(file_path):
    lyrics = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and line.startswith('['): 
                timestamp, text = line.split(']', 1)
                text = text.strip() 
                minutes, seconds = map(float, timestamp[1:].split(':')) 
                time_in_seconds = minutes * 60 + seconds 
                lyrics.append((time_in_seconds, text))  
    return lyrics


def type_effect(text, color, delay=0.02):
    for char in text:
        print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}", end="", flush=True)
        time.sleep(delay)
    print("\033[0m")

def fade_in_effect(text, color, duration=2):
    total_chars = len(text)
    for i in range(1, total_chars + 1):
        part_text = text[:i]
        intensity = int(255 * (i / total_chars))
        print(f"\033[38;2;{color[0]};{color[1]};{color[2]};{intensity}m{part_text}\033[0m", end="", flush=True)
        time.sleep(duration / total_chars)
    print("\033[0m") 

def play_music_with_lyrics(music_path, lyrics):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    
    start_time = time.time()
    previous_text = ""  
    last_display_time = 0  
    
    for timestamp, text in lyrics:
        while time.time() - start_time < timestamp:
            time.sleep(0.01)  

        os.system('cls' if os.name == 'nt' else 'clear')  
 
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if len(text.split()) <= 7:
            print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[0m")
            previous_text = text 
        else:
            if previous_text:
                print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{previous_text}\033[0m")
                previous_text = ""  

            type_effect(text, color) 
            last_display_time = time.time()

    while pygame.mixer.music.get_busy():
        time.sleep(0.01)

if __name__ == "__main__":
    music_path = "mp3/tuchoihieu.mp3" 
    lyrics_path = "lrc/tuchoihieu.lrc" 
    
    if not os.path.exists(music_path):
        print(f"File nhạc không tồn tại: {music_path}")
    elif not os.path.exists(lyrics_path):
        print(f"File lời nhạc không tồn tại: {lyrics_path}")
    else:
        lyrics = read_lyrics(lyrics_path)
        
        play_music_with_lyrics(music_path, lyrics)
