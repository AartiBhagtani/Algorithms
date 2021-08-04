# https://www.codechef.com/START7C/problems/MAXARXOR
from sys import stdin

t = int(stdin.readline())
while(t > 0):
  t -= 1
  inp = [int(x) for x in stdin.readline().split()]
  n = inp[0]
  k = inp[1]

  max_k =  (pow(2,n) - pow(2, n-1))
  if k > max_k:
    k = max_k

  print(k * 2 * (pow(2, n) - 1))