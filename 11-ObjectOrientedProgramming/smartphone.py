from contact import Contact
from contact_list import ContactList

def main():
    # Tworzenie obiektu ContactList
    contact_list = ContactList()

    # Dodawanie kontaktów
    contact_list.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    contact_list.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    contact_list.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    contact_list.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    # Wyświetlanie kontaktów
    contact_list.display_contacts()

if __name__ == "__main__":
    main()
