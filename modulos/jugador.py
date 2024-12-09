import pygame as pg

class Jugador:

    def __init__(self, nombre: str):
        
        self.nombre = nombre
        self.puntaje = 0
        self.puntaje_total = 0

    def get_nombre(self):
        return self.nombre
    
    def get_puntaje_actual(self):
        return self.puntaje
    
    def get_puntaje_total(self):
        return self.puntaje_total
    
    def set_puntaje(self, puntaje: int):
        self.puntaje = puntaje

    def add_puntaje(self, puntaje: int):
        self.puntaje += puntaje

    def actualizar_puntaje_total(self):
        self.puntaje_total += self.puntaje

    

