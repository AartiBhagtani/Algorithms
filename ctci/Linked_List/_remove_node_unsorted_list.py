# ----NOT DONE

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def removeDuplicates(self):
    if self.head:
      predecessor = None
      node = self.head
      prev = node
      node = node.next
      while node:
        duplicate_found = False
        while node and prev.data == node.data:
          prev.next = node.next
          node = node.next
          duplicate_found = True
        if duplicate_found:
          if predecessor:
            predecessor.next = prev.next
            prev.next = None
          else:
            self.head = prev.next
        else:
          # predecessor = prev
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
fourth = Node(1)

llist.head.next = second
second.next = third
third.next = fourth

llist.removeDuplicates()
llist.print_ll()