# Vertical order traversal of tree
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
# This is incorrect as order in a vertical line is not maintained 

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

hm = dict()
def generate_vertical_order(node, vertex):
  if node is None:
    return
  try:  
    hm[vertex].append(node.val)
  except:
    hm[vertex] = [node.val]
  generate_vertical_order(node.left, vertex-1)

  generate_vertical_order(node.right, vertex+1)


def print_vertical_order(node):
  generate_vertical_order(node, 0)
  for index, key in enumerate(sorted(hm)):
    for i in hm[key]:
      print(i, end = ' ')
    print()



root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
root.right.right = Node(10)
root.right.right.left = Node(11)
root.right.right.right = Node(12)
print_vertical_order(root)
