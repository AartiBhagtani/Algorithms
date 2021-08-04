# https://www.codechef.com/LTIME95C/problems/ARRROT
from sys import stdin

n = stdin.readline()
l = [int(x) for x in stdin.readline().split()]
l_sum = sum(l)
q = int(stdin.readline())
all_queries = [int(x) for x in stdin.readline().split()]

while q > 0:
  l_sum = (l_sum * 2)%1000000007
  print(l_sum)
  q -= 1