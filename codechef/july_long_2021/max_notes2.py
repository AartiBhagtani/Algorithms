# https://www.codechef.com/JULY21C/problems/MINNOTES
from sys import stdin
from math import gcd
t = int(stdin.readline())
while(t > 0):
  t -= 1
  n = int(stdin.readline())
  a = [int(x) for x in stdin.readline().split()]

  prefix_gcd = [0] * (n + 2)
  suffix_gcd = [0] * (n + 2)

  
  # compute prefix_gcd
  prefix_gcd[1] = a[0]
  for i in range(2, n+1):
    prefix_gcd[i] = gcd(prefix_gcd[i-1], a[i-1])

  # compute postfix_gcd
  suffix_gcd[n] = a[n-1]
  for i in range(n-1, 0, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i+1], a[i-1])

  # print(prefix_gcd)
  # print(suffix_gcd)
  
  max_gcd = 0
  index = 0
  if suffix_gcd[2] > prefix_gcd[n-1]:
    max_gcd = suffix_gcd[2]
    index = 0
  else:
    max_gcd = prefix_gcd[n-1]
    index = n-1


  for i in range(2, n):
    # max_gcd = max(max_gcd, gcd(prefix_gcd[i-1], suffix_gcd[i+1]))
    gcd_i = gcd(prefix_gcd[i-1], suffix_gcd[i+1])
    if gcd_i > max_gcd:
      max_gcd = gcd_i
      index = i
  # print(max_gcd)
  notes = 0
  # print(index)
  for i in range(n):
    if i == index:
      notes += 1
    else:
      notes += a[i]/max_gcd

  print(int(notes))