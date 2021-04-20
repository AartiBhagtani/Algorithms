# 1.4 page 60 ctdi
from sys import stdin

def can_be_Palindrome(st): 
  No_of_chars = 256
  l = [0] * No_of_chars
  count_odd = 0
  
  for i in range(0, len(s)):
    l[ord(s[i])] += 1

  for i in range(0, 256):
    if l[i] % 2 != 0:
      if count_odd > 1: 
        return False
        return
      count_odd += 1
    
  return True

s = stdin.readline()

print(can_be_Palindrome(s))
