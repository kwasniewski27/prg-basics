class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Dodaje nowy kontakt do listy."""
        self.contacts.append(contact)

    def display_contacts(self):
        """Wyświetla wszystkie kontakty."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(contact)
