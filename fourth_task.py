def parse_input(user_input):

    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

#Add new contact to dictionary of contacts
def add_contact(args, contacts):
    if len(args) !=2:
        return "Please write both name and phone number"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#Change phone number for excisitng contact
def change_contact(args, contacts):
    if len(args) !=2:
        return "Please provide both name and phone number"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact is not found."
    
#Demonstrate phonenumber for specific contact
def show_phone(args, contacts):
    if len(args) != 1:
        return "Please write the name"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact is not found."
    
#Demonstrate all saved contacts
def show_all(contacts):
    if not contacts:
        return "No contacts are found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

#Adding comands for bot
def main():
    contacts = {}
    print("Welcome to assistant bot")
    while True:
        user_input = input("Enter a command:")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("See you soon!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__== "__main__":
    main()