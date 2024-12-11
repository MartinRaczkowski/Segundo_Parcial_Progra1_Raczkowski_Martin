import json
import pygame as pg
from .constantes import (
    CONFIGS_FILE, DIMENSION_PANTALLA, COORDENADA_DONATELLO, COORDENADA_LEONARDO, COORDENADA_MIGUELANGELO, COORDENADA_SPLINTER,
    COORDENADA_RAFAEL, COORDENADAS_ATRILES, COORDENADAS_RESPUESTAS_ATRILES, COLORES, COORDENADAS_CIRCULO_ROJO, COORDENADAS_CIRCULO_AZUL
)
from .widgets.item import Item
from .widgets.text_everything import TextEverything

### cargar preguntas y respuestas

def cargar_configuraciones():
    configuraciones = {}

    with open(CONFIGS_FILE, 'r') as configs:
        configuraciones = json.load(configs)
    return configuraciones 

def draw_answers_rojo(respuesta):
    respuesta_pantalla_rojo = TextEverything(x=COORDENADAS_CIRCULO_ROJO[0], y=COORDENADAS_CIRCULO_ROJO[1]-120, texto=respuesta, pantalla=pantalla, color="COLOR_NEGRO", font_size=100)
    respuesta_pantalla_rojo.draw()

def draw_answers_azul(respuesta):
    respuesta_pantalla_rojo = TextEverything(x=COORDENADAS_CIRCULO_AZUL[0], y=COORDENADAS_CIRCULO_AZUL[1]-120, texto=respuesta, pantalla=pantalla, color="COLOR_NEGRO", font_size=100)
    respuesta_pantalla_rojo.draw()

### pantalla

pantalla = pg.display.set_mode(DIMENSION_PANTALLA) 

fondo = pg.image.load('./assets/imagenes/fondo_colores.png')
fondo = pg.transform.scale(fondo, DIMENSION_PANTALLA)

def draw_lines():
    pg.draw.line(pantalla, COLORES['COLOR_NEGRO'], [0, 800], [200, 200], 5)
    pg.draw.line(pantalla, COLORES['COLOR_NEGRO'], [200, 200], [1200, 200], 5)
    pg.draw.line(pantalla, COLORES['COLOR_NEGRO'], [1200, 200], [1400, 800], 5)
    pg.draw.line(pantalla, COLORES['COLOR_NEGRO'], [200, 200], [200, 0], 5)
    pg.draw.line(pantalla, COLORES['COLOR_NEGRO'], [1200, 200], [1200, 0], 5)

### atriles

atril = pg.image.load("./assets/imagenes/atril.png")
atril = pg.transform.scale(atril, (150,250))
atriles = []
for coordenada in COORDENADAS_ATRILES:
    atril_item = Item(coordenada[0], coordenada[1], pantalla, atril)
    atriles.append(atril_item)

def draw_atriles():
    for atril in atriles:
        atril.draw()

def draw_resp_atril(numero: int, resp_correcta: int):
        if resp_correcta == 0:
            color = COLORES['COLOR_ROJO']
        else:
            color = COLORES['COLOR_AZUL']
        pg.draw.circle(pantalla, COLORES['COLOR_BLANCO'], COORDENADAS_RESPUESTAS_ATRILES[numero], 12)
        pg.draw.circle(pantalla, color, COORDENADAS_RESPUESTAS_ATRILES[numero], 10)

### personajes

donatello = pg.image.load("./assets/imagenes/Donatello.png")
donatello = pg.transform.scale(donatello, (250,450))
donatello_item = Item(COORDENADA_DONATELLO[0], COORDENADA_DONATELLO[1], pantalla, donatello)

leonardo = pg.image.load("./assets/imagenes/Leonardo.png")
leonardo = pg.transform.scale(leonardo, (250,450))
leonardo_item = Item(COORDENADA_LEONARDO[0], COORDENADA_LEONARDO[1], pantalla, leonardo)

splinter = pg.image.load("./assets/imagenes/Splinter.png")
splinter = pg.transform.scale(splinter, (250,250))
splinter_item = Item(COORDENADA_SPLINTER[0], COORDENADA_SPLINTER[1], pantalla, splinter)

miguelangelo = pg.image.load("./assets/imagenes/Miguelangelo.png")
miguelangelo = pg.transform.scale(miguelangelo, (250,450))
miguelangelo_item = Item(COORDENADA_MIGUELANGELO[0], COORDENADA_MIGUELANGELO[1], pantalla, miguelangelo)

rafael = pg.image.load("./assets/imagenes/Rafael.png")
rafael = pg.transform.scale(rafael, (250,350))
rafael_item = Item(COORDENADA_RAFAEL[0], COORDENADA_RAFAEL[1], pantalla, rafael)

def draw_personajes():
    items_list = [donatello_item, leonardo_item, splinter_item, miguelangelo_item, rafael_item]
    for item in items_list:
        item.draw()

### botones

def draw_botones():
    pg.draw.circle(pantalla, COLORES['COLOR_NEGRO'], COORDENADAS_CIRCULO_ROJO, 65)
    pg.draw.circle(pantalla, COLORES['COLOR_NEGRO'], COORDENADAS_CIRCULO_AZUL, 65)

    pg.draw.circle(pantalla, COLORES['COLOR_ROJO'], COORDENADAS_CIRCULO_ROJO, 60)
    pg.draw.circle(pantalla, COLORES['COLOR_AZUL'], COORDENADAS_CIRCULO_AZUL, 60)

### Cargar fuentes 

pg.font.init()
fuente_texto = pg.font.Font('./assets/fuentes/Halimount.otf', 50)

