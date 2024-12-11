import pygame as pg
import random 
from modulos.constantes import DIMENSION_PANTALLA, FPS, COORDENADAS_CIRCULO_ROJO, COORDENADAS_CIRCULO_AZUL
from .auxiliares import (cargar_configuraciones, draw_personajes, draw_atriles, draw_lines, draw_botones, draw_resp_atril, draw_answers_rojo, draw_answers_azul)
from .widgets.text_everything import TextEverything

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
        self.mostrar_resp = 0

        self.level_timer = 15
        self.reduccion_timer = 1
        self.first_last_timer = pg.time.get_ticks()
        self.clock = pg.time.Clock()
        self.info_timer = TextEverything(x=675, y=850, texto=f'Tiempo Restante: {self.level_timer}', pantalla=self.pantalla, color='COLOR_NEGRO', font_size=25)

        self.puntaje_pregunta = self.configs["valor"]
        self.puntaje_total = 0

    @staticmethod
    def get_nivel(pantalla):
        if Nivel.__instanciado is None:
            Nivel(pantalla)
        return Nivel.__instanciado
    
    def actualizar_timer(self):
        if self.level_timer > 0:
            tiempo_actual = pg.time.get_ticks()
            if tiempo_actual - self.first_last_timer > 1000:
                self.level_timer = self.level_timer - self.reduccion_timer
                self.first_last_timer = tiempo_actual
        else: 
            self.nivel_perdido()

    def cargar_configs(self):
        configs_globales = cargar_configuraciones()
        self.configs = configs_globales.get(f'pregunta_{self.nro_pregunta}')
        self.cant_preguntas = len(configs_globales) 

    def draw_preguntas_respuestas(self):
        pregunta = self.configs["pregunta"]
        pregunta_pantalla = TextEverything(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+100, texto=pregunta, pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
        pregunta_pantalla.draw()
        
        if self.orden_respuestas == 0:
            respuesta_rojo = self.configs["resp_correcta"]
            draw_answers_rojo(respuesta=respuesta_rojo)
            self.resp_correcta = 0
            respuesta_azul = self.configs["resp_incorrecta"]
            draw_answers_azul(respuesta=respuesta_azul)
        else:
            respuesta_rojo = self.configs["resp_incorrecta"]
            draw_answers_rojo(respuesta=respuesta_rojo)
            respuesta_azul = self.configs["resp_correcta"]
            draw_answers_azul(respuesta=respuesta_azul)
            self.resp_correcta = 1

    def orden_al_azar(self):
        self.orden_respuestas = random.randint(0,1)

    def responde_correctamente(self):
        self.puntaje_total += self.puntaje_pregunta
        self.nro_pregunta = self.nro_pregunta + 1
        self.orden_respuestas = random.randint(0,1)
        self.level_timer = 15

    def events(self, event_list: list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN:
                if (COORDENADAS_CIRCULO_ROJO[0]-60) < event.pos[0] < (COORDENADAS_CIRCULO_ROJO[0]+60):
                    if (COORDENADAS_CIRCULO_ROJO[1]-60) < event.pos[1] < (COORDENADAS_CIRCULO_ROJO[1]+60):
                        self.respuestas_atriles()
                        if self.resp_correcta == 0:
                            self.responde_correctamente()
                        else:
                            self.respondio_incorrectamente += 1
                elif (COORDENADAS_CIRCULO_AZUL[0]-60) < event.pos[0] < (COORDENADAS_CIRCULO_AZUL[0]+60):
                    if (COORDENADAS_CIRCULO_AZUL[1]-60) < event.pos[1] < (COORDENADAS_CIRCULO_AZUL[1]+60):
                        self.respuestas_atriles()
                        if self.resp_correcta == 1:
                            self.responde_correctamente()
                        else:
                            self.respondio_incorrectamente += 1

    def respuestas_atriles(self):
        self.reduccion_timer = 0
        self.mostrar_resp = 1
        self.draw_respuestas_atriles()

    def draw_marcador_puntaje(self):
        marcador_puntaje = TextEverything(x=120, y=950, texto=f'Puntaje: {self.puntaje_total}', pantalla=self.pantalla, color="COLOR_NEGRO", font_size=50)
        marcador_puntaje.draw()

    def draw_respuestas_atriles(self):
        respuesta_correcta=self.resp_correcta
        draw_resp_atril(0, respuesta_correcta)
        draw_resp_atril(1, respuesta_correcta)
        draw_resp_atril(2, respuesta_correcta)
        draw_resp_atril(3, respuesta_correcta)
        draw_resp_atril(4, respuesta_correcta)

    def nivel_ganado(self):
        self.draw_nivel()
        festejo_pantalla = TextEverything(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='GANASTE!', pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
        festejo_pantalla.draw()

    def nivel_perdido(self):
        self.draw_nivel()
        mensaje_pantalla = TextEverything(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='PERDISTE :(', pantalla=self.pantalla, color="COLOR_NEGRO", font_size=100)
        mensaje_pantalla.draw()

    def draw_nivel(self):
        surface = pg.image.load('assets/imagenes/fondo_colores.png').convert_alpha()
        surface = pg.transform.scale(surface, DIMENSION_PANTALLA)
        slave_rect = surface.get_rect()
        self.pantalla.blit(surface, slave_rect)

    def draw_items(self):
        draw_lines()
        draw_personajes()
        draw_atriles()
        self.info_timer.draw()

    def update(self, event_list: list):
        if self.respondio_incorrectamente > 0:
            self.nivel_perdido()
        elif self.nro_pregunta <= self.cant_preguntas:
            self.draw_nivel()
            self.draw_items()
            self.draw_preguntas_respuestas()
            draw_botones()
        else:
            self.nivel_ganado()
        self.info_timer = TextEverything(x=675, y=850, texto=f'Tiempo Restante: {self.level_timer}', pantalla=self.pantalla, color='COLOR_NEGRO', font_size=25)
        self.events(event_list=event_list)
        self.actualizar_timer()
        self.clock.tick(FPS)

