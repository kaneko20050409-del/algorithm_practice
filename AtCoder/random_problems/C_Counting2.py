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


if __name__ == '__main__':
    solve()