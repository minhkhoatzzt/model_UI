import pygame
import sys
from slider import Slider
from TextBox import TextBox

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom GUI")

# Màu sắc và font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 24)

# Tạo các thành phần GUI
slider1 = Slider(150, 80, 200, 20, 13, 20, BLUE, font)
slider2 = Slider(150, 130, 200, 20, 62, 100, BLUE, font)

textbox_title = TextBox(20, 20, 760, 30, font, GRAY, BLUE)  # Textbox hàng đầu
textbox1 = TextBox(150, 175, 200, 30, font, GRAY, BLUE)
textbox2 = TextBox(150, 225, 200, 30, font, GRAY, BLUE)
textbox3 = TextBox(150, 275, 200, 30, font, GRAY, BLUE)

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    # Vẽ tiêu đề của textbox đầu tiên
    title = font.render("Đặc tả:", True, BLACK)
    screen.blit(title, (20, 0))
    textbox_title.draw(screen)

    # Vẽ và xử lý sự kiện cho slider
    screen.blit(font.render("Sampling Steps:", True, BLACK), (20, 75))
    slider1.draw(screen)

    screen.blit(font.render("Độ tuân theo lời nhắc:", True, BLACK), (20, 125))
    slider2.draw(screen)

    # Vẽ và xử lý sự kiện cho textbox
    screen.blit(font.render("Góc chụp:", True, BLACK), (20, 180))
    textbox1.draw(screen)

    screen.blit(font.render("Thời gian:", True, BLACK), (20, 230))
    textbox2.draw(screen)

    screen.blit(font.render("Địa điểm:", True, BLACK), (20, 280))
    textbox3.draw(screen)

    # Vẽ nút "Bắt đầu"
    pygame.draw.rect(screen, BLUE, (20, 350, 100, 40), border_radius=5)
    button_text = font.render("Bắt đầu", True, WHITE)
    screen.blit(button_text, (45, 360))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Xử lý sự kiện cho các slider
        slider1.handle_event(event)
        slider2.handle_event(event)

        # Xử lý sự kiện cho các textbox
        textbox_title.handle_event(event)
        textbox1.handle_event(event)
        textbox2.handle_event(event)
        textbox3.handle_event(event)

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát
pygame.quit()
sys.exit()
