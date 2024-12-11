import pygame as pg
from .form import Form
from ..constantes import DIMENSION_PANTALLA
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

    def draw(self, event_list: list):
        self.nivel.cargar_configs()
        self.nivel.update(event_list)
        if self.nivel.mostrar_resp == 1:
            start_time = pg.time.get_ticks()  
            while pg.time.get_ticks() - start_time < 1000:
                pass
            self.nivel.reduccion_timer = 1

        self.nivel.draw_marcador_puntaje()

    def update(self, event_list: list):
        self.draw(event_list=event_list)


