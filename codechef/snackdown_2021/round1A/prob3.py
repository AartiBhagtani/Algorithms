# https://www.codechef.com/SNCK1A21/problems/EQBEAUTY

from sys import stdin
import math

t = int(stdin.readline())

while t > 0:
  t -= 1
  n = int(stdin.readline())
  x = [int(x) for x in stdin.readline().split()]
  if n == 2:
    print("0")
  elif n == 3:
    min_value = min(abs(x[0]-x[1]), abs(x[1]-x[2]))
    print(min(min_value, abs(x[0]-x[2])))
  else:
    # find 1st, 2nd min & max
    min1 = min(x)
    x.remove(min1)
    min2 = min(x)
    x.remove(min2)
    max1 = max(x)
    x.remove(max1)
    max2 = max(x)
    x.remove(max2)
    if (min1 == min2 and max1 == max2):
      print("0")
    else: 
      
      # logic with min max prob
      b1 = max1 - min2
      b2 = max2 - min1

      print("beauty 1")
      print(b1)
      print("beauty 2")
      print(b2)
      min_val = min(abs(b1-b2), b1)
      print(min(min_val, b2))


