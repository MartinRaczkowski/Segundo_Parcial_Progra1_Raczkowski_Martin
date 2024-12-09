import json
import pygame as pg
from .constantes import (
    CONFIGS_FILE, DIMENSION_PANTALLA, COORDENADA_DONATELLO, COORDENADA_LEONARDO, COORDENADA_MIGUELANGELO, COORDENADA_SPLINTER,
    COORDENADA_RAFAEL, COORDENADAS_ATRILES, COORDENADAS_RESPUESTAS_ATRILES
)
from .widgets.item import Item

def cargar_configuraciones():

    configuraciones = {}

    with open(CONFIGS_FILE, 'r') as configs:
        configuraciones = json.load(configs)
    return configuraciones 

def crear_diccionario_item(sup_imagen: pg.Surface, sup_rect: pg.Rect) -> dict:

    objeto = {
        "imagen": sup_imagen,
        "rect": sup_rect,
        "visible": True
    }

    return objeto

pantalla = pg.display.set_mode(DIMENSION_PANTALLA) 

fondo = pg.image.load('./assets/imagenes/fondo_colores.png')
fondo = pg.transform.scale(fondo, DIMENSION_PANTALLA)

atril = pg.image.load("./assets/imagenes/atril.png")
atril = pg.transform.scale(atril, (150,250))
atriles = []
for coordenada in COORDENADAS_ATRILES:
    atril_item = Item(coordenada[0], coordenada[1], pantalla, atril)
    atriles.append(atril_item)

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

# Cargar fuentes 
pg.font.init()
fuente_texto = pg.font.Font('./assets/fuentes/Halimount.otf', 50)

