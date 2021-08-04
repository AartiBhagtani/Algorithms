# https://www.codechef.com/MAY21C/problems/XOREQUAL
from sys import stdin
import math 

def mod2(x, n, m):
  if n == 0:
    return 1
  elif n%2 == 0:
    y = mod2(x, n/2, m)
    return (y*y)%m
  else:
    return ((x%m) * mod2(x, n-1, m))%m

t = int(stdin.readline())
while(t > 0):
  n = int(stdin.readline())
  ans = mod2(2, n, 2000000014)
  ans = ans // 2
  print(ans % 1000000007)

  t -= 1

