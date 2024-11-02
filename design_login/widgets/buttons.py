from kivy.lang import Builder
from kivymd.uix.button import MDIconButton, MDTextButton

Builder.load_string("""
<IconBtn>
    theme_icon_color: "Custom"
    icon_size: app.font_size.h1
    
<TextBtn>
    theme_text_color: "Custom"
    markup: True
    font_size: app.font_size.h4
    font_name: "Roboto-Bold"
""")


class IconBtn(MDIconButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class TextBtn(MDTextButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)