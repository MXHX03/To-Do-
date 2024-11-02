from kivy.lang import Builder
from kivymd.uix.label import MDLabel

Builder.load_string("""
<TextLabel>
    theme_text_color:"Custom"
""")


class TextLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)