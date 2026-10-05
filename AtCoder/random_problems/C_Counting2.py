import  sys
import bisect

def solve():

    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    q = int(data[1])

    A = sorted(map(int, data[2:n+2]))

    result = []

    for i in range(q):
        x = int(data[n+2+i])
        num = bisect.bisect_left(A,x)
        result.append(str(n-num))

    sys.stdout.write("\n".join(result) + "\n")


# if __name__ == '__main__':
#     solve()


# 自分で２分探索実装しながら解く
import sys

def bigger_num(lst,target):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

def solves():
    data = sys.stdin.read().split()
    n = int(data[0])
    q = int(data[1])
    A = sorted(map(int,data[2:n+2]))
    x = list(map(int,data[n+2:n+q+2]))
    for i in range(q):
        print(n - bigger_num(A,x[i]))

if __name__ == '__main__':
    solves()