# https://www.codechef.com/MAY21C/problems/LKDNGOLF
from sys import stdin
t = int(stdin.readline())
while(t > 0):
  t -= 1
  l = [int(x) for x in stdin.readline().split()]
  n = l[0]
  x = l[1]
  k = l[2]
  flag = False

  if x > n+1:
    print('NO')
    continue
  
  # forward pass
  if x % k == 0: 
    flag = True
  
  # backward pass
  if not flag:
    if x % k == (n+1) % k: 
      flag = True

  # print result
  if flag: 
    print('YES')
  else:
    print('NO')
  