# https://www.codechef.com/LTIME95C/problems/CCHEAVEN
from sys import stdin
import math

t = int(stdin.readline())
while(t > 0):
  life_length = int(stdin.readline())
  s = stdin.readline()
  g_deeds = 0
  b_deeds = 0
  flag = 'NO'
  if s[0] == '1':
    flag = 'YES'
  else: 
    for i in range(len(s)):
      if s[i] == '1':
        g_deeds += 1
      else:
        b_deeds += 1
      if g_deeds/(i+1) >= 0.5:
        flag = 'YES'
        break
  print(flag)

  t -= 1