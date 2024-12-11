import pygame as pg
from .form import Form
from ..widgets.boton import Boton
from ..widgets.text_title import TextTitle
from ..constantes import DIMENSION_PANTALLA

class FormMainMenu(Form):

    def __init__(self, name, pantalla, x, y, active):
        super().__init__(name, pantalla, x, y, active)
        
        self.surface = pg.image.load('assets/imagenes/fondo_colores.png').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.menu_prin_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-400, texto='This or That', pantalla=pantalla, color="COLOR_NEGRO", font_size=175)
        self.menu_prin_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-300, texto='MENU PRINCIPAL', pantalla=pantalla, color="COLOR_AZUL", font_size=50)

        self.boton_start = Boton(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='COMENZAR', pantalla=pantalla, on_click=self.click_start, font_size=100)
        self.boton_exit = Boton(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+400, texto='SALIR', pantalla=pantalla, on_click=self.click_exit, font_size=50)

        self.widget_list = [self.menu_prin_subtitle, self.menu_prin_title, self.boton_start, self.boton_exit]

    def click_start(self, parametro='form_juego'):
        self.set_active('form_juego')

    def click_exit(self, parametro):
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()

    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()

    

    

