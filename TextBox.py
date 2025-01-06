import pygame

class TextBox:
    def __init__(self, x, y, width, height, font, color, active_color, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.color = color
        self.active_color = active_color
        self.text = text
        self.active = False

    def draw(self, screen):
        # Vẽ khung TextBox
        pygame.draw.rect(screen, self.active_color if self.active else self.color, self.rect, border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, width=1, border_radius=5)

        # Hiển thị phần chữ bên trong TextBox
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_width = text_surface.get_width()

        # Cắt chữ nếu vượt chiều rộng của TextBox
        if text_width > self.rect.width - 10:  # Trừ khoảng cách padding
            text_surface = self.font.render(self.text[-(len(self.text) - 1):], True, (0, 0, 0))

        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
