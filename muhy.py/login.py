from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from database import Database
from kivy.clock import Clock
from add_note import NotesList


class LoginScreen(MDScreen):
    connection = Database().connection
    cursor = connection.cursor()

    def login(self):
        email = self.ids['email_field'].text
        password = self.ids['password_field'].text

        self.cursor.execute("SELECT email, password FROM user_info WHERE email = %s AND password = %s",
                            (email, password))
        result = self.cursor.fetchall()
        if result:
            with open("email.txt", "w") as save_email:
                save_email.write(email)
            self.manager.current = "home_screen"
            Clock.schedule_once(self.fetch_notes, 0.5)
        else:
            toast("Invalid email or address")

    def fetch_notes(self, *args):
        email = self.ids['email_field'].text
        self.cursor.execute("SELECT note FROM notes WHERE email = %s", (email, ))
        result = self.cursor.fetchall()
        print(result)
        for note in result:
            self.manager.get_screen("home_screen").ids['notes_container'].add_widget(NotesList(text=note[0]))

