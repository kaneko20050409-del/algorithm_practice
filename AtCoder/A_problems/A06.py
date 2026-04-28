# オリジナル　遅すぎる
# n,q = map(int, input().split())
# a = list(map(int, input().split()))
# l = []
# r = []
# for _ in range(q):
#     li,ri = map(int, input().split())
#     l.append(li)
#     r.append(ri)

# for i in range(q):
#     total = 0
#     for j in range(l[i]-1,r[i]):
#         total += int(a[j])
#     print(total)


# # pythonらしい書き方
# n = int(input())
# q = int(input())
# a = list(map(int, input().split()))

# # 1. Q行分のデータを [ [L1, R1], [L2, R2], ... ] の形式で受け取る
# data = [list(map(int, input().split())) for _ in range(q)]

# # 2. zipを使って「縦」に分解する
# l, r = zip(*data)

# # zipの結果はタプルなので、必要に応じてリストに変換
# l, r = list(l), list(r)

# # pythonらしい書き方２
# import sys
# input = sys.stdin.readline

# n, q = map(int, input().split())
# a = list(map(int, input().split()))

# # --- 累積和の準備 ---
# # s[i] = aの先頭からi個の要素の合計
# s = [0] * (n + 1)
# for i in range(n):
#     s[i+1] = s[i] + a[i]

# # --- クエリの処理 ---
# for _ in range(q):
#     l, r = map(int, input().split())
#     # 累積和を使えば、ループを回さずに一瞬で求まる
#     # 範囲 [l, r] の和は、(rまでの合計) - (l-1までの合計)
#     print(s[r] - s[l-1])

# 調整して合体させたやつ
import sys
input = sys.stdin.readline

n,q = map(int, input().split())
a = list(map(int, input().split()))
l = []
r = []
for _ in range(q):
    li,ri = map(int, input().split())
    l.append(li)
    r.append(ri)

s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]

for i in range(q):
    print(s[r[i]] - s[l[i]-1])


# プロ
# 解説　https://www.notion.so/A06-350c6f48ff5980f6934efc29fbb6254a
import sys

def solve():
    data = iter(sys.stdin.read().split())

    N = int(next(data))
    Q = int(next(data))
    A = [int(next(data)) for _ in range(N)]

    S = [0]*(N + 1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    
    for _ in range(Q):
        l = int(next(data))
        r = int(next(data))
        print(S[r] - S[l-1])

    


    
if __name__ == '__main__':
    solve()