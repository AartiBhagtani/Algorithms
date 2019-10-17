from collections import Counter

for key, val in sorted(Counter(input()), key=lambda x: (-x[1], x[0]))[:3]:
    print(key, val)
