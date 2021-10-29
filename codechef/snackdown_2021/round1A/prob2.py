# https://www.codechef.com/SNCK1A21/problems/MINLCM1

from sys import stdin

t = int(stdin.readline())

while t > 0:
  t -= 1
  x, k = [int(x) for x in stdin.readline().split()]

  print(x * 2, end=" ")
  max = x * k
  print(max * (max-1))