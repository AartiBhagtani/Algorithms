# https://www.codechef.com/LTIME95C/problems/BENCHP
from sys import stdin
t = int(stdin.readline())
while(t > 0):
  t -= 1
  l_input = [int(x) for x in stdin.readline().split()]
  N = l_input[0]
  min_weight = l_input[1]
  rod_weight = l_input[2]
  l = [0]*100001
  weights = [int(x) for x in stdin.readline().split()]

  if rod_weight >= min_weight:
    print('YES')
    continue

  for i in range(N):
    val = weights[i]
    l[val] += 1
  
  i = 100001
  lift_weight = rod_weight
  flag = 'NO'
  while i >= 1: 
    i -= 1
    if l[i] > 1:
      if l[i] % 2 != 0:
        l[i] -= 1
      lift_weight += (i * l[i])
      if lift_weight >= min_weight:
        flag = 'YES'
        break
  print(flag)


  