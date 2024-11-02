from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string("""
<Circle>
    size_hint: None, None
    radius: [100]
""")


class Circle(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
