"""
Created on Wed Feb  5 22:37:26 2025

@author: greglabmeier

Edited by Jack Rellamas
"""

def add_contact(contacts: dict):
    name = input("Enter name: ").lower()
    phone = input("Enter phone number: ").lower()
    email = input("Enter email: ").lower()

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")

def delete_contact(contacts: dict):
    name = input("Enter name to delete: ").lower()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def view_single_contact(contacts: dict, name: str):
    name = name.lower()
    if name in contacts:
        print(f'n{name}: {contacts[name]}')
    else:
        print("Contact not found.")

def view_contacts_by_letter(contacts: dict):
    letter = input('Enter the first letter of the names you want to see: ').lower()
    for name in contacts:
        if name[0].upper() == letter:
            view_single_contact(contacts, name)

def update_contact(contacts: dict, name: str):
    name = name.lower()
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} updated successfully!")
    else:
        print('Contact not found.')

contacts = {}
keep_asking = True
while keep_asking:
    print("\nContact Book Menu:")
    print('0. View Full Contact Book')
    print("1. Add Contact")
    print("2. Delete Contact")
    print('3. View Single Contact')
    print('4. View Contacts by Letter')
    print('5. Update a contact')
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '0':
        print('\nContacts:')
        print(contacts)
    elif choice == "1":
        add_contact(contacts)
    elif choice == "2":
        delete_contact(contacts)
    elif choice == '3':
        name = input('Enter name to view contact info: \n')
        view_single_contact(contacts, name)
    elif choice == '4':
        view_contacts_by_letter(contacts)
    elif choice == '5':
        name = input('Enter name to view contact info: \n')
        update_contact(contacts, name)
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        keep_asking = False
    else:
        print("Invalid choice. Please enter a number from 0-6.")
