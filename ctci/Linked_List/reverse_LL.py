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

  def reverseLL(self):
    first = None
    second = self.head
    while second != None:
      temp = second.next
      second.next = first
      first = second
      second = temp
    self.head = first

  def print_ll(self):
    node = self.head
    while node:
      print(node.data, end=' ')
      node = node.next

llist = LinkedList()
llist.head = Node(1)
second = Node(0)
third = Node(4)
fourth = Node(0)

llist.head.next = second
second.next = third
third.next = fourth

llist.reverseLL()
llist.print_ll()
