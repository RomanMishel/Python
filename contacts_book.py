contacts_list = {}


def add_contact():
    contact_name = input("Enter a contact name: ")
    contact_email = input("Enter a contact email: ")
    contact_phone = input("Enter a contact phone: ")

    contacts_list[contact_name] = {
        "email": contact_email,
        "phone": contact_phone,
    }

    print("Contact added!")


def show_contacts():
    if not contacts_list:
        print("Contacts list is empty.")
        return

    for name, contact in contacts_list.items():
        print(f"Name: {name}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print()


def remove_contact():
    contact_name = input("Enter a contact you want to delete: ")

    if contact_name in contacts_list:
        del contacts_list[contact_name]
        print("Contact deleted!")
    else:
        print("Contact not found.")


def edit_contact():
    contact_name = input("Enter contact name to edit: ")

    if contact_name not in contacts_list:
        print("Contact not found!")
        return

    print("1. Edit email")
    print("2. Edit phone")
    choice = input("What do you want to edit? ")

    if choice == "1":
        new_email = input("Enter new email: ")
        contacts_list[contact_name]["email"] = new_email
        print("Email updated!")
    elif choice == "2":
        new_phone = input("Enter new phone: ")
        contacts_list[contact_name]["phone"] = new_phone
        print("Phone updated!")
    else:
        print("Wrong choice!")


def exit_menu():
    print("Goodbye")


def main():
    while True:
        user_input = input(
            "Please choose action:\n"
            "1. Add Contact\n"
            "2. Show All Contacts\n"
            "3. Remove Contact\n"
            "4. Edit Contact\n"
            "5. Exit\n"
        )

        if user_input == "1":
            add_contact()
        elif user_input == "2":
            show_contacts()
        elif user_input == "3":
            remove_contact()
        elif user_input == "4":
            edit_contact()
        elif user_input == "5":
            exit_menu()
            break
        else:
            print("Could not find the operation you chose.")


if __name__ == "__main__":
    main()
