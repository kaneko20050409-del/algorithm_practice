# がんばって自分で書いたけど終わってるコード

# import sys

# def solve():

#     data = iter(sys.stdin.read().split())

#     n = int(next(data))

#     dot_lst = [[int(next(data)),int(next(data))] for _ in range(n)]

#     s = list(next(data))

#     is_collision = 'No'

#     y_lst = []

#     for i in range(n):
#         is_in_lst = False
#         for j in range(len(y_lst)):
#             if dot_lst[i][1] == y_lst[j][0]:
#                 y_lst[j].append([i,dot_lst[i][0],s[i]])
#                 is_in_lst = True
#             else:
#                 pass
#         if not is_in_lst:
#             y_lst.append([dot_lst[i][1],[i,dot_lst[i][0],s[i]]])

#     y_lst.sort(key=len)

#     for i in range(len(y_lst)):
#         if len(y_lst[i]) == 2:
#             pass
#         else:
#             for j in range(1,len(y_lst[i])):
#                 for k in range(1,len(y_lst)):
#                     if y_lst[i][j][2] != y_lst[i][j+k][2]:
#                         if y_lst[i][j][2] == 'L':
#                             if y_lst[i][j][1] > y_lst[i][j+k][1]:
#                                 is_collision = 'Yes'
#                             else:
#                                 pass
#                         else:
#                             if y_lst[i][j][1] < y_lst[i][j+k][1]:
#                                 is_collision = 'Yes'
#                             else:
#                                 pass
#                     else:
#                         pass

#     print(is_collision)





# if __name__ == '__main__':
#     solve()



# 解答コード　辞書使えば計算量をO(N^3)->O(N)にできる

import sys

def solve():
    # 高速入力
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    # X座標とY座標のリストを格納
    # data[1:2*n+1:2] でX座標、data[2:2*n+1:2] でY座標をまとめて取得
    x_lst = [int(x) for x in data[1:2*n:2]]
    y_lst = [int(y) for y in data[2:2*n+1:2]]
    s = data[2*n+1]
    
    # Y座標ごとに、Rを向いている人の最小のX座標、Lを向いている人の最大のX座標を記録する辞書
    # 辞書の中身のイメージ: { Y座標: [Rの最小X, Lの最大X] }
    from collections import defaultdict
    # 初期値として、Rの最小値には無限大(inf)、Lの最大値にはマイナス無限大(-inf)を設定
    y_groups = defaultdict(lambda: [float('inf'), float('-inf')])
    
    for i in range(n):
        x = x_lst[i]
        y = y_lst[i]
        direction = s[i]
        
        if direction == 'R':
            # Rを向いている人の最小のX座標を更新
            if x < y_groups[y][0]:
                y_groups[y][0] = x
        else:
            # Lを向いている人の最大のX座標を更新
            if x > y_groups[y][1]:
                y_groups[y][1] = x
                
    # 衝突しているか判定
    for y, (min_r, max_l) in y_groups.items():
        # 右に行く人の最小Xが、左に行く人の最大Xより左にあれば衝突する
        if min_r < max_l:
            print('Yes')
            return
            
    print('No')

if __name__ == '__main__':
    solve()


# dequeを使ったコード

import sys
from collections import defaultdict, deque

def solve():
    # 高速入力
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    x_lst = [int(x) for x in data[1:2*n:2]]
    y_lst = [int(y) for y in data[2:2*n+1:2]]
    s = data[2*n+1]
    
    # 1. 辞書型（defaultdict）で y 座標ごとにグループ化
    # y_groups[y座標] = [(x座標, 向き), (x座標, 向き), ...]
    y_groups = defaultdict(list)
    for i in range(n):
        y_groups[y_lst[i]].append((x_lst[i], s[i]))
        
    # 各 y 座標の直線ごとに判定
    for y, people in y_groups.items():
        
        # 2. x 座標が小さい順（左から右）にソート
        people.sort(key=lambda p: p[0])
        
        # 3. 追加課題：collections.deque をスタックとして使用
        stack = deque()
        
        for x, direction in people:
            if direction == 'R':
                # 右向きの人がいたらスタックに積む
                stack.append(x)
            elif direction == 'L':
                # 左向きの人が来たとき、スタックに右向きの人がいれば衝突！
                if stack: 
                    print('Yes')
                    return
                    
    print('No')

if __name__ == '__main__':
    solve()