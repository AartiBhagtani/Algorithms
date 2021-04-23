# remove duplicates from sorted LL completely print only remaining distinct elements
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def removeDuplicates(self):
    if self.head:
      node = self.head
      prev = node
      node = node.next
      while node:
        if prev.data == node.data:
          prev.next = node.next
        else:
          prev = node
        node = node.next

  def print_ll(self):
    node = self.head
    while node:
      print(node.data, end=' ')
      node = node.next

llist = LinkedList()
llist.head = Node(1)
second = Node(1)
third = Node(1)
fourth = Node(2)

llist.head.next = second
second.next = third
third.next = fourth

llist.removeDuplicates()
llist.print_ll()
