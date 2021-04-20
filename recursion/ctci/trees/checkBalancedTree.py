# check if tree is balanced or not h(lefttree) - h(righttree) > 0
#  ctci 4.4
class Node:
  def __init__(self, data):
  self.data = data
  self.left = self.right = None

class Height:
	def __init__(self):
		self.height = 0

def isBalanced(root):
  if root is None:
    return 0
  lh = isBalanced(root.left)
  rh = isBalanced(root.right)
  # checking if the subtree is ever false then returning
  # false for the whole recursion
  if lh is False or rh is False:
    return False
  if abs(lh-rh) > 1:
      # returning false if subtree is not balanced
    return False
  else:
    # returning height if subtree is balanced
    return max(lh, rh)+1

root = Node(1)
root.right = Node(3)
root.right.left = Node(6)

if isBalanced(root):
	print('Tree is balanced')
else:
	print('Tree is not balanced')
