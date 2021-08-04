# https://www.codechef.com/LTIME95C/problems/EQUINOX

from sys import stdin
t = int(stdin.readline())
while t > 0:
  l = [int(x) for x in stdin.readline().split()]
  N = l[0]
  A = l[1]
  B = l[2]
  letters = ['E', 'Q', 'U', 'I', 'O', 'N', 'X']
  s_points = 0
  a_points = 0
  while N > 0: 
    game_string = stdin.readline()
    if game_string[0] in letters:
      s_points += A
    else:
      a_points += B
    N -= 1
  if s_points == a_points:
    print('DRAW')
  elif s_points > a_points:
    print('SARTHAK')
  else:
    print('ANURADHA')
  t -= 1  