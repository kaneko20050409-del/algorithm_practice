n, k = map(int, input().split())

count = 0

# 2重ループで num1 と num2 を決める
for num_1 in range(1, n + 1):
    for num_2 in range(1, n + 1):
        # 合計が k になるための num_3 を計算する
        num_3 = k - num_1 - num_2
        
        # num_3 が「1以上 n以下」の範囲に収まっているかチェック
        if 1 <= num_3 <= n:
            count += 1

print(count)


# かしこい超速い
# image/A05.jpg
N, K = map(int, input().split())

count = 0

for n in range(1, N+1):
    left = max(1, K - n - N)
    right = min(N, K - n - 1)
    
    if left <= right:
        count += (right - left + 1)

print(count)