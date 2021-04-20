# Least common ancestor => not working
# approach 
# problem 4.8
class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
  
def LCA(node, data1, data2): 
  if node == None:
    return None
  l_tree = LCA(node.left, data1, data2)
  r_tree = LCA(node.right, data1, data2)
  if l_tree and r_tree and l_tree.val != data1 and r_tree.val != data1:
    return node.val
  if l_tree or r_tree:
    return node.val
  return None  

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
# root.left.right = Node(7)
# root.right = Node(3)
print(LCA(root, 2, 3))
