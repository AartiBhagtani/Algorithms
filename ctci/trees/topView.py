# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
# In O(nlogn) time

class newNode:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

hm = dict()
def generate_top_view_nodes(node, hd, level):
  if node is None:
    return
  if hd in hm:
    if level < hm[hd][1]:
      hm[hd] = [node.val, level]
  else:
      hm[hd] = [node.val, level]
  generate_top_view_nodes(node.left, hd-1, level+1)
  generate_top_view_nodes(node.right, hd+1, level+1)


def print_top_view(node):
  generate_top_view_nodes(node, 0, 0)
  for index, key in enumerate(sorted(hm)):
    print(hm[key][0], end = ' ')

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
print_top_view(root)
