# Left View of tree using level order traversal

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
  
def print_left_view(node):
  stack = []
  stack.append(node)
  while len(stack) > 0 :
    size_arr = len(stack)
    print(stack[0].val)
    while size_arr > 0 :
      # if size_arr == len(stack):
      #   print(ele[-1].val)
      ele = stack.pop(0)
      if ele.left:
        stack.append(ele.left)
      if ele.right:
        stack.append(ele.right)
      size_arr = size_arr - 1

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
root.right.right = Node(10)
# root.right.right.left = Node(11)
root.right.right.right = Node(12)
print_left_view(root)
