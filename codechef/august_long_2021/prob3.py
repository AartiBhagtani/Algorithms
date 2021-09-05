# https://www.codechef.com/COOK131B/problems/MODEQUAL

from sys import stdin
import sys 

t = int(stdin.readline())
while(t > 0):
  t -= 1
  a = [int(x) for x in stdin.readline().split()]
  n = a[0]
  p = a[1]
  k = a[2]
  ans = 0
  for i in range(n):
    for j in range(i, n, k):
      if j == p:
        break
      ans += 1
    if j == p:
      break
  print(ans + 1)
  