# https://www.codechef.com/OCT21C/problems/ANDSUBAR
from sys import stdin
import math

t = int(stdin.readline())

while t > 0:
  t -= 1
  n = int(stdin.readline())
  print(math.ceil(n/2))
