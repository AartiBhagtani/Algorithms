# check if given binary tree is BST
#  ctci 4.5
class Node:
  def __init__(self, val):
    self.val = val
    self.left = self.right = None

def checkBST(root, min, max):
  if root is None:
    return True
  if root.val < min or root.val > max:
    return False
  return checkBST(root.left, min, root.val) and checkBST(root.right, root.val, max)

root = Node(5)
root.left = Node(1)
root.right = Node(6)

print(checkBST(root, float('-inf'), float('inf')))