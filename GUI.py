import TextBox as textBox
import pygame

class GUI:
    def __init__(self):
        self.textBox = textBox.TextBox()

    def run(self):
        self.textBox.run()
    
    def draw(self, screen):
        
        self.textBox.draw(screen)
        
        
def main():
    gui = GUI()
    gui.run()
    gui.draw(pygame.display.get_surface())