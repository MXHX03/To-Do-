from kivy.properties import StringProperty
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from database import Database


class NotesList(OneLineIconListItem):
    text = StringProperty()

    def show_notes(self, note):
        self.dialog = MDDialog(text=f'[color=#000000]{note}[/color]')
        self.dialog.open()


class DeletedNotesList(OneLineIconListItem):
    text = StringProperty()

    def show_notes(self, note):
        self.dialog = MDDialog(text=f'[color=#000000]{note}[/color]')
        self.dialog.open()

class AddNote(MDScreen):
    connection = Database().connection
    cursor = connection.cursor()

    def save(self, note):
        email = self.manager.get_screen("login_screen").ids['email_field'].text
        if note:
            self.cursor.execute("INSERT INTO notes (email, note) VALUE(%s, %s)", (email, note))

            self.connection.commit()
            toast("Note saved!")
            self.manager.current = "home_screen"
            self.manager.get_screen("home_screen").ids['nav'].switch_tab("screen1")
            self.manager.get_screen("home_screen").ids['notes_container'].add_widget(NotesList(text=note))
        else:
            toast("Blank space!")
