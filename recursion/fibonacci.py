from sys import stdin

n = int(stdin.readline())

f = 0
s = 1
print(f)
print(s)
for i in range(n-2):
  t = f + s
  print(t)
  f = s
  s = t