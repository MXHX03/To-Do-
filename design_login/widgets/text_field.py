from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField

Builder.load_string("""
<TextField>
    hint_text_color_normal: app.colors.dark
    hint_text_color_focus: app.colors.dark
    line_color_normal: app.colors.dark
    line_color_focus: app.colors.dark
    text_color_normal: app.colors.dark
    text_color_focus: app.colors.dark
    size_hint_x: .8
    mode: "fill"
    radius: [20, 20, 20, 20]
    active_line: False
    size_hint_y: .08
""")


class TextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)