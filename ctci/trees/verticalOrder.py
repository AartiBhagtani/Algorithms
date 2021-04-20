# Left View of tree using recurssion

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
  
def print_left_view(node, curr, max):
  
root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
root.right.right = Node(10)
root.right.right.left = Node(11)
root.right.right.right = Node(12)
print_left_view(root, 0, -1)
