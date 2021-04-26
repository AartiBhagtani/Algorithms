# https://www.geeksforgeeks.org/window-sliding-technique/
# with this technique we are reducing O(n^2) complexity of problem to O(n) problem.

from sys import stdin

l = [int(x) for x in stdin.readline().split()]
k = int(stdin.readline())

curr_sum = max_sum = sum(l[:k])
for i in range(k, len(l)):
  curr_sum += l[i]
  curr_sum -= l[i-k]
  max_sum = max(max_sum, curr_sum)

print(max_sum)
  