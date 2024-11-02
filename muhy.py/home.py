from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton


class HomeScreen(MDScreen):
    def logout(self):
        yes_btn = MDFillRoundFlatButton(text="yes", on_press=self.yes, md_bg_color="green")
        no_btn = MDFillRoundFlatButton(text="no", on_press=self.no, md_bg_color="red")

        self.dialog = MDDialog(title="logout", text="Are you sure?", buttons=[yes_btn, no_btn])

        self.dialog.open()

    def yes(self, *args):
        self.manager.current = "login_screen"
        self.dialog.dismiss()


    def no(self, *args):
        self.dialog.dismiss()





