from sys import stdin
import sys
from datetime import datetime

# n = int(stdin.readline())

def fibo(n):
  if n <= 0: 
    sys.exit('n cannot be less than zero')
  elif n == 1: 
    return 0
  elif(n == 2):
    return 1
  return fibo(n-2) + fibo(n-1)

print(datetime.now().time()) # time object
print(fibo(9))
print(datetime.now().time()) # time object
