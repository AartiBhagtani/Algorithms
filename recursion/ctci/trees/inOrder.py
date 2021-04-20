from sys import stdin

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

def printInorderTree(root):
  if(root == None):
    return
  printInorderTree(root.left)
  print(root.val)
  printInorderTree(root.right)
  
root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
printInorderTree(root)
printInorderTree(root)    