def query_game (N, A, Q, P):
    ans = []
    reverse = False
    for queries in P:
        if queries[0] == 1:
            if reverse: 
               reverse = False
            else: 
                reverse = True
        elif queries[0] == 2:
            if reverse:
                i = N - queries[1]
                j = N - queries[2]
            else: 
                i = queries[1] - 1
                j = queries[2] - 1
            temp = A[j] 
            A[j] = A[i]
            A[i] = temp
        else:
            index = 0
            for i in range(len(A)):
                if A[i] == queries[1]:
                    index = i
                    break
            if reverse:
                index = N - index
            ans.append(index)
    return ans

    

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    P = [list(map(int, input().split())) for i in range(Q)]

    out_ = query_game(N, A, Q, P)
    print (' '.join(map(str, out_)))