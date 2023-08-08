import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def display_menu():
    print("**** Contact Management System ****")
    print("1. Add Contact")
    print("2. Search Contact by Name")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. View All Contacts")
    print("6. Exit")
    print("**********************************")

def is_valid_phone(phone):
    return len(phone) == 10 and phone.isdigit()

def is_valid_email(email):
    return '@' in email

def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        phone = input("Enter contact phone number (10 digits): ")
        email = input("Enter contact email address: ")

        if not is_valid_phone(phone) or not is_valid_email(email):
            print("Invalid phone number or email address. Please try again.")
            return

        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    name = input("Enter contact name to search: ")
    contact = contacts.get(name)
    if contact:
        print(f"Contact found:\nName: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone = input("Enter new phone number (10 digits): ")
        email = input("Enter new email address: ")

        if not is_valid_phone(phone) or not is_valid_email(email):
            print("Invalid phone number or email address. Please try again.")
            return

        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def view_all_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            view_all_contacts(contacts)
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
