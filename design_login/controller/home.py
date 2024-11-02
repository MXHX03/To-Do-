
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import TwoLineAvatarListItem, TwoLineAvatarIconListItem
from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):
    Builder.load_file("views/home.kv")



class ChatItems(MDFloatLayout, TwoLineAvatarIconListItem, FakeRectangularElevationBehavior):
    image = StringProperty()
    name = StringProperty()
    last_msg = StringProperty()
    time_sent = StringProperty()