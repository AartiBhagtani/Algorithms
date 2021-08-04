# https://www.codechef.com/MAY21C/problems/TCTCTOE
from sys import stdin

def count_values(grid, val):
  count = 0
  for i in range(3):
    for j in range(3):
      if grid[i][j] == val:
        count += 1
  return count

def count_winners(grid):
  # horizontal
  winner_count = 0
  prev = '_'
  winner = []
  for i in range(3):
    prev = grid[i][0]
    if prev == '_':
      continue
    for j in range(3):
      if grid[i][j] == prev:
        prev = grid[i][j]
      else:
        break
    if j == 2 and prev == grid[i][j]:
      winner_count +=1 
      winner.append(prev)
  
  for i in range(3):
    prev = grid[0][i]
    if prev == '_':
      continue
    for j in range(3):
      if grid[j][i] == prev:
        prev = grid[j][i]
      else:
        break
    if j == 2 and prev == grid[j][i]:
      winner_count +=1 
      winner.append(prev)

  if grid[0][0] != '_' and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
    winner_count += 1
    winner.append(grid[0][0])

  if grid[0][2] != '_' and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
    winner_count += 1
    winner.append(grid[0][2])

  return [winner_count, winner]    

t = int(stdin.readline())
while(t > 0):
  t -= 1
  grid = []
  for a in range(3):
    i = stdin.readline()
    row = []
    for b in range(3):
      row.append(i[b])
    grid.append(row)
  
  x_count = count_values(grid, 'X')
  o_count = count_values(grid, 'O')
  dash_count = count_values(grid, '_')

  winner_count, winner = count_winners(grid)
  diff = x_count - o_count

  if not(diff == 1 or diff == 0):
    ans = 3

  elif winner_count > 2:
    ans = 3

  elif winner_count == 2 and winner[0] != winner[1]:
    ans = 3

  elif winner_count >= 1 and winner[0] == 'X' and diff == 0:
    ans = 3

  elif winner_count >= 1 and winner[0] == 'O' and diff == 1:
    ans = 3

  elif winner_count == 0 and dash_count > 0:
    ans = 2
  
  # elif winner_count == 1 or (winner_count == 0 and dash_count == 0):
  #   ans = 1

  else:
    ans = 1

  print(ans)
  