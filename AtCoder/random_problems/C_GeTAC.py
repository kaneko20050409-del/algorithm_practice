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

def solve_2():
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


# if __name__ == '__main__':
#     solve_2()


import sys

def solve():

    data = sys.stdin.read().split()

    N = int(data[0])
    Q = int(data[1])
    S = list(data[2])

    # 累積和
    acc = [0] * (N+1)

    for i in range(1,N):
        acc[i+1] = acc[i] + (S[i] == 'C' and S[i-1] == 'A')

    for i in range(Q):
        l = int(data[2*i+3])
        r = int(data[2*i+4])
        print(acc[r]-acc[l])

if __name__ == '__main__':
    solve()