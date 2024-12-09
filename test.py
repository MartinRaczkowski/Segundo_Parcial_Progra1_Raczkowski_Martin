#test

import pygame as pg 
from modulos.constantes import (COLOR_AZUL, COLOR_ROJO, COLOR_NEGRO, COLOR_BLANCO, DIMENSION_PANTALLA, COORDENADAS_CIRCULO_AZUL, \
COORDENADAS_CIRCULO_ROJO, COORDENADAS_ATRILES, COORDENADAS_RESPUESTAS_ATRILES)

from modulos.formularios.form_main_menu import FormMainMenu

import random
# Configurar Ventana de juego
#pg.display.set_caption('Ejemplo de juego')
# Seteamos un icono a la ventana de juego
#pg.display.set_icon(splinter)


numero = random.randint(0,1)
print(numero)

#test

marcador_respuestas_correctas = 0
numero_pregunta = 0
respuesta_incorrecta = False

respuesta_correcta = 'rojo'

while juego_corriendo:

    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        
        if evento.type == pg.QUIT:
            print(evento, evento.type)
            juego_corriendo = False

        if evento.type == pg.MOUSEBUTTONDOWN:
            print(evento.pos)
            if (415) < evento.pos[0] < (535):
                if (790) < evento.pos[1] < (910):
                    print('rojo')
                    if respuesta_correcta == 'rojo':
                        marcador_respuestas_correctas += 1
                        numero_pregunta += 1
                    elif respuesta_correcta == 'azul':
                        respuesta_incorrecta = True

            if (815) < evento.pos[0] < (935):
                if (790) < evento.pos[1] < (910):
                    print('azul')
                    if respuesta_correcta == 'azul':
                        marcador_respuestas_correctas += 1
                        numero_pregunta += 1
                    elif respuesta_correcta == 'rojo':
                        respuesta_incorrecta = True




    #pantalla.blit(fondo, (0,0))



    #marcador_respuestas_correctas_en_pantalla = fuente_texto.render(f'Respuestas correctas: {marcador_respuestas_correctas}', True, COLOR_NEGRO)
    #pantalla.blit(marcador_respuestas_correctas_en_pantalla, (450, 950))

    #preguntas = ['2 + 2 = ', '2 + 3 = ', '2 * 2 = ']
    #if numero_pregunta % 2 == 0:
        #respuesta_correcta = 'rojo'
    #else: 
        #respuesta_correcta = 'azul'
    #if numero_pregunta < 3:
        #pregunta_en_pantalla = fuente_texto.render(f'{preguntas[numero_pregunta]}', True, COLOR_NEGRO)
        #i = 0
#        
        #while i < 5:
            #if respuesta_correcta == 'rojo':
                #j = 0
                #while j < 5:
                    #pg.draw.circle(pantalla, COLOR_BLANCO, COORDENADAS_RESPUESTAS_ATRILES[j], 12)
                    #pg.draw.circle(pantalla, COLOR_ROJO, COORDENADAS_RESPUESTAS_ATRILES[j], 10)
                    #j += 1
            #elif respuesta_correcta == 'azul':
                #j = 0
                #while j < 5:
                    #pg.draw.circle(pantalla, COLOR_BLANCO, COORDENADAS_RESPUESTAS_ATRILES[j], 12)
                    #pg.draw.circle(pantalla, COLOR_AZUL, COORDENADAS_RESPUESTAS_ATRILES[j], 10)
                    #j += 1
            #i += 1
    #pantalla.blit(pregunta_en_pantalla, (600, 700))
#
COORDENADAS_CIRCULO_ROJO = [475, 850]
COORDENADAS_CIRCULO_AZUL = [875, 850]
    #pg.draw.circle(pantalla, COLOR_NEGRO, COORDENADAS_CIRCULO_ROJO, 65)
    #pg.draw.circle(pantalla, COLOR_NEGRO, COORDENADAS_CIRCULO_AZUL, 65)

    #pg.draw.circle(pantalla, COLOR_ROJO, COORDENADAS_CIRCULO_ROJO, 60)
    #pg.draw.circle(pantalla, COLOR_AZUL, COORDENADAS_CIRCULO_AZUL, 60)




#
    #respuesta_a = fuente_texto.render(f'4', True, COLOR_BLANCO)
    #pantalla.blit(respuesta_a, (455, 830))
#
    #respuesta_b = fuente_texto.render(f'5', True, COLOR_BLANCO)
    #pantalla.blit(respuesta_b, (865, 830))
#
    #if respuesta_incorrecta == False:
        #texto = fuente_texto.render(f'', True, COLOR_NEGRO)
    #elif respuesta_incorrecta == True:
        #texto = fuente_texto.render(f'PERDISTE', True, COLOR_NEGRO)
#        
    #pantalla.blit(texto, (450, 550))

#pg.display.flip()



#pg.quit()
# 


