from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from database import Database
import re


class SignupScreen(MDScreen):
    connection = Database().connection
    cursor = connection.cursor()

    def signup(self):
        email = self.ids['email_field'].text
        password = self.ids['password_field'].text
        pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|edu|org)"

        if email == "" and password == "":
            Snackbar(text="All fields are required", size_hint_x=.8, bg_color="red", radius=[10, 0, 10, 0],
                     snackbar_animation_dir="Right", snackbar_y="10dp", snackbar_x="10dp").open()

        elif not re.search(pattern, email):
            Snackbar(text="Please enter a valid email address", bg_color="red", radius=[20, 20, 20, 20],
                     snackbar_x="15dp", snackbar_y="15dp").open()
        elif len(password) < 6:
            Snackbar(text="password should not be less than 6 characters", bg_color="red", radius=[20, 20, 20, 20],
                     snackbar_x="15dp", snackbar_y="15dp").open()
        else:
            try:
                self.cursor.execute("INSERT INTO user_info (email, password) VALUES (%s, %s)", (email, password))
                self.connection.commit()
                toast("Account created successfully!")
            except Database().integrity_error:
                toast("User already exist!")


