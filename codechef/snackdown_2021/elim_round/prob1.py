# https://www.codechef.com/SNCKQL21/problems/LUCKYNUM

from sys import stdin

t = int(stdin.readline())

while t > 0:
  t -= 1
  a, b, c = [int(x) for x in stdin.readline().split()]
  if a == 7 or b == 7 or c == 7:
    print('YES')
  else:
    print('NO')