# print ancestor nodes (path) or parent of given node
# ctci 4.6

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def printAncestorNodes(node, data):
  if node is None:
    return False
  l_subtree = printAncestorNodes(node.left, data)
  r_subtree = printAncestorNodes(node.right, data)
  if l_subtree:
    print(node.val)
    return True
  if r_subtree:
    print(node.val)
    return True
  if node.val == data:
    return True
  return False
  # return l_subtree if l_subtree else r_subtree
  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6) 
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(printAncestorNodes(root, 6))
