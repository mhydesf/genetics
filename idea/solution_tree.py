import os
from anytree import Node
from anytree.exporter import DotExporter

root = Node("*")
left = Node("x", parent=root)
right = Node("+", parent=root)
left_left = Node("y", parent=right)
right_right = Node("/", parent=right)
r_r_l = Node("a", parent=right_right)
r_r_r = Node("b", parent=right_right)

DotExporter(root).to_dotfile("solution_tree.dot")
os.system("dot -Tpng solution_tree.dot -o ../img/solution_tree.png")
