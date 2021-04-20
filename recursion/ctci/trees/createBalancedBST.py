# create Balanced BST from sorted array
# problem 4.2

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
  
def createBST(l): 
  if(len(l) < 1):
    return

  mid = len(l)/2
  node = Node(l[mid])
  node.left = Node(l[:mid])
  node.right = Node(l[mid+1:])

def print_preorder(node):
  if not node:
    return
  print(node.val)
  print_preorder(node.left)
  print_preorder(node.right)
  

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
print('Inorder Traversal for tree')
print_preorder(root)
l = [1, 2, 3, 4, 5]
createBST(l)
