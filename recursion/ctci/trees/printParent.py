# print successor or parent of given node
# ctci 4.6

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def printSuccessor(node, data):
  if node is None:
    return None
  if (node.left and node.left.val == data) or (node.right and node.right.val == data):
    return node
  l_subtree = printSuccessor(node.left, data)
  r_subtree = printSuccessor(node.right, data)
  return l_subtree if l_subtree else r_subtree
  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6) 
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(printSuccessor(root, 7).val)