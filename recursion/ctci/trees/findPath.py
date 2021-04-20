# create Balanced BST from sorted array
# problem 4.2
class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
l = []  
def findParent(node, data): 
  if node == None:
    return False
  left_result = findParent(node.left, data)
  right_result = findParent(node.right, data)
  if left_result or right_result or node.val == data:
    l.append(node.val)
    return True

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(7)
root.left.right.right = Node(10)
root.right = Node(5)
findParent(root, 10)
print(l)