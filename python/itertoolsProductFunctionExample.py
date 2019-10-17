# Link : https://www.hackerrank.com/domains/python
# Gives combination of every element in one list with every other element in all other list
from itertools import product

if __name__ == '__main__':
    k, m = [int(x) for x in input().split()]
    temp = []
    for _ in range(k):
        temp.append([int(x) for x in input().split()][1:])    

    max_sum = -1
    for ele in product(*temp):
        max_sum = max(sum(map(lambda x: x**2, ele))%m, max_sum)

    print(max_sum)


