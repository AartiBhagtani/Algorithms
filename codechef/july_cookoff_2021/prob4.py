# https://www.codechef.com/COOK131B/problems/MODEQUAL

from sys import stdin
import sys 

t = int(stdin.readline())
while(t > 0):
  t -= 1
  n = int(stdin.readline())
  a = [int(x) for x in stdin.readline().split()]
  ans = 0
  flag = True
  first_min = a[0]
  for i in a:
    if i < first_min:
      first_min = i

  first_min_occurence = 0 
  for i in a:
    if i == first_min:
      first_min_occurence += 1
  
  if first_min == 0 or first_min_occurence == n:
    ans = n - first_min_occurence
    
  else:
    for i in a:
      if i != first_min and first_min != i % (i - first_min):
        flag = False
        break

  if flag:
    ans = n - first_min_occurence
  else:  
    ans = n
  print(ans)
  