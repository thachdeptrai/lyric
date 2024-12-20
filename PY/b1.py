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
    ("♪", 13),
    ("Đâu,", 1.5),
    ("ta đã làm được gì đâu",2.9),
    ("Ta hỏi nhau rất nhiều câu", 2.2),
    ("Chúng ta sau này", 1.8),
    ("Sẽ bên cạnh hay sẽ vội bước mau", 4.7),
    ("Hôm đó là thứ bảy", 1.1),
    ("anh đã ước kim đồng hồ ngưng nhưng nó vẫn cứ nhảy", 2.33),
    ("Loay hoay với thùng ốp lưng khá nặng", 1.66),
    ("nên phải hai đứa đẩy", 1.5),
    ("Đẩy đi trên phố đi bộ để ", 1.33),
    ("bán ",0.6),
    ("với hai hàng nước chảy", 1.2),
    ("Lúc đó cũng có vài người nhận ra", 1.3),
    ("Anh", 0.4),
    ("Tham", 0.4),
    ("Gia", 0.4),
    ("nhiều bài hát và vài cuộc thi", 1.4),
    ("Nhưng",0.4),
    ("sau",0.4),
    ("bao",0.4),
    ("lâu nay",0.5),
    ("anh lại để cơ hội vụt đi", 1.8),    
    ("Ngày trước nhật hoàng cũng oai lắm mà", 2),
    ("Đi diễn nhiều người coi lắm mà",1.2),
    ("Anh chỉ biết ngậm chặt bờ môi",1.3),    
    ("tiếc nuối những ngày đằng sau cánh gà",1.99),    
    ("Không đủ can đảm để gọi về nhà",1.43),    
    ("nói rằng",0.44),    
    ("con đã thất bại nên phải cất lại",1.5),    
    ("Chắc tại tự cao nên con rất ngại",1.52),    
    ("Thấy lạc lõng khi nhắm đôi mắt lại",1.3),    
    ("Ôm mớ tiêu cực dù biết rất hại",1.4),
    ("Sai lầm lớn nhất nghĩ mình bất bại",2.5),    
    ("Anh luôn mơ thành sao hạng a",1.6),    
    ("Nhưng sao giờ đây nhìn lại ngày càng đi xuống",1.88),    
    ("Bao nhiêu người thành công ngoài kia thì anh lại càng thèm muốn",2.8),    
    ("Sóng lớn đẩy thuyền xa đò",1.5),    
    ("25 không làm ra trò",1.4),    
    ("Vẫn chưa thể nào tỏ tình nhưng đối với anh em như",3.6),    
    ("Mùa xuân ghé chơi hiên nhà",1.8),    
    ("Mời gọi mùa thu ở bên cạnh ta",2.6),    
    ("Nếu mai không còn nắng lên thì ai sẽ nhắc tên anh vậy",5.55),    
    ("Anh đã làm được gì",1.6),    
    ("Đâu, ta đã làm được gì đâu",3.8),    
    ("Ta hỏi nhau rất nhiều câu", 2.6),
    ("Chúng ta sau này", 1.8),
    ("Sẽ bên cạnh hay sẽ vội bước mau", 4.8),  
    ("Ta sẽ làm được điều đó",3.5),    
    ("Ta sẽ băng ngược chiều gió ",4.5),    
    ("giông kia",0.7),    
    ("ta vẫn không ngại ngần",1.5),    
    ("Cười lên anh,",2),    
    ("đời sẽ chẳng mấy vui nếu không ồ ạt,",3),    
    ("vỗ về từng con sóng lớn",2.7),    
    ("Khiến ta càng phải khôn hơn",2),    
    ("và mạnh mẽ hơn",2),    
    ("Mọi muộn phiền sẽ qua",2.4),    
    ("chúng ta nắm tay đi hết chặng đường",4.5),    
    ("Miễn đôi mình vui là được nhé anh",9),    
    # ("",),    
    # ("",),    
    # ("",),    
#python anhdalamgidau.py
#python b1.py
]
color_list = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

# Hàm hiển thị lời bài hát
def display_lyrics(lyrics_with_delay):
    current_words = []  # Danh sách từ ngắn cần giữ lại
    margin = " " * 5  # Lề 5 ký tự

    for line, delay in lyrics_with_delay:
        os.system('cls' if os.name == 'nt' else 'clear')
        words = line.split()
        random_color = random.choice(color_list)
        if len(words) < 3:
            current_words.append(line)  # Lưu từ ngắn lại
            print(margin + random_color + " ".join(current_words))   
        else:
            print(margin + random_color + " ".join(current_words))  
            print(margin + random_color + line)   
            current_words = []   
        time.sleep(delay)


# Hàm phát nhạc
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

if __name__ == "__main__":
    # Đường dẫn file nhạc
    music_path = "MP3/anhdalamgidau.mp3"  

    # Chạy phát nhạc trong luồng riêng
    music_thread = Thread(target=play_music, args=(music_path,))
    music_thread.start()

    # Hiển thị lời bài hát
    display_lyrics(lyrics_with_delay)

    # Đợi luồng nhạc hoàn thành
    music_thread.join()