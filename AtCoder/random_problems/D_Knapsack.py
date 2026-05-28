import sys

def solve():

    data = sys.stdin.read().split()

    N = int(data[0])
    W = int(data[1])

    w = []
    v = []
    idx = 0

    for _ in range(N):
        w.append(int(data[idx + 2]))
        v.append(int(data[idx + 3]))
        idx += 2

    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(N):
        current_w = w[i]
        current_v = v[i]
        for j in range(W+1):
            if j-current_w >= 0:
                dp[i+1][j] = max(dp[i][j],dp[i][j-current_w]+current_v)
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[N][W])



# if __name__ == '__main__':
#     solve()


#参照するのは一行前のデータのみしたがって１次元リストで完結できるー＞はやい

def solve_2():

    data = sys.stdin.read().split()

    N = int(data[0])
    W = int(data[1])

    item = [[] for _ in range(N)]
    idx = 0

    for i in range(N):
        item[i].append(int(data[idx+2]))
        item[i].append(int(data[idx+3]))
        idx += 2

    dp = [0 for _ in range(W+1)]

    for we,va in item:
        for i in range(W,we-1,-1):
            if dp[i] <= dp[i-we] + va:
                dp[i] = dp[i-we] + va
    
    print(max(dp))



if __name__ == '__main__':
    solve_2()