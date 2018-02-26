import tree_methods


while True:
    command = input("Please select from the options below:\n"
                    "1) Create a new tree\n"
                    "2) Edit an existing tree\n"
                    "3) Visualize a tree\n"
                    "4) Print a tree's code\n"
                    "5) Quit\n"
                    "Option Number: ")

    if command == "1":
        tree_methods.create_tree()
    elif command == "2":
        tree_methods.edit_tree()
    elif command == "3":
        tree_methods.visualize_tree()
    elif command == "4":
        tree_methods.print_code()
    elif command == "5":
        print("Goodbye!")
        break
    else:
        print("Yikes! Command was not found...")