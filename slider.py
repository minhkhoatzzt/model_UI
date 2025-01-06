import pygame

class Slider:
    def __init__(self, x, y, width, height, value, max_value, color, font, label=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.max_value = max_value
        self.color = color
        self.font = font
        self.label = label
        self.dragging = False

    def draw(self, screen):
        # Vẽ nhãn (label) phía trên thanh trượt
        if self.label:
            label_text = self.font.render(self.label, True, (0, 0, 0))
            label_pos = (self.x, self.y - label_text.get_height() - 10)  # Đặt cách thanh trượt 10px
            screen.blit(label_text, label_pos)

        # Vẽ thanh nền slider
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height), border_radius=5)

        # Vẽ phần đã kéo của slider
        fill_width = (self.value / self.max_value) * self.width
        pygame.draw.rect(screen, self.color, (self.x, self.y, fill_width, self.height), border_radius=5)

        # Vẽ nút trượt
        knob_x = self.x + fill_width
        knob_radius = self.height // 2
        pygame.draw.circle(screen, (50, 50, 50), (int(knob_x), self.y + knob_radius), knob_radius)

        # Hiển thị giá trị hiện tại
        value_text = self.font.render(f"{int(self.value)}", True, (0, 0, 0))
        value_pos = (self.x + self.width + 10, self.y + self.height // 2 - value_text.get_height() // 2)
        screen.blit(value_text, value_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra nếu nhấn vào thanh hoặc nút trượt
            knob_x = self.x + (self.value / self.max_value) * self.width
            knob_radius = self.height // 2
            if (self.x <= event.pos[0] <= self.x + self.width and 
                self.y <= event.pos[1] <= self.y + self.height) or \
               ((event.pos[0] - knob_x) ** 2 + (event.pos[1] - (self.y + knob_radius)) ** 2 <= knob_radius ** 2):
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        if event.type == pygame.MOUSEMOTION and self.dragging:
            relative_pos = event.pos[0] - self.x
            self.value = max(0, min(self.max_value, (relative_pos / self.width) * self.max_value))
