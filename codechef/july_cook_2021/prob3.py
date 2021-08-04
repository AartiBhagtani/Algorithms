# https://www.codechef.com/LTIME98C/problems/BUTYPAIR
from sys import stdin
import math


def find_permutation(n, r):
  return n * (n - 1)

t = int(stdin.readline())
while(t > 0):
  t -= 1
  n = int(stdin.readline())
  a = [int(x) for x in stdin.readline().split()]

  if n == 1:
    print(0)
  else:
    elements_count = {}
    for i in a:
      if i in elements_count:
        elements_count[i] += 1
      else:
        elements_count[i] = 1
    
    count = 0
    same_keys = []
    for key, value in elements_count.items():
      if value != 1:
        same_keys.append(value)
        
    ans = find_permutation(n, 2)
    repetitions = 0

    for i in same_keys:
      repetitions += find_permutation(i, 2)

    print(ans - repetitions)
    