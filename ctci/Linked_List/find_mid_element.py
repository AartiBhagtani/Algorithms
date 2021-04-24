# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
# 2 pointer approach, move first pointer by 1 ele and second by 2 elements.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def findMid(self):
    first = self.head
    second = self.head
    while second and second.next:
      second = second.next
      second = second.next

      first = first.next
    return first.data

  def print_ll(self):
    node = self.head
    while node:
      print(node.data, end=' ')
      node = node.next

llist = LinkedList()
llist.head = Node(1)
second = Node(1)
third = Node(2)
fourth = Node(3)

llist.head.next = second
second.next = third
third.next = fourth

print(llist.findMid())
llist.print_ll()
