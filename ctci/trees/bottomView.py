# https://www.geeksforgeeks.org/bottom-view-binary-tree/

# In O(nlogn) time
class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

hm = dict()
def generate_bottom_view_nodes(node, hd, level):
  if node is None:
    return
  if hd in hm:
    if level >= hm[hd][1]:
      hm[hd] = [node.val, level]
  else:
      hm[hd] = [node.val, level]
  generate_bottom_view_nodes(node.left, hd-1, level+1)
  generate_bottom_view_nodes(node.right, hd+1, level+1)


def print_bottom_order(node):
  generate_bottom_view_nodes(node, 0, 0)
  for index, key in enumerate(sorted(hm)):
    print(hm[key][0], end = ' ')

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
print_bottom_order(root)
