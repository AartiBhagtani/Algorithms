# https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/
# ctci 8.1

from sys import stdin

# def find_step(n):
#   if n == 1 or n == 0:
#     return 1
#   elif n == 2:
#     return 2
#   elif memo[n] > -1:
#     return memo[n]
#   else:
#     print(n)
#     memo[n] = find_step(n-1) + find_step(n-2) + find_step(n-3)

def find_step_2(n):
  for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
  return memo[n]  

n = int(stdin.readline())
memo = [-1]*(n+1)
memo[0] = 1
memo[1] = 1
memo[2] = 2
# find_step(n)
# print(memo)
print(find_step_2(n))

