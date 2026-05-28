#Knapsack1では計算量O(NW)だったがそれじゃ爆発するのでO(N^2V)のアルゴリズムを作る

import sys

def solve():

    data = sys.stdin.read().split()
    N = int(data[0])
    W = int(data[1])
    # item = [[] for _ in range(N)]
    # idx = 0
    # sum_v = 0

    # for i in range(N):
    #     item[i].append(int(data[2+idx]))
    #     item[i].append(int(data[3+idx]))
    #     sum_v += int(data[3+idx])
    #     idx += 2
    w = []
    v = []
    idx = 0

    for _ in range(N):
        w.append(int(data[idx+2]))
        v.append(int(data[idx+3]))
        idx += 2

    sum_v = sum(v)
    INF = 10 ** 15

    dp = [[INF]*(sum_v+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        current_w = w[i]
        current_v = v[i]
        for j in range(sum_v+1):
            if j-current_v >= 0:
                dp[i+1][j] = min(dp[i][j],dp[i][j-current_v]+current_w)
            else:
                dp[i+1][j] = dp[i][j]
    
    max_index = 0

    for i in range(N+1):
        for j in range(sum_v+1):
            if dp[i][j] <= W:
                if j > max_index:
                    max_index = j
                
    print(max_index)



if __name__ == '__main__':
    solve()