# https://www.codechef.com/START7C/problems/CHSFORMT
from sys import stdin

t = int(stdin.readline())
while(t > 0):
  t -= 1
  x = [int(x) for x in stdin.readline().split()]
  a = x[0]
  b = x[1]

  s = a+b
  if s < 3:
    print(1)
  elif s >= 3 and s <= 10:
    print(2) 
  elif s >= 11 and s <= 60:
    print(3)
  else:
    print(4)

