from sys import stdin

n = int(stdin.readline())
y = [int(x) for x in (stdin.readline().split())]

def rec_sort(arr):
  if len(arr) == 1:
    return
  temp = arr.pop()
  rec_sort(arr)

  insert(arr, temp)

def insert(arr, temp): 
  if(len(arr) == 0 or arr[-1] <= temp): 
    arr.append(temp)
    return

  temp2 = arr.pop()  
  insert(arr, temp)
  arr.append(temp2)

rec_sort(y)

print(y)
