# print all possible arrays of a BST
#  ctci 4.9
class Node:
  def __init__(self, data):
  self.data = data
  self.left = self.right = None

def printArray(root):
  
root = Node(1)
root.right = Node(3)
root.right.left = Node(6)

printArray(root):
