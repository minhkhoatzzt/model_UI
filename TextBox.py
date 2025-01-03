import pygame

class HeadingText:
    def __init__(self, text, font, color, boundingRect, alignment="center"):
        self.text = text
        self.font = font
        self.color = color
        self.boundingRect = boundingRect # the text will be put in this rect
        self.alignment = alignment
        
        self.textSurf = self.font.render(self.text, True, self.color)
        self.textRect = self.textSurf.get_rect()
        self.textRect.center = self.boundingRect.center
        
        if self.alignment == "left":
            self.textRect.left = self.boundingRect.left
        elif self.alignment == "right":
            self.textRect.right = self.boundingRect.right
        elif self.alignment == "center":
            self.textRect.center = self.boundingRect.center
            
    def draw(self, screen):
        screen.blit(self.textSurf, self.textRect)