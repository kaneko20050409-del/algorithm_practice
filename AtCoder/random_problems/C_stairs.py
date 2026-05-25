import sys
import math

def solve():

    data = sys.stdin.read().split()

    N = int(data[0])
    M = int(data[1])
    a = list(map(int, data[2:M+2]))

    try_sum = 0
    can = True

    def exe_com(total: int, num: int):
        result = math.factorial(total-num)/(math.factorial(num)*math.factorial(total-2*num))
        return result

    for i in range(len(a)):
        if a[i] == a[i-1] + 1:
            can = False

    while can:
        for i in range(N//2):
            kari = exe_com(N,i)
            try_sum += kari

        for i in range(len(a)):
            index = a[i]
            if a[i-1] == index+2:
                for j in range((N-(index+2))//2):
                    one_kari = exe_com(N-index-2,j)
                    try_sum -= one_kari
                for j in range((N-(index+1))//2):
                    two_kari = exe_com(N-index-1,j)
                    try_sum -= two_kari
            else:
                for j in range((N-(index+2))//2):
                    one_kari = exe_com(N-index-2,j)
                    try_sum -= 2*one_kari
                for j in range((N-(index+1))//2):
                    two_kari = exe_com(N-index-1,j)
                    try_sum -= 2*two_kari
        break

    print(int(try_sum%1000000007))





if __name__ == '__main__':
    solve()

#答え

N,M=map(int,input().split())
stair=set(int(input()) for _ in range(M))
dp=[0]*(N+1)
dp[0]=1

for i in range(1,N+1):
  if i in stair:
    dp[i]=0
    continue
  
  dp[i]+=dp[i-1]
  
  if i>=2:
    dp[i]+=dp[i-2]
    dp[i]%=1000000007
    
print(dp[-1])