# https://www.codechef.com/COOK131B/problems/MODEQUAL

from sys import stdin
import sys 

def add_ans(n, p, k):
  ans = 0
  ans += p//k
  if n%k != 0:
    if n%k < p%k: 
      ans += n%k
    else:
      ans += p%k
    
  return ans

t = int(stdin.readline())
while(t > 0):
  t -= 1
  a = [int(x) for x in stdin.readline().split()]
  n = a[0]
  p = a[1]
  k = a[2]
  ans = (n//k) * (p%k)
  ans += add_ans(n, p, k)
  print(ans + 1)