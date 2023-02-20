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

    def del_node(self, id_node):
        x = self.find_value(id_node)
        if x is None:
            return None
        elif not self:
            return None
        else:
            return self.__delete_search_parrent(id_node)

    def __delete_search_parrent(self, del_node, parrent_del_node=None):
        if del_node < self.id_node:
            return self.left.__delete_search_parrent(del_node, self)
        elif del_node > self.id_node:
            return self.right.__delete_search_parrent(del_node, self)
        elif del_node == self.id_node:
            return self.__delete_interpreter(self, parrent_del_node)
        else:
            return None

    def __delete_interpreter(self, del_node, parrent_del_node):
        if del_node.left is None and del_node.right is None:
            return del_node.__delete_leaf(del_node, parrent_del_node)
        elif del_node.left is None or del_node.right is None:
            return del_node.__delete_one_child(del_node, parrent_del_node)
        else:
            sr, pr = del_node.__find_min(del_node.right, del_node)
            del_node.id_node = sr.id_node
            del_node.__delete_one_child(sr, pr)


    def __delete_leaf(self, del_node, parrent_del_node):
        if parrent_del_node.left == del_node:
            parrent_del_node.left = None
        elif parrent_del_node.right == del_node:
            parrent_del_node.right = None
            return del_node
        else:
            return None

    def __delete_one_child(self, del_node, parrent_del_node):
        if parrent_del_node.left == del_node:
            if del_node.left is None:
                parrent_del_node.left = del_node.right
            else:
                parrent_del_node.left = del_node.left
        elif parrent_del_node.right == del_node:
            if del_node.left is None:
                parrent_del_node.right = del_node.right
            else:
                parrent_del_node.right = del_node.left
        else:
            return None

    def __find_min(self, node, parrent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parrent


# nodes = [8, 3, 15, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None, 12, 16, 17, 20, 18, 19]

# tree = Tree(None)
#
# tree.insert_list(nodes)
# # tree.print_tree()
#
# # print(tree.min_value())
# # print(tree.max_value())
#
# tree.del_node(1)
# tree.del_node(14)
# tree.del_node(8)
# tree.print_tree()