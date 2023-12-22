from modules.settings import *
from modules.gui_elements import Label


class DClock:
    def __init__(self, game):
        self.game = game

        self.week_days = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
        self.months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

        # Texts
        self.title_label = Label(self.game,
                                 (WIDTH // 2, 50),
                                 TITLE_FONT,
                                 "A Simple Digital Clock",
                                 True,
                                 self.game.color2)

        self.get_hour()
        self.get_date()

    def get_hour(self):
        l_time = time.localtime()

        self.hour_label = Label(self.game,
                                (WIDTH // 2, 150),
                                HOUR_FONT,
                                f"{l_time.tm_hour}h {l_time.tm_min}m {l_time.tm_sec}s",
                                True,
                                self.game.color2)

    def get_date(self):
        l_time = time.localtime()
        week_day = self.week_days[l_time.tm_wday]
        month = self.months[l_time.tm_mon - 1]

        self.date_label = Label(self.game,
                                (WIDTH // 2, 220),
                                DATE_FONT,
                                f"{week_day}, {l_time.tm_mday} de {month} de {l_time.tm_year}",
                                True,
                                self.game.color2)

    def draw(self):
        # Writing the texts in the screen
        self.title_label.draw()  # Title
        self.hour_label.draw()  # Hour/Minute/Second
        self.date_label.draw()  # Week day, Month, Day, Year
