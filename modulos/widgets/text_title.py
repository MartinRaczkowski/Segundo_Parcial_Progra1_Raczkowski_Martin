import pygame as pg
from .widget import Widget
from ..constantes import COLORES

class TextTitle(Widget):

    def __init__(self, x, y, texto, pantalla, color, font_size = 50):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pg.font.Font('assets/fuentes/Halimount.otf', self.font_size)

        self.color = COLORES[color]
        self.image = self.font.render(self.texto, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        return super().draw()
    
    def update(self):
        self.draw()

    
    