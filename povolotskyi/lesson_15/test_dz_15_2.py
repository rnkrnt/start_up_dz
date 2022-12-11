from dz_15_2 import Tree

#  У моїй реалізації классу Tree тільки функції min_value та max_value повертають значення

nodes = [8, 3, 15, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None, 12, 16, 17, 20, 18, 19]
tree = Tree(None)
tree.insert_list(nodes)

def test_min_value():
    assert  tree.min_value().id_node == 1

def test_max_value():
    assert  tree.max_value().id_node == 20