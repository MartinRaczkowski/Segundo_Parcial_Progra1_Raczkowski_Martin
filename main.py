#test

import pygame as pg 

pg.init()

DIMENSION_PANTALLA = (1400, 1000)

# Colores
COLOR_AZUL = (0, 0, 128)
COLOR_AMARILLO = (255, 255, 0)
COLOR_VERDE = (0, 200, 0)
COLOR_ROJO = (200, 0, 0)
COLOR_NARANJA = (254, 120, 0)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)

# Cargar fuentes sin instalarlas en la pc
fuente_timer = pg.font.Font('./Halimount.otf', 50)

# Superficies
pantalla = pg.display.set_mode(DIMENSION_PANTALLA)

fondo = pg.image.load('./assets/imagenes/fondo.colores.png')
fondo = pg.transform.scale(fondo, DIMENSION_PANTALLA)

coordenadas_circulo_rojo = [475, 850]
coordenadas_circulo_azul = [875, 850]

atril = pg.image.load("./assets/imagenes/atril.png")
atril = pg.transform.scale(atril, (150,250))

donatello = pg.image.load("./assets/imagenes/Donatello.png")
donatello = pg.transform.scale(donatello, (250,450))

leonardo = pg.image.load("./assets/imagenes/Leonardo.png")
leonardo = pg.transform.scale(leonardo, (250,450))

miguelangelo = pg.image.load("./assets/imagenes/Miguelangelo.png")
miguelangelo = pg.transform.scale(miguelangelo, (250,450))

rafael = pg.image.load("./assets/imagenes/Rafael.png")
rafael = pg.transform.scale(rafael, (250,350))

splinter = pg.image.load("./assets/imagenes/Splinter.png")
splinter = pg.transform.scale(splinter, (250,250))

# Configurar Ventana de juego
pg.display.set_caption('Ejemplo de juego')
# Seteamos un icono a la ventana de juego
pg.display.set_icon(splinter)

coordenada_atril_a = [200, 200]
coordenada_atril_b = [400, 200]
coordenada_atril_c = [600, 200]
coordenada_atril_d = [800, 200]
coordenada_atril_e = [1000, 200]

coordenada_donatello = [150, 10]
coordenada_leonardo = [350, 10]
coordenada_splinter = [550, 150]
coordenada_miguelangelo = [750, 30]
coordenada_rafael = [950, 90]

#test

juego_corriendo = True

marcador_respuestas_correctas = 0
numero_pregunta = 0
respuesta_incorrecta = False

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

    pantalla.blit(fondo, (0,0))

    pg.draw.line(pantalla, COLOR_NEGRO, [0, 800], [200, 200], 5)
    pg.draw.line(pantalla, COLOR_NEGRO, [200, 200], [1200, 200], 5)
    pg.draw.line(pantalla, COLOR_NEGRO, [1200, 200], [1400, 800], 5)

    pg.draw.line(pantalla, COLOR_NEGRO, [200, 200], [200, 0], 5)
    pg.draw.line(pantalla, COLOR_NEGRO, [1200, 200], [1200, 0], 5)

    pantalla.blit(donatello, coordenada_donatello)
    pantalla.blit(leonardo, coordenada_leonardo)
    pantalla.blit(splinter, coordenada_splinter)
    pantalla.blit(miguelangelo, coordenada_miguelangelo)
    pantalla.blit(rafael, coordenada_rafael)

    pantalla.blit(atril, coordenada_atril_a)
    pantalla.blit(atril, coordenada_atril_b)
    pantalla.blit(atril, coordenada_atril_c)
    pantalla.blit(atril, coordenada_atril_d)
    pantalla.blit(atril, coordenada_atril_e)

    marcador_respuestas_correctas_en_pantalla = fuente_timer.render(f'Respuestas correctas: {marcador_respuestas_correctas}', True, COLOR_NEGRO)
    pantalla.blit(marcador_respuestas_correctas_en_pantalla, (450, 950))

    preguntas = ['2 + 2 = ', '2 + 3 = ', '2 * 2 = ']
    if numero_pregunta % 2 == 0:
        respuesta_correcta = 'rojo'
    else: 
        respuesta_correcta = 'azul'
    if numero_pregunta < 3:
        pregunta_en_pantalla = fuente_timer.render(f'{preguntas[numero_pregunta]}', True, COLOR_NEGRO)
        i = 0
        coordenadas_respuestas_atriles = [(275,320), (475,320), (675,320), (875,320), (1075,320)]
        while i < 5:
            if respuesta_correcta == 'rojo':
                j = 0
                while j < 5:
                    pg.draw.circle(pantalla, COLOR_BLANCO, coordenadas_respuestas_atriles[j], 12)
                    pg.draw.circle(pantalla, COLOR_ROJO, coordenadas_respuestas_atriles[j], 10)
                    j += 1
            elif respuesta_correcta == 'azul':
                j = 0
                while j < 5:
                    pg.draw.circle(pantalla, COLOR_BLANCO, coordenadas_respuestas_atriles[j], 12)
                    pg.draw.circle(pantalla, COLOR_AZUL, coordenadas_respuestas_atriles[j], 10)
                    j += 1
            i += 1
    pantalla.blit(pregunta_en_pantalla, (600, 700))

    

    pg.draw.circle(pantalla, COLOR_NEGRO, coordenadas_circulo_rojo, 65)
    pg.draw.circle(pantalla, COLOR_NEGRO, coordenadas_circulo_azul, 65)

    pg.draw.circle(pantalla, COLOR_ROJO, coordenadas_circulo_rojo, 60)
    pg.draw.circle(pantalla, COLOR_AZUL, coordenadas_circulo_azul, 60)

    respuesta_a = fuente_timer.render(f'4', True, COLOR_BLANCO)
    pantalla.blit(respuesta_a, (455, 830))

    respuesta_b = fuente_timer.render(f'5', True, COLOR_BLANCO)
    pantalla.blit(respuesta_b, (865, 830))

    if respuesta_incorrecta == False:
        texto = fuente_timer.render(f'', True, COLOR_NEGRO)
    elif respuesta_incorrecta == True:
        texto = fuente_timer.render(f'PERDISTE', True, COLOR_NEGRO)
        
    pantalla.blit(texto, (450, 550))

    pg.display.flip()



pg.quit() 