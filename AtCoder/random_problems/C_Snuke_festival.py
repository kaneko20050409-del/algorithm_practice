import sys

def solve():

    data = iter(sys.stdin.read().split())

    n = int(next(data))
    upper = []
    middle = []
    lower = []
    parts = [upper,middle,lower]
    for i in range(3):
        for _ in range(n):
            parts[i].append(int(next(data)))
        parts[i].sort()

    # 自作くそ二分探索関数
    # なにがくそか
    # while check が無限ループする閾値がリストに存在しない場合
    # 計算範囲もあいまいでミスがある
    # def binary_search(lst: list,num: int): #二分探索関数numは閾値
    #     check = True
    #     index = []
    #     while check:
    #         len_lst = len(lst)
    #         if num > lst[int(len_lst/2)]:
    #             lst = lst[int(len_lst/2):]
    #         elif num < lst[int(len_lst/2)]:
    #             lst = lst[:int(len_lst/2)]
    #         else:
    #             index = [i for i, x in enumerate(lst) if x == num]
    #             check = False
    #     return index[-1] #条件満たす配列のインデックスを返す

    # ちゃんとした二分探索関数
    def binary_upper_search_count(lst, target):
        left = 0
        right = len(lst)
        while left < right:
            mid = (left + right) // 2
            if lst[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left  # target未満の個数がそのまま返る
    
    def binary_lower_search_count(lst, target):
        left = 0
        right = len(lst)
        while left < right:
            mid = (left + right) // 2
            if lst[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right
    

    result = 0
    for i in range(n): # middle[i]をupper,lowerで二分探索ー＞条件満たすやつ数える
        upper_num = binary_upper_search_count(upper, middle[i])
        lower_num = binary_lower_search_count(lower, middle[i])
        lower_num = n - lower_num
        result += upper_num * lower_num

    print(result)
    

if __name__ == '__main__':
    solve()


# 最速コード
import sys
import bisect  # 標準ライブラリの二分探索

def solve():
    # 入力の高速化
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # スライスを使って一気に分割（これだけでも速くなります）
    upper = sorted(map(int, input_data[1:n+1]))
    middle = sorted(map(int, input_data[n+1:2*n+1]))
    lower = sorted(map(int, input_data[2*n+1:3*n+1]))

    result = 0
    for b in middle:
        # upperの中で b 未満の数を探す (indexがそのまま個数になる)
        upper_count = bisect.bisect_left(upper, b)
        
        # lowerの中で b より大きい数を探す
        # bisect_rightは「b以下の最後の要素の次」のインデックスを返す
        lower_idx = bisect.bisect_right(lower, b)
        lower_count = n - lower_idx
        
        result += upper_count * lower_count

    print(result)

if __name__ == '__main__':
    solve()