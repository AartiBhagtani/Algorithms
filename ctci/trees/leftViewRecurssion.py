# Left View of tree using recurssion

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
max_val = -1  
def print_left_view(node, curr, max_val):
  if node is None:
    return
  if curr > max_val:
    print(node.val)
    max_val = max(curr, max_val)
  print_left_view(node.left, curr + 1, max_val)
  print_left_view(node.right, curr + 1, max_val)
  
root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
root.right.right = Node(10)
root.right.right.left = Node(11)
root.right.right.right = Node(12)
print_left_view(root, 0, -1)
