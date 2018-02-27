import turtle as t
wn = t.Screen()
width = 1000
height = 1000
t.setworldcoordinates(0, 0, width, height)

t.title("Trees!")
t.speed(5)


class Node:
    def __init__(self, label, x, y, radius=50):
        self.label = label
        self.x_pos = x
        self.y_pos = y
        self.radius = radius


class Screen:
    def __init__(self, w, h, x_adjuster=0):
        self.width = w
        self.height = h
        self.x_adjuster = x_adjuster


def draw_tree(tree_structure):
    y_slices = height / tree_structure.vertical_levels()
    starting_screen = Screen(width, height, 0)
    calculate_node(tree_structure, None, y_slices, starting_screen)
    t.reset()


def calculate_node(curr_tree, parent_node, y_slices, curr_screen, radius=50):
    x_pos = curr_screen.width / 2 + curr_screen.x_adjuster
    y_pos = curr_screen.height - 2 * radius

    tree_node = Node(curr_tree.label, x_pos, y_pos, radius)

    draw_node(tree_node)

    if curr_tree.branches:
        level_elements = curr_tree.horizontal_levels()
        new_width = curr_screen.width / level_elements
        new_height = curr_screen.height - y_slices
        horizontal_index = 0
        for b in curr_tree.branches:
            new_x_adjuster = curr_screen.x_adjuster + horizontal_index * new_width
            new_screen = Screen(new_width, new_height, new_x_adjuster)
            calculate_node(b, tree_node, y_slices, new_screen, radius)
            horizontal_index += 1

    if parent_node:
        t.goto(parent_node.x_pos, parent_node.y_pos)


def draw_node(node):
    if t.pos() == (0.0, 0.0):
        t.penup()
    else:
        t.pendown()
    t.goto(node.x_pos, node.y_pos + 2 * node.radius)
    t.goto(node.x_pos, node.y_pos)
    text_size = 18 // len(node.label) + 12
    t.color('Dark Blue')
    t.begin_fill()
    if not t.isdown():
        t.pendown()
    t.circle(node.radius, extent=None, steps=100)
    t.end_fill()
    t.penup()
    t.color('yellow')
    t.goto(node.x_pos, node.y_pos + node.radius - (text_size // 2))
    t.write(node.label, align='center', font=('Times New Roman', text_size))
    t.goto(node.x_pos, node.y_pos)
    t.color('black')
