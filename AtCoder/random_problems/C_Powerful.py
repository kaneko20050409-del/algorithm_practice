import sys
from collections import deque
import bisect


def solve():

    data = sys.stdin.read().split()

    n = int(data[0])
    m = int(data[1])
    A = sorted(map(int, data[2:n+2]))
    A = deque(A)

    result = 0

    for _ in range(m):
        num = (A.pop())//2
        bisect.insort_right(A, num)
            
    result = sum(A)

    print(result)


if __name__ == '__main__':
    solve()


#Gemini
import sys
import heapq

def solve():
    # 入力を一括で読み込み
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    
    # データをマイナスにしてリスト化（data[2] から n 個取得）
    # マイナスにすることで、絶対値が最も大きいものが最小値として扱われる
    A = [-int(x) for x in data[2:n+2]]
    
    # リストをヒープ（優先度付きキュー）に変換
    heapq.heapify(A)

    # M回、最大値を取り出して半分（切り捨て）にして戻す
    for _ in range(m):
        # 一番大きい値（マイナスがついているので最小値）を取り出す
        max_val = -heapq.heappop(A)
        
        # 半分にする（// は切り捨て）
        halved = max_val // 2
        
        # マイナスをつけてヒープに戻す
        heapq.heappush(A, -halved)

    # 最終的な合計を求める（マイナスを戻して合計する）
    result = sum(-x for x in A)
    print(result)

if __name__ == '__main__':
    solve()

#heapqを使わないかしこいやつ
import sys



def make_sub_list(a):
    pred_a = a
    sub_list = []
    while (a > 0):
        a = a // 2 
        sub_list.append(pred_a - a)
        pred_a = a
    return sub_list

def main():
    list_length, discount_num = [int(x) for x in input().split()]
    list_A = [int(x) for x in input().split()]
    list_sum = sum(list_A)
    
    sub_list = []
    for a in list_A:
        sub_list += make_sub_list(a)
    
    sub_list.sort(reverse=True)
    discount_sum = sum(sub_list[:discount_num])
    print(list_sum - discount_sum)
    

    
if __name__ == "__main__":
    main()