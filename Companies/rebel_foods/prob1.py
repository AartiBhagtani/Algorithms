# https://www.codechef.com/JULY21C/problems/MINNOTES
from sys import stdin
from math import gcd
t = int(stdin.readline())
while(t > 0):
  t -= 1
  n = int(stdin.readline())
  a = [int(x) for x in stdin.readline().split()]

  prefix_gcd = [0] * (len(a) + 2)
  suffix_gcd = [0] * (len(a) + 2)

  # compute prefix_gcd
  for i in range(1, len(a)+1):
    prefix_gcd[i] = gcd(prefix_gcd[i-1], a[i-1])

  # compute prefix_gcd
  for i in range(len(a), 1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i+1], a[i+1])
  print(suffix_gcd)