# Least common ancestor
# problem 4.8
class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

def LCA(node, data1, data2):
  if node == None:
    return None
  if node.val == data1 or node.val == data2:
    return node
  left = LCA(node.left, data1, data2)
  right = LCA(node.right, data1, data2)
  if(left and right):
    return node
  if left == None and right == None: 
    return None
  if left != None:
    return left
  else:
    return right

root = Node(1) 
root.left = Node(2)
root.left.left = Node(3)
# root.left.right = Node(7)
# root.right = Node(3)
print(LCA(root, 1, 2).val)
