

class Form:

    forms_dict = {}

    def __init__(self, name: str, pantalla, x: int, y: int, active: bool):

        self.forms_dict[name] = self
        self.pantalla = pantalla
        self.active = active
        self.x = x
        self.y = y

    def set_active(self, name: str):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def draw(self):
        self.pantalla.blit(self.surface, self.slave_rect)

    