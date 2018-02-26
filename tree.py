import tkinter
from tkinter import *

import turtle as t           # Allows us to use turtles

wn = t.Screen()      # Creates a playground for turtles

#setting title
t.title ('Trees!')
t.speed(0)

trees = {}  # All trees

class Tree:

    def __init__ (self, label, tree_id, branches=[]):
        self.label = label
        self.tree_id = tree_id
        for branch in branches:
            assert(isinstance(branch, Tree))
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(repr(self.label), repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def delete_child(self, child):
        assert(isinstance(child, Tree))
        try:
            self.branches.remove(child)
        except:
            print('{0} not found in the tree'.format(child))

    def add_child(self, child):
        assert(isinstance(child, Tree))
        print('Tree ID: ', self.tree_id)
        self.branches.append(child)


def draw_leaf(label, position, radius=50):
    """Draws a circle with label written in the middle of it."""
    t.goto(*position)
    # FIXME: if text size is greater than 16 it goes out of the circle
    text_size =  18 // len(label) + 12
    print(text_size)
    t.color('Dark Blue')
    t.begin_fill()
    t.down()
    t.circle(radius,extent=None, steps=100)
    t.end_fill()
    t.up()
    t.hideturtle()
    t.penup()
    t.color('yellow')
    t.goto(position[0], position[1]+radius-(text_size//2))
    t.write(label, align='center', font = ('Times New Roman', text_size))
    t.goto(position[0], position[1])


def draw_tree():
    """Draws the tree in Turtle"""
    return None
# tree_created = {'parent':[label,0,self], 'children': [label,id, parent]}
tree_created = None
tree_id = 0

def add():
    global tree_id, tree_created

    def check_branch(tree, entered_id, curr_id):
        """ Returns a True if tree was added else False"""
        for b in tree.branches:
            if b.tree_id == entered_id:
                b.add_child(add_tree(curr_id))
                return True
            elif check_branch(b, entered_id, curr_id):
                return True
        return False

    def add_tree(curr_id):
        ''' creates a tree and returns it. '''
        label = input('Label: ')
        try:
            label = float(label)
            f_or_i = None
            while  f_or_i != 'f' and f_or_i != 'i':
                f_or_i = input('would you like to make this a float or an int (f/i)')
                if f_or_i.lower() == 'i':
                    label = int(label)
                elif f_or_i.lower() != 'f':
                    print('Please type (f) for float or (i) for int')
                f_or_i == f_or_i.lower()
        except:
            label = str(label)
        return Tree(label, curr_id)

    if tree_created:

        if tree_created.branches:
            entered_id = None
            while entered_id == None:
                try:
                    entered_id = input('Which tree would you like to delete (enter ID): ')
                    if entered_id.lower() == 'cancel':
                        return
                    entered_id = int(entered_id)
                except:
                    print("please enter a valid id or cancel: ")
            print('entered id: ', entered_id) #debugging purposes.
        else: entered_id = 0

        if entered_id == 0:
            tree_created.add_child(add_tree(tree_id))
            tree_id += 1
            return

        if check_branch(tree_created, entered_id, tree_id):
            tree_id += 1
    else:
        tree_created = add_tree(tree_id)
        tree_id += 1


def delete():
    global tree_created, tree_id

    def confirm(t):
        print('Are you sure you want to delete this entire tree? (y/n)')
        print_tree(t)
        confirm = input().strip()
        if confirm.lower() == 'y':
            return True
        else:
            print('The tree was not deleted')
            return False

    def check_branch(tree, entered_id):
        """checks branchs of tree and deletes the tree if it is there"""
        for b in tree.branches:
            if b.tree_id == entered_id:
                if confirm(b):
                    tree.delete_child(b)
                else:
                    return
            else:
                check_branch(b, entered_id)
        return



    if tree_created:
        if tree_created.branches:
            entered_id = None
            while entered_id == None:
                try:
                    entered_id = input('Which tree would you like to delete (enter ID): ').strip()
                    if entered_id.lower() == 'cancel':
                        return
                    entered_id = int(entered_id)
                except:
                    print("please enter a valid id or cancel: ")
            print('entered id: ', entered_id) #debugging purposes.
        else: entered_id = 0

        if not entered_id:
            if confirm(tree_created):
                tree_created = None
                tree_id = 0
        else:
            check_branch(tree_created, entered_id)


    else:
        print('Error. No tree to delete')


def edit():
    global tree_id, tree_created

    def change_label(t):
        print('Old label: ', t.label)
        new_label = input('Input new label: ')
        try:
            new_label = float(new_label)
            f_or_i = None
            while  f_or_i != 'f' and f_or_i != 'i':
                f_or_i = input('would you like to make this a float or an int (f/i)')
                if f_or_i.lower() == 'i':
                    new_label = int(new_label)
                elif f_or_i.lower() != 'f':
                    print('Please type (f) for float or (i) for int')
                f_or_i == f_or_i.lower()
        except:
            new_label = str(new_label)
        t.label = new_label

    def check_branch(tree, entered_id):
        """ changes label"""
        for b in tree.branches:
            if b.tree_id == entered_id:
                change_label(b)

            else: check_branch(b, entered_id)

        return

    if tree_created:
        if tree_created.branches:
            entered_id = None
            while entered_id == None:
                try:
                    entered_id = input('Which tree would you like to edit (enter ID): ').strip()
                    if entered_id.lower() == 'cancel':
                        return
                    entered_id = int(entered_id)
                except:
                    print("please enter a valid id or cancel: ")
            print('entered id: ', entered_id) #debugging purposes.
        else: entered_id = 0

        if entered_id == 0:
            change_label(tree_created)
        else:
            check_branch(tree_created, entered_id)



def create_tree():
    global tree_id, tree_created
    def parse_tree(code):
        global tree_id
        if 'Tree' not in code:
            print('Formating Tree incorrectly. \nPlease format Tree(label, [Tree(....)])')
            return
        code = code.strip('Tree(')
        comma_index = code.find(',')

        print(code[0])
        has_quote = False
        if "'" == code[0]:
            code = code[1::]
            end_quote = code.find("'")
            label = code[:end_quote]
            has_quote = True

        if comma_index == -1:
            if not has_quote:
                label = code.strip(')')
                try:
                    if '.' in label:
                        label = float(label)
                    else:
                        label = int(label)
                except:
                    print('Invalid literal')
                    return
            try:
                t, tree_id = Tree(label, tree_id), tree_id + 1
            except:
                print('Formating Tree incorrectly. \nPlease format Tree(label, [Tree(....)])')
                return
            return t

        if not has_quote:
            label = code[:comma_index]
            try:
                if '.' in label:
                    label = float(label)
                else:
                    label = int(label)
            except:
                print('Invalid literal')
                return

        children = []
        children_str = code[comma_index+1:].strip().strip('[').strip().strip(')').strip(']') #FIXME: clean it up
        while children_str:
            nested = children_str.find(']')
            if nested == -1:
                several = children_str.find(',')
                if several == -1:
                    children.append(parse_tree(children_str))
                    children_str = ''
                else:
                    child = children_str[:several]
                    children_str = children_str[several+1:]
                    children.append(parse_tree(child))
            else:
                child = parse_tree(children_str[:nested+2])
                children_str = children_str[nested+2:].strip(',').strip()
                children.append(child)

        try:
            t, tree_id = Tree(label, tree_id, children), tree_id + 1
        except:
            print('Formating Tree incorrectly. \nPlease format Tree(label, [Tree(....)])')
            return
        return t
    tree = input('input tree code: ')
    tree_id = 0
    tree_created = parse_tree(tree)


def print_tree(t = tree_created, indent=0):
    print(t)
    print(t.branches)
    if t:
        print('  ' * indent + str(t.label))
        [print_tree(branch, indent + 1) for branch in t.branches]

def print_code():
    print(tree_created)

def print_treeID(t, indent=0):
    if t:
        print((' ' * indent) + str(t.tree_id))
        for b in t.branches:
            print_treeID(b, indent + 1)
    else:
        print('no tree')



while True:
    command = input("Please enter the number of your desired computation"
                    "1) Create new tree\n"
                    "2) Edit an existing tree\n"
                    "3) Print a tree\n"
                    "4) Print a tree's code\n"
                    "5) Quit")

    if command == "1":
        #create_tree()
        print()
    elif command == "2":
        #edit_tree(ID)
        print()
    elif command == "3":
        #print_tree(ID)
        print()
    elif command == "4":
        #print_code(ID)
        print()
    elif command == "5":
        print("Goodbye!")
        break
    else:
        print("Yikes! Command was not found...")

    draw_tree()



create_tree()




# while True:
#     label = input()
#     xpos = input('x: ')
#     ypos =  input('y: ')
#     position = [int(xpos), int(ypos)]
#     draw_leaf(label, position)
#     if label == 'null':
#         break
# wn.mainloop()             # Wait for user to close window

#  # Begin the fill process.
# # "Pen" down?
# for i in range(squares):  # For each edge of the shape
#     turtle.forward(40) # Move forward 40 units
#     turtle.left(angle) # Turn ready for the next edge
# turtle.up() # Pen up
# turtle.end_fill()
