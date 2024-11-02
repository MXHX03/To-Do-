class NoteApp:
    """creating a note app"""

    def __init__(self, notes):
        self.notes = notes

    def write_note(self):
        create_note = open("notes.txt", "a")
        create_note.write(self.notes)

    def read_note(self):
        read_note = open("notes.txt", "r")
        mynotes = read_note.readlines()
        print(mynotes)


# NoteApp("I want to send the assignment today!\n").write_note()
# NoteApp("").read_note()


class Guest:
    def __init__(self, guest):
        self.guest = guest

    def write_guest(self):
        create_guest = open("guest.txt", "a")
        create_guest.write(name)


name = input("enter your name: ")
Guest(name).write_guest()


