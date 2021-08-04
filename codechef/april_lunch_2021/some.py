# https://www.codechef.com/LTIME95C/problems/SLOOP
from sys import stdin
t = int(stdin.readline())
while(t > 0):
  l = [int(x) for x in stdin.readline().split()]
  m = l[0]
  s = l[1]
  print(int(m/s))
  t -= 1