# https://www.codechef.com/OCT21C/problems/MEXOR

from sys import stdin
import math

def allones(s):
  for i in s:
    if i == '0':
      return False
  return True


t = int(stdin.readline())

while t > 0:
  t -= 1
  x = int(stdin.readline())

  s = bin(x).replace('0b', '')
  if allones(s):
    print(x+1)
  else:
    temp = len(s)
    print(int(math.pow(2, temp-1)))