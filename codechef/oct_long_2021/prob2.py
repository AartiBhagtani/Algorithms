# https://www.codechef.com/OCT21C/problems/THREEBOX
from sys import stdin

t = int(stdin.readline())

while t > 0:
  t -= 1
  a = [int(x) for x in stdin.readline().split()]

  if a[0]+a[1]+a[2] <= a[3]:
    print('1')
  elif a[0]+a[1] <= a[3]:
    print('2')
  else:
    print('3')
