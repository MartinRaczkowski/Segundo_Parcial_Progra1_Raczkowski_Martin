from modulos.widgets.widget import Widget
import pygame as pg

class Item():

    def __init__(self, x: int, y: int, pantalla, image): 
        
        self.x = x
        self.y = y
        self.pantalla = pantalla
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self):
        self.pantalla.blit(self.image, (self.x, self.y))

    def update(self):
        self.draw()

    