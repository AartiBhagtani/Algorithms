# https://www.codechef.com/START7C/problems/FODCHAIN
from sys import stdin
import math

t = int(stdin.readline())
while(t > 0):
  t -= 1
  x = [int(x) for x in stdin.readline().split()]
  e = x[0]
  k = x[1]

  score = 0
  while e > 0:
    score += 1
    e = math.floor(e/k)
  
  print(score)