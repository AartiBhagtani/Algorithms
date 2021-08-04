# https://www.codechef.com/MAY21C/problems/SOLBLTY
from sys import stdin
t = int(stdin.readline())
while(t > 0):
  l = [int(x) for x in stdin.readline().split()]
  x = l[0]
  a = l[1]
  b = l[2]

  ans = a + (100-x)*b

  print(ans*10)
  t -= 1