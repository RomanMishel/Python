contacts_list = {
    "name" : "",
    "email" : "",
    "phone" : "",
}

user_input = input(str("Please choose action: \n1.Add Contact \n2.Show All Contacts \n.3Remove Contact \n4.Edit Contact \n5.Exit"))

def add_contact():
    contact_name = input(str("Enter a contact name: "))
    contact_email = input(str("Enter a contact email: "))
    contact_phone = input(str("Enter a contact phone: "))

    contacts_list.append(contact_name, contact_email, contact_phone)
    print("Contact Added!")

