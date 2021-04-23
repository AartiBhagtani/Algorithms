# remove nth node from LL from the end
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# https://www.geeksforgeeks.org/delete-nth-node-from-the-end-of-the-given-linked-list/

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def removeNode(self, n):
    first_pointer = self.head
    second_pointer = self.head
    while n > 0:
      second_pointer = second_pointer.next
      n -= 1
    if second_pointer == None:
      self.head = self.head.next
      return
    while second_pointer and second_pointer.next != None:
      first_pointer = first_pointer.next
      second_pointer = second_pointer.next
    first_pointer.next = first_pointer.next.next
    

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

llist.removeNode(1)
llist.print_ll()
