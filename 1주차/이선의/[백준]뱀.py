'''
뱀 몸길이 1
맨위 맨 좌측 위치(0,0)

초마다 이동
1. 머리를 다음칸에 위치시킴
2. 벽 || 몸과 부딪치면 게임 종료
3. 이동 칸에 사과 존재, 꼬리 움직임 X(몸길이 길어짐)
4. 사과 X, 꼬리 위치칸 없앰
'''

from collections import deque

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2 #사과

'''
위 (0, -1)
오른쪽 (1, 0)
왼쪽 (-1, 0)
아래쪽 (0, 1)
'''
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = deque()
snake.append((0, 0))

# 이동 정보
l = int(input())
l_list = {}
# (몇 초 뒤에 , D오른쪽 L왼쪽) 이동
for i in range(l):
    x, s = input().split()
    l_list[int(x)] = s

x, y = 0, 0
board[x][y] = 1
sec = 0
toward = 0
while True:
    sec += 1
    x += direct[toward][0]
    y += direct[toward][1]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if board[x][y] == 2:
        snake.append((x, y))
        board[x][y] = 1
        if sec in l_list:
            if l_list[sec] == 'L':
                toward = (toward-1) % 4
            else:
                toward = (toward + 1) % 4
    elif board[x][y] == 0:
        board[x][y] = 1
        snake.append((x, y))
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
        if sec in l_list:
            if l_list[sec] == 'L':
                toward = (toward-1) % 4
            else:
                toward = (toward + 1) % 4
    else:
        break


print(sec)