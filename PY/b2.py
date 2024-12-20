import os
import time
from threading import Thread
import pygame
from colorama import init, Fore
import random


# Khởi tạo colorama
init(autoreset=True)
# Lời bài hát và thời gian hiển thị từng câu
lyrics_with_delay = [
    ("♪ Ta mất nhau thật rồi em ơi", 3,True),
    ("Tan vỡ hai cực đành ",3.5,False),    
    ("chia đôi",0.55,False),    
    ("Anh sẽ luôn ghi nhớ em",2.02,False),    
    ("Trong từng tế bào",1.33,False),    
    ("Vậy mà dừng lại như thế sao",5.33,True),    
    ("Cuộc gọi nhỡ cho em hàng đêm",1.4,False),    
    ("Đến tận 200 lần",1.7,False),    
    ("Dòng ký ức trong em về anh",1.8,False),    
    ("Bây giờ đang phai dần",2.3,False),    
    ("Quay gót rời đi",1.5,False),    
    ("không để lại gì",1.8,False),    
    ("Bay vút qua tầm tay",1.6,False),    
    ("Sao còn vương vấn để làm gì",1.6,True),    
    ("Bọn mình kết thúc\n",1.4,False),    
    ("Thật rồi",0.4,False),    
    ("Hết sức ",0.4,False),  
    ("Thật rồi",0.4,False),  
    ("Phải không em ơi",1.6,True),    
    ("Chuyện tình có khúc phải lòng",1.6,False),    
    ("Có lúc phải rời\n",1.2,False),    
    ("Vậy đến lúc rồi",1.55,True),    
    ("Và có lẽ giờ này",1.5,False),    
    ("Em đã ngủ say",1.5,False),    
    ("Còn anh thì vẫn mang",1.5,False),    
    ("Nỗi nhớ em trong đêm thật dài",3.5,True),    
    ("Thêm lý do cho anh tồn tại",3.3,False),    
    ("Để lại chạm vào bờ môi ấy dịu dàng",3.8,False),    
    ("Lời thì thầm ngọt ngào bên tai",3.7,True),    
    ("Ta mất nhau thật rồi em ơi",3.5,False),    
    ("Tan vỡ hai cực đành chia đôi",3.3,False),    
    ("Anh sẽ luôn ghi nhớ em",2.2,False),    
    ("Trong từng tế bào",1.7,False),    
    ("Vậy mà dừng lại như thế sao...",6.9,True),    
   
 
#  python b2.py
]
color_list = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

def display_lyrics(lyrics_with_delay):
    current_words = []  # Danh sách từ ngắn cần giữ lại
    margin = " " * 5  # Lề 5 ký tự

    for line, delay, use_typing_effect in lyrics_with_delay:
        os.system('cls' if os.name == 'nt' else 'clear')
        words = line.split()
        random_color = random.choice(color_list)

        # Hiển thị từ ngắn trước đó
        if current_words:
            print(margin + random_color + " ".join(current_words))

        if use_typing_effect:
            # Hiệu ứng gõ từng ký tự
            start_time = time.time()  # Ghi lại thời điểm bắt đầu
            print(margin, end='', flush=True)  # In lề trước
            for char in line:
                print(random_color + char, end='', flush=True)  # Mỗi ký tự đều được gán màu
                time.sleep(0.07)  # Độ trễ giữa các ký tự
            print()  # Xuống dòng sau khi hoàn thành dòng hiện tại

            # Chờ thời gian còn lại để đồng bộ
            elapsed_time = time.time() - start_time
            if delay > elapsed_time:
                time.sleep(delay - elapsed_time)
        else:
            # Hiển thị toàn bộ dòng mà không có hiệu ứng gõ chữ
            print(margin + random_color + line)
            time.sleep(delay)

        # Lưu từ ngắn hoặc reset danh sách
        if len(words) < 5:
            current_words.append(line)  # Lưu từ ngắn lại
        else:
            current_words = []  # Xóa danh sách từ ngắn

# Hàm phát nhạc
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

if __name__ == "__main__":
    # Đường dẫn file nhạc
    music_path = "MP3/matketnoi.mp3"  

    # Chạy phát nhạc trong luồng riêng
    music_thread = Thread(target=play_music, args=(music_path,))
    music_thread.start()

    # Hiển thị lời bài hát
    display_lyrics(lyrics_with_delay)

    # Đợi luồng nhạc hoàn thành
    music_thread.join()