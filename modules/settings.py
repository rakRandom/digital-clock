import pygame as pg
import time
import sys

pg.init()

RES = WIDTH, HEIGHT = 600, 350
FPS = 60

TITLE_FONT = pg.font.Font(pg.font.get_default_font(), 26)
HOUR_FONT = pg.font.Font(pg.font.get_default_font(), 80)
DATE_FONT = pg.font.Font(pg.font.get_default_font(), 24)
BUTTON_FONT = pg.font.Font(pg.font.get_default_font(), 20)
FONT = pg.font.Font(pg.font.get_default_font(), 14)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
