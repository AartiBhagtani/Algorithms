from sys import stdin

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

stack = []

def printPreorder(root):
  stack = []
  current = root
  stack.append(current)
  while len(stack) > 0:
    current = stack.pop()
    print(current.val)
    if current.right != None:
      stack.append(current.right)
    if current.left != None:
      stack.append(current.left)
  return

def printInorder(root):
  current = root
  if current == None and len(stack) == 0:
    return 
  while(current != None):
    stack.append(current)
    current = current.left
  if current == None and len(stack) > 0:
    current = stack.pop()
    print(current.val)
    current = current.right
    printInorder(current)

def printPostorder:
# post order using hashset
  

def printPostorder2:
# post order using 2 stacks

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
print('Inorder Traversal for tree')
printInorder(root)
print('Preorder Traversal for tree')
printPreorder(root)
print('Postorder Traversal for tree')
printPostorder(root)