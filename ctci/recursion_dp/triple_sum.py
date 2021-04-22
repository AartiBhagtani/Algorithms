# https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/
# ctci 8.1

from sys import stdin

def find_step(n):
  if n == 1 or n == 0:
    return 1
  elif n == 2:
    return 2
  else:
    return find_step(n-3) + find_step(n-2) + find_step(n-1)

n = int(stdin.readline())
print(find_step(int(n)))

