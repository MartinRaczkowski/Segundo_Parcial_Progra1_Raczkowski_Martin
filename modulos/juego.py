import sys
import pygame as pg

from modulos.formularios import FormManager

from modulos.constantes import DIMENSION_PANTALLA

def correr_juego():
    
    pg.init()

    pantalla = pg.display.set_mode(DIMENSION_PANTALLA)
    pg.display.set_caption('This or That')

    juego_corriendo = True 

    forms = FormManager(pantalla)

    while juego_corriendo:

        lista_eventos = pg.event.get()
        for evento in lista_eventos:

            if evento.type == pg.QUIT:
                print(evento, evento.type)
                juego_corriendo = False

        forms.update(lista_eventos)
        pg.display.update()

    pg.quit()
    sys.exit()
