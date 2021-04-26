# problem - https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/?currentPage=1&orderBy=hot&query=

from sys import stdin

l = [int(x) for x in stdin.readline().split()]
k = int(stdin.readline())
max_freq = float('-inf')

for i in range(len(l)):
  temp = k
  curr_freq = 0
  j = i

  while temp > 0 and j < len(l)-1:
    temp -= abs(l[j] - l[j+1])
    j += 1
    curr_freq += 1
  max_freq = max(curr_freq, max_freq)
