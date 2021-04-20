# print level order traversal
# problem 4.3

class Node:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
  
def print_levelorder(node): 
  current = node
  q = []
  q.append(current)
  while len(q) > 0: 
    no_of_nodes_at_given_level = len(q)
    while no_of_nodes_at_given_level > 0:
      current = q.pop(0)
      print(current.val, end=' ')
      if current.left:
        q.append(current.left)
      if current.right:
        q.append(current.right)
      no_of_nodes_at_given_level -= 1
    print('')

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(3)
print('Level order Traversal for a tree')
print_levelorder(root)
