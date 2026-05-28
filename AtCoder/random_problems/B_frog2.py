import sys

def solve():

    data = sys.stdin.read().split()

    N = int(data[0])
    K = int(data[1])

    H = [int(data[i+2]) for i in range(N)]

    INF = 10 ** 10

    dp = [INF] * N
    dp[0] = 0

    for i in range(N):
        for j in range(1,K+1):
            if i+j < N:
                dp[i+j] = min(dp[i+j],dp[i]+abs(H[i+j]-H[i]))

    print(dp[-1])


if __name__ == '__main__':
    solve()

#二重リストの中で関数を動かすと遅くなる。
#配るdpと貰うdp両方かけるといい

"""breakとcontinueのちがい
    breakはループから抜け出す
    continueはループをその一回分スキップ"""

#もらうdpの速いコード
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
H = list(map(int, input().split()))
INF = 10 ** 10
dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    for j in range(1, K+1):
        prev = i - j
        if prev < 0:
            break
        
        new_cost = dp[prev] + abs(H[i]-H[prev])
        if dp[i] > new_cost:
            dp[i] = new_cost

print(dp[-1])