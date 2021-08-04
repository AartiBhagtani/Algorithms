# https://www.codechef.com/START6C/problems/ETUP
from sys import stdin
from itertools import combinations

def find_states(a, index, index_2=0):
  print("index ")
  print(index)
  comb = combinations(range(index), 2)
  k = index
  if index_2 != 0:
    k = index_2
  score = 0
  for list_i in comb:
    print("comb ")
    print(list_i)
    i = list_i[0]
    j = list_i[1]
    score += check_valid(a[i], a[j], a[k])
    print("score")
    print(score)
  return score

def check_valid(i, j, k):
  print(i, j, k)
  odd_count = 0
  if i < j < k:
    if i % 2 != 0:
      odd_count += 1
    if j % 2 != 0:
      odd_count += 1
    if k % 2 != 0:
      odd_count += 1
    if odd_count == 0 or odd_count == 2:
      return 1
  return 0

t = int(stdin.readline())
while(t > 0):
  t -= 1
  x = [int(x) for x in stdin.readline().split()]
  q = x[1]
  a = [int(x) for x in stdin.readline().split()]

  # form dp_states
  dp = [0] * len(a)
  for i in range(2, len(a)):
    dp[i] = dp[i-1] + find_states(a, i)

  r_dp = [0] * len(a)
  for i in range(len(a)-2, -1):
    r_dp[i] = r_dp[i+1] + find_states(a, i)

  print(dp)
  for i in range(q):
    score = 0
    l_r = [int(x) for x in stdin.readline().split()]
    l = l_r[0] - 1
    r = l_r[1] - 1
    if r - l >= 2:
      if l == 0:
        score = dp[r]
      else:
        score = dp[r] - r_dp[l]
    print(score)

