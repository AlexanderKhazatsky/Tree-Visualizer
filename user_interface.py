import tree_methods


while True:
    command = input("Please select from the options below:\n"
                    "1) Create a new tree\n"
                    "2) Edit an existing tree\n"
                    "3) Visualize a tree\n"
                    "4) Print a tree's code\n"
                    "5) Write code manually\n"
                    "6) Print existing trees\n"
                    "7) Quit\n"
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
        tree_methods.write_code()
    elif command == "6":
        tree_methods.print_trees()
    elif command == "7":
        print("Goodbye!")
        break
    else:
        print("Yikes! Command was not found...")

#Tree("hello",[Tree("world",[Tree("god level",[]), Tree("achieved",[Tree("get on my level",[]), Tree("denero",[])])]), Tree("()(0.0)()",[])])