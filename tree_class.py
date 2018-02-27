def run_code(code):
    exec(code)

class Tree:
    tree_count = 0
    all_trees = {}

    def __init__(self, label, branches):
        Tree.tree_count += 1
        self.tree_id = Tree.tree_count
        self.label = label
        self.branches = branches
        Tree.all_trees[self.tree_id] = self

    def __repr__(self):
        if self.is_leaf():
            return 'Tree({0})'.format(self.label)
        return 'Tree({0}, {1})'.format(self.label, [b for b in self.branches])

    def is_leaf(self):
        return not self.branches

    def add_branch(self, branch_label):
        new_branch = Tree(branch_label, [])
        self.branches += [new_branch]

    def delete(self, delete_id):
        deleted = Tree.all_trees[delete_id]
        [b.delete(b.tree_id) for b in deleted.branches]
        del Tree.all_trees[delete_id]
        if delete_id != self.tree_id:
            self.branches.remove(deleted)

    def replace_label(self, old, new):
        if self.label == old:
            self.label = new
        if not self.is_leaf():
            [b.replace_label(old, new) for b in self.branches]

    def print_tree(self, indent=0):
        print(' ' * indent + self.label)
        [b.print_tree(indent + 1) for b in self.branches]

    def vertical_levels(self, total=0):
        if self.is_leaf():
            return total + 1
        return max([b.vertical_levels(total + 1) for b in self.branches])

    def horizontal_levels(self):
        return len(self.branches)

#Tree("hello",[Tree("world",[Tree("god level",[]), Tree("achieved",[Tree("get on my level",[]), Tree("denero",[])])]), Tree("()(0.0)()",[])])