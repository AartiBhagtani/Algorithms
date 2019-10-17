from collections import OrderedDict
def merge_the_tools(string, k):
    ans = [string[i:i+k] for i in range(0, len(string), k)]

    for x in ans:
        d = OrderedDict.fromkeys(x, 0)
        print(''.join(d.keys()))    
        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)