from collections import defaultdict
d = {}
days = [3,0,0,0,0,2]
apples = [3,0,0,0,0,2]

for i in range(len(days)):
  min_days = min(days[i], apples[i])
  start_day = i + 1
  for j in range(start_day, start_day+min_days):
    d[j] = 1
print(len(d))


