# import sys

# def solve():
#     data = iter(sys.stdin.read().split())

#     N = int(next(data))
#     Q = int(next(data))
#     S = list((next(data)))

#     for _ in range(Q):
#         l = int(next(data))
#         r = int(next(data))
#         part_S = S[l-1:r]
#         result = ''.join(part_S)
#         print(result.count('AC'))




# if __name__ == '__main__':
#     solve()

# 累積和を使ったコード

import sys

def solve():
    data = iter(sys.stdin.read().split())

    N = int(next(data))
    Q = int(next(data))
    S = next(data)
    
    acc = [0] * (N+1)  #ACがi文字目までに何回出てきたかをカウント
    for i in range(1,N):
        acc[i+1] = acc[i]
        if S[i-1:i+1] == 'AC':
            acc[i+1] += 1

    for i in range(Q):
        l = int(next(data))
        r = int(next(data))
        print(acc[r]-acc[l])


if __name__ == '__main__':
    solve()