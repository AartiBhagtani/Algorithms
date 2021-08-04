# https://leetcode.com/problems/palindrome-linked-list/ 
# ctci
# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/

class Node:
  def __init__(self, data):
    self.data = data  
    self.next = None

def find_mid(head):
  count = 0
  first = head
  second = head
  while second and second.next:
    second = second.next
    second = second.next

    first = first.next
    count += 1
  return [first, count]

def reverse_LL(head):
  first = None
  second = head
  while second != None:
    temp = second.next
    second.next = first
    first = second
    second = temp
  return first


def checkPalindrome(node):
  mid_element, is_even = find_mid(node)
  if is_even % 2 != 0: 
    mid_element = mid_element.next

  reversed_LL_node = reverse_LL(mid_element)
  temp = reversed_LL_node
  if not temp and node.data != node.next.data:
    print(False)
    return
    
  while temp:
    # print
    if node.data != temp.data:
      print(False)
      return
    node = node.next
    temp = temp.next
  print(True)
  return

def printLinkedlist(node):
  while node:
    print(node.data)
    node = node.next

one = Node(1)   
two = Node(0)
three = Node(3)
four = Node(4)
five = Node(0)
six = Node(1)
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six

checkPalindrome(one)