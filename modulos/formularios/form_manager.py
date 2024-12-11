import pygame as pg
from .form_main_menu import FormMainMenu
from .form_juego import FormJuego

class FormManager:

    def __init__(self, pantalla):
        
        self.main_screen = pantalla

        self.forms = [
            FormMainMenu(name='form_main_menu', pantalla=pantalla, x=0, y=0, active=True),
            FormJuego(name='form_juego', pantalla=pantalla, x=0, y=0, active=True)

        ]

    def forms_update(self, event_list: list):

        if self.forms[0].active:
            self.forms[0].update()
        
        elif self.forms[1].active:
            self.forms[1].update(event_list)

        elif self.forms[2].active:
            self.forms[2].update()
    
    def update(self, event_list: list):
        self.forms_update(event_list)

