import sys
import math

def solve():

    data = sys.stdin.read().split()
        
    N = int(data[0])

    H = [int(data[i+1]) for i in range(N)]

    dp = [math.inf] * N
    dp[0] = 0

    for i in range(N):
        if i + 1 < N:
            dp[i+1] = min(dp[i+1], dp[i] + abs(H[i+1] - H[i]))

        if i + 2 < N:
            dp[i+2] = min(dp[i+2], dp[i] + abs(H[i+2] - H[i]))

    print(dp[-1])

if __name__ == '__main__':
    solve()