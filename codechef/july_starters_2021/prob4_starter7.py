# https://www.codechef.com/START7C/problems/CEILSUM
from sys import stdin
import math

t = int(stdin.readline())
while(t > 0):
  t -= 1
  x = [int(x) for x in stdin.readline().split()]
  a = x[0]
  b = x[1]

  if (a > b ) and (a + a-1)%2 != 0:
    x = a-1
  elif (a < b ) and (a + a+1)%2 != 0:
    x = a+1
  else:
    x = a

  print(math.ceil((b-x)/2) + math.ceil((x-a)/2))
