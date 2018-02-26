import tree_class


def input_validator(message, options, error_message="Yikes! Command was not found...", type=int):
    response = type(input(message))
    if response not in options:
        print(error_message)
        return input_validator(message, options, error_message)
    return response


def create_tree():
    print("You selected: Create a new tree")
    tree_class.Tree(input("Label: "))


def edit_tree():
    if len(tree_class.Tree.all_trees) == 0:
        print("You haven't created any trees yet")
        return

    print("You selected: Edit an existing tree")

    message = "ID of the tree you would like to edit: "
    options = list(tree_class.Tree.all_trees.keys())
    error_message = "Sorry! It doesn't look like this tree exists"

    tree_id = input_validator(message, options, error_message)
    tree_to_edit = tree_class.Tree.all_trees[tree_id]

    message = "Please select the change you would like to make to this tree:\n" \
              "1) Change a label\n" \
              "2) Add a branch\n" \
              "3) Delete a branch\n" \
              "4) Delete the tree\n" \
              "Option Number: "
    options = [1, 2, 3, 4]

    option = input_validator(message, options)

    if option == 1:
        print("You selected: Change a label")
        old = input("Old label: ")
        new = input("New label: ")
        tree_to_edit.replace_label(old, new)
    elif option == 2:
        print("You selected: Add a branch")
        branch_label = input("Label of new branch: ")
        tree_to_edit.add_branch(branch_label)
    elif option == 3:
        branch_id = int(input("ID of branch to delete: "))
        if branch_id not in [b.tree_id for b in tree_to_edit.branches]:
            print("This branch is not in the tree")
        else:
            tree_to_edit.delete(branch_id)
    elif option == 4:
        tree_to_edit.delete(tree_id)


def visualize_tree():
    if len(tree_class.Tree.all_trees) == 0:
        print("You haven't created any trees yet")
        return

    print("You selected: Visualize a tree")

    message = "ID of the tree you would like to visualize: "
    options = list(tree_class.Tree.all_trees.keys())
    error_message = "Sorry! It doesn't look like this tree exists"

    tree_id = input_validator(message, options, error_message)
    tree_to_visualize = tree_class.Tree.all_trees[tree_id]
    tree_to_visualize.print_tree()


def print_code():
    if len(tree_class.Tree.all_trees) == 0:
        print("You haven't created any trees yet")
        return
    print("You selected: Print a tree's code")

    message = "ID of the tree who's code you would like to print: "
    options = list(tree_class.Tree.all_trees.keys())
    error_message = "Sorry! It doesn't look like this tree exists"

    tree_id = input_validator(message, options, error_message)
    tree_to_print = tree_class.Tree.all_trees[tree_id]
    tree_to_print.print_code()
