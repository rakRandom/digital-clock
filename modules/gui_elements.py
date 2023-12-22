from modules.settings import *


class Button:
    def __init__(self, game, pos, font, text, color, background):
        self.game = game
        self.text = Label(game, pos, font, text, True, color, background)
        self.touched = False

    def update(self, pos, font, text, color, background):
        self.text.update(pos, font, text, True, color, background)

    def draw(self):
        self.text.draw()
        pg.draw.rect(self.game.screen, self.game.color2, self.text.rect.inflate(15, 15), 2)

    def is_touched(self):
        if self.is_hovered() and pg.mouse.get_pressed()[0] and not self.touched:
            self.touched = True
            return True
        if not (self.is_hovered() and pg.mouse.get_pressed()[0]):
            self.touched = False
            return False

    def is_hovered(self):
        if self.text.rect.inflate(15, 15).collidepoint(pg.mouse.get_pos()):
            return True
        else:
            return False


class Label:
    def __init__(self, game, pos, font, text, antialias, color, background=None):
        self.game = game
        self.text_surf = font.render(text, antialias, color, background)
        self.text_rect = self.text_surf.get_rect(center=pos)

    def update(self, pos, font, text, antialias, color, background=None):
        self.text_surf = font.render(text, antialias, color, background)
        self.text_rect = self.text_surf.get_rect(center=pos)

    def draw(self):
        self.game.screen.blit(self.text_surf, self.text_rect)

    @property
    def rect(self):
        return self.text_rect
