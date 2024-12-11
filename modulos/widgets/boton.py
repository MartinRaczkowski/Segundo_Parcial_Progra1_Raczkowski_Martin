from modulos.widgets.widget import Widget
import pygame as pg
from ..constantes import COLORES

class Boton(Widget):

    def __init__(self, x, y, texto, pantalla, font_size = 25, on_click = None, on_click_param = None):
        super().__init__(x, y, texto, pantalla, font_size) 
        self.font = pg.font.Font('assets/fuentes/Halimount.otf', self.font_size)
        self.image = self.font.render(self.texto, True, COLORES['COLOR_ROJO'])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.on_click = on_click
        self.on_click_param = on_click_param

    def boton_presionado(self):
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                pg.time.delay(300)
                self.on_click(self.on_click_param)


    def draw(self):
        super().draw()

    def update(self):
        self.draw()
        self.boton_presionado()
        




    

    