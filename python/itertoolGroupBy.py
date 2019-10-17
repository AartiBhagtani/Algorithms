# link: https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

s = input()
for (key, group) in groupby(s):
    t = (len(list(group)), int(key))
    print(t, end=' ')

