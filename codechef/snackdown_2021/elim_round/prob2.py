# https://www.codechef.com/SNCKQL21/problems/TESTSERIES

from sys import stdin

t = int(stdin.readline())

while t > 0:
  t -= 1
  a = [int(x) for x in stdin.readline().split()]
  i = e = d = 0
  for x in a:
    if x == 0:
      d += 1
    elif x == 1:
      i += 1
    else:
      e += 1
  
  if e > i:
    print('England')
  elif i > e:
    print('India')
  else:
    print('Draw')
  
