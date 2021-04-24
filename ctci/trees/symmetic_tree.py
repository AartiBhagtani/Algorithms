class newNode:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

def isMirror(root1, root2):
      if root1 is None and root2 is None:
        return True
      if(root1 and root2 and root1.val == root2.val):
        return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
      return False
    
def isSymmetric(root) -> bool:
  if root is None:
    return True
  return isMirror(root.left, root.right)
      
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
print(isSymmetric(root))
