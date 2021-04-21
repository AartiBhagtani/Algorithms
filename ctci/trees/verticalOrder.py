# Vertical order traversal of tree
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-3/

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

def generate_vertical_order(node):
  if node is None:
    return
  hm = dict()

  hd_node = dict()
  q = []
  q.append(node)
  hd_node[node] = 0
  while len(q) > 0:
    size_q = len(q)
    while size_q > 0:
      ele = q.pop(0)
      hd = hd_node[ele]
      if hm.get(hd) is None:
        hm[hd] = []
      hm[hd].append(ele.val)
      if ele.left:
        hd_node[ele.left] = hd_node[ele] - 1
        q.append(ele.left)
      if ele.right:
        hd_node[ele.right] = hd_node[ele] + 1
        q.append(ele.right)
      size_q -= 1
  for index, key in enumerate(sorted(hm)):
    for i in hm[key]:
      print(i, end = ' ')
    print()


# def print_vertical_order(node):
  # generate_vertical_order(node)
  # 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)
generate_vertical_order(root)
