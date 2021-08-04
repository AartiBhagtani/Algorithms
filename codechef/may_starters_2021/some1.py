# https://www.codechef.com/START4C/problems/QUIZPLAG
from sys import stdin
t = int(stdin.readline())
while(t > 0):
  l = [int(x) for x in stdin.readline().split()]
  n = l[0]
  m = l[1]
  k = l[2]
  attempts = [int(x) for x in stdin.readline().split()]
  player_set = [0] * (n+1)
  ans = 0

  for i in attempts:
    if i <= n:
      player_set[i] += 1
  
  for i in player_set:
    if i > 1:
      ans += 1
  print(ans)
  t -= 1