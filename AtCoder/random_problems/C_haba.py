import sys
from collections import deque

def solve():

    data = sys.stdin.read().split()

    r = int(data[0])
    c = int(data[1])

    s = [int(data[2])-1,int(data[3])-1,0]
    g = [int(data[4])-1,int(data[5])-1]

    mass = [list(data[j+6]) for j in range(r)]

    def find_null(point: list):
        result = []
        upper_point = [point[0]+1,point[1],point[2]]
        lower_point = [point[0]-1,point[1],point[2]]
        right_point = [point[0],point[1]+1,point[2]]
        left_point = [point[0],point[1]-1,point[2]]
        if mass[upper_point[0]][upper_point[1]] == '.':
            upper_point[2] += 1
            result.append(upper_point)
            mass[upper_point[0]][upper_point[1]] = '#'
        if mass[lower_point[0]][lower_point[1]] == '.':
            lower_point[2] += 1
            result.append(lower_point)
            mass[lower_point[0]][lower_point[1]] = '#'
        if mass[right_point[0]][right_point[1]] == '.':
            right_point[2] += 1
            result.append(right_point)
            mass[right_point[0]][right_point[1]] = '#'
        if mass[left_point[0]][left_point[1]] == '.':
            left_point[2] += 1
            result.append(left_point)
            mass[left_point[0]][left_point[1]] = '#'

        return result
    
    not_goal = True
    A = deque()
    A.append(s)
    num_act = 0
    
    while not_goal:
        new_point = A.popleft()
        if (new_point[0] == g[0] and new_point[1] == g[1]):
            num_act = new_point[2]
            not_goal = False
        else:
            A.extend(find_null(new_point))

    print(num_act)



if __name__ == '__main__':
    solve()


#もう一つ地図を用意し回数をそこに書いていくほうほう
from collections import deque
R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
c=[input() for _ in range(R)]

sy,sx=sy-1,sx-1
gy,gx=gy-1,gx-1
que=deque()
dy=[0,1,0,-1]
dx=[-1,0,1,0]

dist=[[-1]*C for _ in range(R)]
dist[sy][sx]=0
que=deque()
que.append((sy,sx))

while que:
  y,x=que.popleft()
  if (y,x)==(gy,gx):
    break
  
  for i in range(4):
    newy=y+dy[i]
    newx=x+dx[i]
    
    if c[newy][newx]=="." and dist[newy][newx]==-1:
      dist[newy][newx]=dist[y][x]+1
      que.append((newy,newx))
print(dist[gy][gx])