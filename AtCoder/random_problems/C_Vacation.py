import sys

def solve():
    
    data = sys.stdin.read().split()

    N = int(data[0])
    ABC = [[int(data[3*i+1]),int(data[3*i+2]),int(data[3*i+3])] for i in range(N)]

    INF = 10 ** 10
    dp = [-INF] * (N+1)
    dp[0] = 0

    # def get_max(lst):

    #     num_index = [0,0]
 
    #     if lst[0] <= lst[1]:
    #         if lst[1] <= lst[2]:
    #             num_index = [lst[2],2]
    #         else:
    #             num_index = [lst[1],1]
    #     else:
    #         if lst[0] <= lst[2]:
    #             num_index = [lst[2],2]
    #         else:
    #             num_index = [lst[0],0]

    #     return num_index

    for i in range(N):
        max_num = 0
        max_index = ABC[0].index(max(ABC[0]))
        ABC[i].remove(ABC[i][max_index])
        if ABC[i][0] > ABC[i][1]:
            max_index = 0
        else:
            max_index = 1
        max_num = ABC[i][max_index]
        dp[i+1] = dp[i] + max_num

    print(dp[-1])


# if __name__ == '__main__':
#     solve()

import sys

def solve_2():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])

    ABC = []
    idx = 1
    for _ in range(N):
        ABC.append([int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])])
        idx += 3

    dp = [[0] * 3 for _ in range(N)]

    dp[0][0] = ABC[0][0]
    dp[0][1] = ABC[0][1]
    dp[0][2] = ABC[0][2]

    for i in range(1, N):
        dp[i][0] = ABC[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = ABC[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = ABC[i][2] + max(dp[i-1][0], dp[i-1][1])

    print(max(dp[N-1]))

# if __name__ == '__main__':
#     solve_2()




import sys

def solve_3():

    data = sys.stdin.read().split()

    N = int(data[0])

    ABC = []
    idx = 0

    for _ in range(N):
        ABC.append([int(data[1+idx]),int(data[2+idx]),int(data[3+idx])])
        idx += 3

    dp = [[0]*3 for _ in range(N)]

    dp[0][0] = ABC[0][0]
    dp[0][1] = ABC[0][1]
    dp[0][2] = ABC[0][2]

    for i in range(N):
        dp[i][0] = ABC[i][0] + max(dp[i-1][1],dp[i-1][2])
        dp[i][1] = ABC[i][1] + max(dp[i-1][0],dp[i-1][2])
        dp[i][2] = ABC[i][2] + max(dp[i-1][0],dp[i-1][1])

    print(max(dp[N-1]))

if __name__ == '__main__':
    solve_3()





if __name__ == '__main__':
    solve_3()