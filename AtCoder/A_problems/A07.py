# # オリジナル遅すぎる
# import sys
# input = sys.stdin.readline

# d = int(input())
# n = int(input())
# l = []
# r = []
# for i in range(n):
#     li,ri = map(int, input().split())
#     l.append(li)
#     r.append(ri)

# # d行目にd日目の出席者数を出力

# num_part = [0]*d

# for i in range(n):
#     for j in range(l[i]-1,r[i]):
#         num_part[j] += 1

# for i in range(d):
#     print(num_part[i])

# 計算量を小さくしたバージョン（Imos method）
# 解説　https://www.notion.so/A07-350c6f48ff59809e83fdebeff9f4f25b
import sys
input = sys.stdin.readline

d = int(input())
n = int(input())

# 変化を記録するための配列（終了日の翌日のために d+1 のサイズにする）
diff = [0] * (d + 1)

for _ in range(n):
    l, r = map(int, input().split())
    # 開始日に +1
    diff[l-1] += 1
    # 終了日の翌日に -1
    if r < d:
        diff[r] -= 1

# 累積和をとることで、各日の出席者数が出る
ans = [0] * d
current_attendees = 0
for i in range(d):
    current_attendees += diff[i]
    ans[i] = current_attendees

# 出力
for a in ans:
    print(a)

# code by Ral88
import sys

def solve():
    data = iter(sys.stdin.read().split())
    
    D = int(next(data))
    N = int(next(data))
    number = 0

    people = [0]*(D+2)

    for _ in range(N):
        l = int(next(data))
        r = int(next(data))
        
        people[l] += 1
        people[r+1] += -1
    
    for i in range(D):
        number += people[i + 1]
        print(number)

    



if __name__ == "__main__":
    solve()