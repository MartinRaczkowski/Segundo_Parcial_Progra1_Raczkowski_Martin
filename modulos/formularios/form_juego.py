import pygame as pg
from .form import Form
from ..widgets.boton import Boton
from ..widgets.text_title import TextTitle
from ..constantes import DIMENSION_PANTALLA, COLOR_NEGRO
from ..auxiliares import leonardo_item, donatello_item, splinter_item, miguelangelo_item, rafael_item, atriles
from ..widgets.item import Item
from ..nivel import Nivel


class FormJuego(Form):

    def __init__(self, name, pantalla, x, y, active):
        super().__init__(name, pantalla, x, y, active)

        self.surface = pg.image.load('assets/imagenes/fondo_colores.png').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.pantalla = pantalla 
        self.nivel = Nivel.get_nivel(pantalla=pantalla)

        self.donatello_item = donatello_item
        self.leonardo_item = leonardo_item
        self.splinter_item = splinter_item
        self.miguelangelo_item = miguelangelo_item
        self.rafael_item = rafael_item

        self.items_list = [self.donatello_item, self.leonardo_item, self.splinter_item, self.miguelangelo_item, self.rafael_item]


    def draw(self, event_list: list):
        self.nivel = Nivel.get_nivel(pantalla=self.pantalla)
        self.nivel.cargar_configs()
        self.nivel.update(event_list)

    def update(self, event_list: list):
        self.nivel = Nivel.get_nivel(pantalla=self.pantalla)
        self.draw(event_list=event_list)


