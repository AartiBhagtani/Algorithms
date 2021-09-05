# https://www.codechef.com/LTIME98C/problems/REDALERT

from sys import stdin

t = int(stdin.readline())
while(t > 0):
  t -= 1
  x = [int(x) for x in stdin.readline().split()]
  n = x[0]
  d = x[1]
  h = x[2]

  a = [int(x) for x in stdin.readline().split()]
  water_level = 0

  red_alert = False
  for i in a:
    if i > 0:
      water_level += i
    elif water_level-d < 0:
      water_level = 0
    else:
      water_level -= d
    if water_level > h:
      red_alert = True
      break
    
  if red_alert:
    print('YES')
  else:
    print('NO')
