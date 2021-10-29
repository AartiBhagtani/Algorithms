# https://www.codechef.com/OCT21C/problems/MIXTURE
from sys import stdin

t = int(stdin.readline())
while t > 0:
  t -= 1
  a, b = [int(x) for x in stdin.readline().split()]

  if a == 0:
    print('Liquid')
  elif b == 0:
    print('Solid')
  else:
    print('Solution')
  