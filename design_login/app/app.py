from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.utils import rgba, QueryDict, platform
from kaki.app import App
from PIL import ImageGrab
from kivy.core.window import Window
from controller.login import LoginScreen

from controller.signup import SignupScreen

from controller.home import HomeScreen

resolution = ImageGrab.grab().size

if platform == "linux" or platform == "win" or platform == "macosx":
    Window.size = (350, 720)
    Window.top = 0
    Window.left = resolution[0] - Window.width


class LoginDesign(App, MDApp):

    colors = QueryDict()
    colors.yellow = rgba("#FFAE48")
    colors.dark = rgba("#4C525C")
    colors.blue = rgba("#58BFE6")
    colors.white = rgba("#FFFFFF")

    font_size = QueryDict()
    font_size.heading = "28dp"
    font_size.h1 = "22dp"
    font_size.h2 = "20dp"
    font_size.h3 = "18dp"
    font_size.h4 = "16dp"
    font_size.h5 = "14dp"
    font_size.h6 = "12dp"

    CLASSES = {
        "HomeScreen":
            "design_login.controller.home.HomeScreen",
        "LoginScreen": "design_login.controller.login.LoginScreen"
    }

    AUTORELOADER_PATHS = [(".", {"recursive": True}),

    ]

    KV_FILES = [
        "views/home.kv",
        "views/signup.kv",
        "views/login.kv"
    ]

    def build_app(self):
        self.screenmanager = ScreenManager()
        screens = [LoginScreen(name="login"),
                   SignupScreen(name="signup"),
                   HomeScreen(name="home")
                   ]

        for screen in screens:
            self.screenmanager.add_widget(screen)
        self.screenmanager.current = "signup"
        return self.screenmanager

    def change_screen(self, screen_name):
        self.screenmanager.current = screen_name
