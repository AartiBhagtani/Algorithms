# https://www.codechef.com/LTIME98C/problems/CHFSPL

from sys import stdin

t = int(stdin.readline())
while(t > 0):
  t -= 1
  x = [int(x) for x in stdin.readline().split()]
  
  x.sort()

  print(x[2] + x[1])