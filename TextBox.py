import pygame

class TextBox:
    def __init__(self, x, y, width, height, font_size=30, text_color=(0, 0, 0), bg_color=(255, 255, 255), border_color=(0, 0, 0), border_width=2, label=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text = ""
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_width = border_width
        self.active = False
        self.label = label

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked inside the text box
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False  # Exit editing mode when pressing Enter
            else:
                self.text += event.unicode

    def draw(self, screen):
        # Draw the label
        label_surface = self.font.render(self.label, True, self.text_color)
        screen.blit(label_surface, (self.rect.x - label_surface.get_width() - 10, self.rect.y + (self.rect.height - label_surface.get_height()) // 2))

        # Draw the text box background
        pygame.draw.rect(screen, self.bg_color, self.rect)

        # Draw the border
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

        # Ensure text fits within the text box
        text_surface = self.font.render(self.text, True, self.text_color)
        while text_surface.get_width() > self.rect.width - 10:  # Allow some padding
            self.text = self.text[1:]  # Remove the first character
            text_surface = self.font.render(self.text, True, self.text_color)

        # Render the text
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

# Example usage
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Text Box Example")

    clock = pygame.time.Clock()
    running = True

    textbox = TextBox(300, 250, 200, 50, label="Đặc điểm")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            textbox.handle_event(event)

        screen.fill((200, 200, 200))
        textbox.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
