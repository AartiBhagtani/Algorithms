import math

def lsb_set(num):
    b_r = bin(num).replace("0b", "")
    index = 0
    for i in range(len(b_r)-1, -1, -1):
        index += 1
        if b_r[i] == '1':
            return index
    return index

def MaxPairs (N, nums):
    # Write your code here
    score = 0 
    odd_count = 0
    temp_list = []
    sort_list = []
    for i in nums:
        if i % 2 != 0:
            odd_count += 1
        else:
            temp_list.append(i)
    score += math.ceil(odd_count/2)

    for i in temp_list:
        sort_list.append(lsb_set(i))

    sort_list.sort()
    for i in range(len(sort_list)-1):
        score += max(sort_list[i], sort_list[i+1])
    return score

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    out_ = MaxPairs(N, nums)
    print (out_)