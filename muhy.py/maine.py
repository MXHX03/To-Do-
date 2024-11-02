from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition, FadeTransition, NoTransition
from signup import SignupScreen
from login import LoginScreen
from home import HomeScreen
from add_note import AddNote, NotesList, DeletedNotesList
from database import Database
import os



class MyNotes(MDApp):
    def build(self):
        Builder.load_file("signup.kv")
        Builder.load_file("login.kv")
        Builder.load_file("home.kv")
        Builder.load_file("add_note.kv")

        self.theme_cls.material_style = "M3"

        self.screenmanager = ScreenManager(transition=SwapTransition())
        screens = [SignupScreen(name="signup_screen"),
                   LoginScreen(name="login_screen"),
                   HomeScreen(name="home_screen"),
                   AddNote(name="add_note_screen")]

        for screen in screens:
            self.screenmanager.add_widget(screen)
        return self.screenmanager

    def on_start(self):
        current_path = os.getcwd()
        if os.path.exists(f"{current_path}/email.txt"):
            with open("email.txt", "r") as read_email:
                read = read_email.readlines()
            fetched_email = read[0]
            self.screenmanager.get_screen("login_screen").ids['email_field'].text = fetched_email

    def delete_note(self, note):
        connection = Database().connection
        cursor = connection.cursor()
        email = self.screenmanager.get_screen("login_screen").ids['email_field'].text

        cursor.execute("INSERT INTO deleted_notes(email,note) VALUE(%s, %s)", (email, note))
        connection.commit()

        self.screenmanager.get_screen("home_screen").ids['deleted_notes_container'].add_widget(DeletedNotesList
                                                                                               (text=note))

        cursor.execute("DELETE FROM notes WHERE email= %s AND note = %s", (email, note))
        connection.commit()

        self.ask_dialog.dismiss()


        self.screenmanager.get_screen("home_screen").ids['notes_container'].clear_widgets()
        cursor.execute("SELECT note FROM notes WHERE email = %s", (email,))
        result = cursor.fetchall()
        # result = result[0]
        for fetched_note in result:
            self.screenmanager.get_screen("home_screen").ids['notes_container'].add_widget(NotesList
                                                                                           (text=fetched_note[0]))

    def ask(self, note):
        yes_btn = MDFillRoundFlatButton(text="yes", on_press=lambda x: self.delete_note(note), md_bg_color="green")
        no_btn = MDFillRoundFlatButton(text="no", on_press=self.close, md_bg_color="red")
        self.ask_dialog = MDDialog(title="[color=#b90000]delete?[/color]",  text="Are you sure?", buttons=[yes_btn,
                                                                                                           no_btn])

        self.ask_dialog.open()

    def close(self, *args):
        self.ask_dialog.dismiss()


    def remove(self, note):
        connection = Database().connection
        cursor = connection.cursor()
        email = self.screenmanager.get_screen("login_screen").ids['email_field'].text

        cursor.execute("DELETE FROM deleted_notes WHERE email = %s AND note = %s", (email, note))
        connection.commit()
        toast("removed successfully!")

        self.screenmanager.get_screen("home_screen").ids['deleted_notes_container'].clear_widgets()

        cursor.execute("SELECT note FROM deleted_notes WHERE email=%s", (email,))
        result = cursor.fetchall()
        for fetched_note in result:
            self.screenmanager.get_screen("home_screen").ids['deleted_notes_container'].add_widget(DeletedNotesList
                                                                                           (text=fetched_note[0]))




MyNotes().run()

