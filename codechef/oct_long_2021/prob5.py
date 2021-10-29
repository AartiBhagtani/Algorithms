# https://www.codechef.com/OCT21C/problems/DIGITREM

from sys import stdin

t = int(stdin.readline())

while t > 0:
  t -= 1
  n, d = [x for x in stdin.readline().split()]

  # if d is not present
  if n.find(d) == -1:
    print('0')
    continue

  int_d = int(d)
  int_n = int(n)
  
  # if d is 0
  if int_d == 0: 
    new_n = n.replace("0", "1")
    print(int(new_n) - int(n))
    continue
  
  if int_d == 9:
    n = [int(x) for x in n]
    new_n = [0] * len(n)
    for i in range(len(n)-1, -1, -1):
      if n[i] == int_d:
        if i == len(n)-1:
          new_n[i] = 1 
        else:
          # print((10 - new_n[i+1]))
          new_n[i+1] += (10 - n[i+1])
        
        if i > 0:
          if n[i-1] == 8:
            n[i-1] += 1
          if n[i-1] == 9:
            n[i-1] -= 1

    for i in new_n:
      print(i, end = '')
    continue

  print('here')
  # else
  new_n = [0] * len(n)
  for i in range(len(n)-1, -1, -1):
    if int(n[i]) == int_d:
      if i == len(n)-1:
        new_n[i] = 1
      else:
        # print((10 - new_n[i+1]))
        new_n[i+1] += (10 - int(n[i+1]))
  
  for i in new_n:
    print(i, end = '')
