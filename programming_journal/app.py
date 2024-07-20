from database   import add_entry, get_entries, create_table, get_user


menu = """Please select one of the following options:
1) Add a new entry for today.
2) View entries.
3) Get User
4) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"


def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"\n{entry[1]}: {entry[0]}\n\n")


print(welcome)

create_table()


while (user_input := input(menu)) != "4":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    elif user_input == "3":
        username = input("Enter username: ")
        view_entries(get_user(username))
    else:
        print("Invalid option")