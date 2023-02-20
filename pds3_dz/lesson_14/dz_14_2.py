class Tree:
    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if id_node is None:
            return None
        elif self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node)
        if self.right:
            self.right.print_tree()

    def insert_list(self, lis):
        for index in range(len(lis)):
            self.insert(lis[index])

    def min_value(self):
        if self.left:
           return self.left.min_value()
        else:
            return self

    def max_value(self):
        if self.right:
           return self.right.max_value()
        else:
           return self

    def find_value(self, id_node):
        if self.id_node is None:
            x = None
        elif id_node < self.id_node:
            if self.left is None:
                x = None
            else:
                x = self.left.find_value(id_node)
        elif id_node > self.id_node:
            if self.right is None:
                x = None
            else:
                x = self.right.find_value(id_node)
        elif id_node == self.id_node:
            x = self.id_node
        else:
            x = None
        return x



nodes = [8, 3, 15, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None, 12, 16, 17, 20, 18, 19]

tree = Tree(None)

tree.insert_list(nodes)
# tree.print_tree()

print(tree.min_value())
print(tree.max_value())