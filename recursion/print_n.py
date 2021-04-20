print('Print n numbers using recurssion')
n = int(input())

def print_numbers(n): 
  if(n == 0): 
    return
  
  # descending print
  # print(n)
  print_numbers(n-1)
  # ascending print
  print(n)
  
print_numbers(n)
