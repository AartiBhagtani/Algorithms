# https://www.codechef.com/LTIME98C/problems/ARRT

from sys import stdin

t = int(stdin.readline())
while(t > 0):
  t -= 1
  n = int(stdin.readline())

  a = [int(x) for x in stdin.readline().split()]
  b = [int(x) for x in stdin.readline().split()]
  
  index = 0
  min_value = (a[0] + b[0])%n
  for i in range(len(a)):
    new_value = (a[0]+b[i]) % n
    if min_value == new_value:
      index2 = i
    if new_value < min_value:
      index = i
      min_value = new_value

  c = b
  c = c[index2:] + c[:index2]
  b = b[index:] + b[:index]

  list1 = []
  list2 = []

  for i in range(len(a)):
    list1.append((a[i]+b[i])%n)
    list2.append((a[i]+c[i])%n)
  
  if list2 <  list1:
    list1 = list2
  
  for i in range(len(a)):
    print(list1[i], end = ' ')