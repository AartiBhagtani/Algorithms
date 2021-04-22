# wip
# https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/
# https://www.geeksforgeeks.org/power-set/
# ctci 8.4

from sys import stdin

def find_subsets(s):
  # s = sorted(s)
  l = []
  for i in range(0, len(s)+1):
    for j in range(i+1, len(s)):
      l.append(s[i:j])
  return l	

s = (stdin.readline())
ans = find_subsets(s)
print(len(ans))