from modules.settings import *
from modules import gui_elements, dclock


class Main:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Digital Clock")
        pg.display.set_icon(pg.image.load("assets/images/clock.png").convert_alpha())

        # Variables
        self.show_fps = False
        self.theme = False  # False = Light Theme - True = Dark Theme
        self.color1 = WHITE
        self.color2 = BLACK

        self.dclock = dclock.DClock(self)

        # GUI elements
        self.theme_btn = gui_elements.Button(self, (WIDTH//2, HEIGHT - 50), BUTTON_FONT, "Change Theme", self.color2, self.color1)

        # Events
        self.update_hour = pg.USEREVENT + 3
        self.update_date = pg.USEREVENT + 4

        pg.time.set_timer(self.update_hour, 100)
        pg.time.set_timer(self.update_date, 5000)

        # Sound
        self.click_sound = pg.mixer.Sound("assets/audios/click-sound.mp3")

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == self.update_hour:
                self.dclock.get_hour()  # Get hour

            if event.type == self.update_date:
                self.dclock.get_date()  # Get date

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_INSERT:
                    self.show_fps = False if self.show_fps else True

    def update(self):
        # Set cursor
        if self.theme_btn.is_hovered():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        # Change theme
        if self.theme_btn.is_touched():
            self.click_sound.play()

            # Changing the colors
            if self.theme:
                self.color1 = WHITE
                self.color2 = BLACK
                self.theme = False
            else:
                self.color1 = BLACK
                self.color2 = WHITE
                self.theme = True

            # Updating the theme
            self.dclock = dclock.DClock(self)
            self.theme_btn.update((WIDTH // 2, HEIGHT - 50), BUTTON_FONT, "Change Theme", self.color2, self.color1)

        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(self.color1)

        # Writing the texts in the screen
        self.dclock.draw()
        self.theme_btn.draw()

        if self.show_fps:
            self.screen.blit(FONT.render(f"{self.clock.get_fps():.1f}", False, self.color2), (0, 0))

        pg.display.update()

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()
