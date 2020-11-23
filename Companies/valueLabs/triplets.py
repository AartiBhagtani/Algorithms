from collections import Counter

def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    if(k > n - k):
        k = n - k
    # initialize result
    res = 1
    # Calculate value of  
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res


def good(a, b, c):
    ct = 0
    s = a+b+c
    if s%a == 0:
        ct += 1
    if s%b == 0:
        ct += 1
    if s%c == 0:
        ct += 1
   
    if ct == 1:
        return True
    else:
        return False
   
num = int(input())
arr = []
for i in range(num) :
    arr.append(int(input()))

c = Counter(arr)
n = len(c.keys())
arr = list(c.keys())
print(c)
count = 0
for i in range(n):
    for j in range(i+1, n):
        if (c[arr[i]] + c[arr[j]]) >= 3:
            if c[arr[j]] >= 2:
                if good(arr[i], arr[j], arr[j]):
                    print(arr[i], arr[j], arr[j])
                    temp = (binomialCoefficient(c[arr[i]], 1) * binomialCoefficient(c[arr[j]], 2)) * 6
                    count = count + temp
            if c[arr[i]] >= 2:
                if good(arr[i], arr[j], arr[i]):
                    print(arr[i], arr[j], arr[i])
                    temp = (binomialCoefficient(c[arr[j]], 1) * binomialCoefficient(c[arr[i]], 2)) * 6
                    count = count + temp
        for k in range(j+1, n):
            if good(arr[i], arr[j], arr[k]):
                temp = (binomialCoefficient(c[arr[j]], 1) * binomialCoefficient(c[arr[i]], 1) + binomialCoefficient(c[arr[k]], 1)) * 6
                count = count + temp      

print(int(count))
