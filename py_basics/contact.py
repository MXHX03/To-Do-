class ContactApp:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def add_contact(self):  # method that adds a new contact
        fullname = self.first_name + " " + self.last_name  # concatenates the first and last name
        with open("contacts.txt", "a") as contacts:  # open our database for writing
            contacts.write(fullname + " " + self.phone_number + " " + self.email + "\n")
        print("contact saved successfully!")

    def search(self):  # method that searches for a particular contact in our database
        with open("contact.txt", "r") as contacts:   # open our database for writing
            contacts = contacts.readlines()  # saves all the contacts to a list
            print(contacts)
        for contact in contacts:  # looping through all the contacts
            print(contact)
            contact = contact.split(" ")  # split the values and add them to a list
            print(contact)
            # check if the first or the last name or phone number corresponds with the one in the database
            if self.first_name == contact[0] or self.last_name == contact[1] or self.phone_number == contact[2] in \
                    contact:
                print(f"fullname: {contact[0]} {contact[1]}")  # print fullname
                print(f"phone_number: {contact[2]}")  # print phone number
                print(f"email: {contact[3]}")  # print email
                break  # stop the loop from running
            else:
                print("contact not found")  # if contact is not found, print

    def list_contact(self):  # returns a list of contacts
        serial_num = 1  # serial number of the contacts
        with open("contacts.txt", "r") as contacts:  # open our database for reading
            contacts = contacts.readlines()

            for contact in contacts:  # looping through all the contacts
                print(f"{serial_num}) {contact}")  # assigning a serial number to each contact
                serial_num += 1  # incrementing the serial number after each iteration (loop)



ContactApp("", "", "", "").add_contact()
ContactApp("", "", "", "").search()
ContactApp("", "", "", "").list_contact()


# "a" -append
# "r"-read
# "W"-write
# \n - adds a new line