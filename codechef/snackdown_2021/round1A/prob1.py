# https://www.codechef.com/SNCK1A21/problems/DANCEMOVES

from sys import stdin
import math

t = int(stdin.readline())

while t > 0:
  t -= 1
  x, y = [int(x) for x in stdin.readline().split()]
  if y <= x:
    print(x-y)
  else:
    diff = y - x
    if (diff % 2) == 0:
      print(int(diff/2))
    else:
      print(math.ceil(diff/2) + 1)
