from .auxiliares import (
    cargar_configuraciones
) # importar diccionario de los items
import pygame as pg
import random 
from modulos.constantes import DIMENSION_PANTALLA
from .widgets.text_title import TextTitle
from .auxiliares import leonardo_item, donatello_item, splinter_item, miguelangelo_item, rafael_item, atriles
COLOR_NEGRO = (0, 0, 0)
from .widgets.boton import Boton
class Nivel:

    __instanciado = None

    def __init__(self, pantalla):

        if Nivel.__instanciado is None:
            Nivel.__instanciado = self
        
        self.pantalla = pantalla
        self.nro_pregunta = 1
        self.orden_respuestas = 0
        self.resp_correcta = 0
        self.respondio_incorrectamente = 0
        self.configs = {}
        self.nivel_terminado = False
        self.cargar_configs()
        self.cant_preguntas = 0

        self.volver_menu_ppal = 0

        self.donatello_item = donatello_item
        self.leonardo_item = leonardo_item
        self.splinter_item = splinter_item
        self.miguelangelo_item = miguelangelo_item
        self.rafael_item = rafael_item

        self.items_list = [self.donatello_item, self.leonardo_item, self.splinter_item, self.miguelangelo_item, self.rafael_item]

        self.puntaje = 0

    @staticmethod
    def get_nivel(pantalla):
        if Nivel.__instanciado is None:
            Nivel(pantalla)
        return Nivel.__instanciado
    
    @staticmethod
    def esta_instanciado():
        return Nivel.__instanciado != None

    def cargar_configs(self):
        configs_globales = cargar_configuraciones()
        self.configs = configs_globales.get(f'pregunta_{self.nro_pregunta}')
        self.cant_preguntas = len(configs_globales) 

    def draw_preguntas_respuestas(self):

        pregunta = self.configs["pregunta"]
        pregunta_pantalla = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto=pregunta, pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
        pregunta_pantalla.draw()

        
        if self.orden_respuestas == 0:
            respuesta_rojo = self.configs["resp_correcta"]
            respuesta_pantalla_rojo = TextTitle(x=475, y=750, texto=respuesta_rojo, pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
            respuesta_pantalla_rojo.draw()
            self.resp_correcta = 0
            respuesta_azul = self.configs["resp_incorrecta"]
            respuesta_pantalla_azul = TextTitle(x=875, y=750, texto=respuesta_azul, pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
            respuesta_pantalla_azul.draw()

        else:
            respuesta_rojo = self.configs["resp_incorrecta"]
            respuesta_pantalla_rojo = TextTitle(x=475, y=750, texto=respuesta_rojo, pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
            respuesta_pantalla_rojo.draw()
            respuesta_azul = self.configs["resp_correcta"]
            respuesta_pantalla_azul = TextTitle(x=875, y=750, texto=respuesta_azul, pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
            respuesta_pantalla_azul.draw()
            self.resp_correcta = 1

    def orden_al_azar(self):
        self.orden_respuestas = random.randint(0,1)

    def responde_correctamente(self):
        self.nro_pregunta = self.nro_pregunta + 1
        self.orden_respuestas = random.randint(0,1)

    def events(self, event_list: list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN:
                print(event.pos)
                if (415) < event.pos[0] < (535):
                    if (790) < event.pos[1] < (910):
                        print('rojo')
                        if self.resp_correcta == 0:
                            self.responde_correctamente()
                        else:
                            self.respondio_incorrectamente += 1

                elif (815) < event.pos[0] < (935):
                    if (790) < event.pos[1] < (910):
                        print('azul')
                        if self.resp_correcta == 1:
                            self.responde_correctamente()
                        else:
                            self.respondio_incorrectamente += 1


    def nivel_ganado(self):
        self.draw_nivel()
        festejo_pantalla = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='GANASTE!', pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
        festejo_pantalla.draw()

    def nivel_perdido(self):
        # que el juego termine cuando el jugador se equivoca o se queda sin tiempo 
        self.draw_nivel()
        mensaje_pantalla = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='PERDISTE :(', pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
        mensaje_pantalla.draw()


    def draw_botones(self, pantalla):
        COORDENADAS_CIRCULO_ROJO = [475, 850]
        COORDENADAS_CIRCULO_AZUL = [875, 850]
        COLOR_ROJO = (200, 0, 0)
        COLOR_NEGRO = (0, 0, 0)
        COLOR_BLANCO = (255, 255, 255)
        COLOR_AZUL = (0, 0, 128)

        pg.draw.circle(pantalla, COLOR_NEGRO, COORDENADAS_CIRCULO_ROJO, 65)
        pg.draw.circle(pantalla, COLOR_NEGRO, COORDENADAS_CIRCULO_AZUL, 65)

        pg.draw.circle(pantalla, COLOR_ROJO, COORDENADAS_CIRCULO_ROJO, 60)
        pg.draw.circle(pantalla, COLOR_AZUL, COORDENADAS_CIRCULO_AZUL, 60)

    def draw_nivel(self):
        surface = pg.image.load('assets/imagenes/fondo_colores.png').convert_alpha()
        surface = pg.transform.scale(surface, DIMENSION_PANTALLA)
        slave_rect = surface.get_rect()
        self.pantalla.blit(surface, slave_rect)

    def draw_items(self):
        pg.draw.line(self.pantalla, COLOR_NEGRO, [0, 800], [200, 200], 5)
        pg.draw.line(self.pantalla, COLOR_NEGRO, [200, 200], [1200, 200], 5)
        pg.draw.line(self.pantalla, COLOR_NEGRO, [1200, 200], [1400, 800], 5)
        pg.draw.line(self.pantalla, COLOR_NEGRO, [200, 200], [200, 0], 5)
        pg.draw.line(self.pantalla, COLOR_NEGRO, [1200, 200], [1200, 0], 5)
        for item in self.items_list:
            item.draw()
        for atril in atriles:
            atril.draw()

    def draw(self):
        self.draw_nivel()
        self.draw_items()
        self.draw_botones()
    
    def update(self, event_list: list):
        if self.respondio_incorrectamente > 0:
            self.nivel_perdido()
        elif self.nro_pregunta <= self.cant_preguntas:
            self.draw_nivel()
            self.draw_items()
            self.draw_preguntas_respuestas()
            self.draw_botones(self.pantalla)
        else:
            self.nivel_ganado()
        self.events(event_list=event_list)
        
        


