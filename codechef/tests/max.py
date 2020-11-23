from sys import stdin

t = int(stdin.readline())

while t:
    n, k = [int(x) for x in stdin.readline().split()]
    arr = [int(x) for x in stdin.readline().split()]

    i = 0
    final_ans = 0
    while i < n:
        if arr[i] <= k:
            tmp_count, flag = 0, 0
            while i < n and arr[i] < k:
                print i 
                print arr[i]
                if arr[i] == k:
                      flag = 1
 
                tmp_count += 1
                i += 1

            if flag:
                final_ans += tmp_count
        else:
            i += 1

    print(final_ans)

    t -= 1