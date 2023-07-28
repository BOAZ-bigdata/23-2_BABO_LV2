'''
선생님: 상하좌우를 아무리 멀리 있더라도 장애물로 막히기 전에 다 볼 수 있음

N*N

학생: S
선생: T
이외: X

3개의 장애물을 설치 + 감시 피할 수 있는지 여부
'''
import collections
from collections import deque

# 입력
n = int(input())
hall = []

for i in range(n):
    hall.append(list(input().split()))

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
ans = False

def bfs():
    isVisited = [[0] * n for _ in range(n)]
    for k in range(n):
        for j in range(n):
            if hall[k][j] == 'T':
                q.append((k, j))
    while q:
        x, y = q.popleft()
        for d in dxy:
            tx, ty = x, y
            while True:
                nx = tx + d[0]
                ny = ty + d[1]
                if 0 <= nx < n and 0 <= ny < n:
                    if hall[nx][ny] == 'X' and isVisited[nx][ny] == 0:
                        isVisited[nx][ny] = 1
                    elif hall[nx][ny] == 'S':
                        return False
                    elif hall[nx][ny] == 'O':
                        break
                    tx, ty = nx, ny
                else:
                    break
    return True


def solution(cur):
    global ans

    if cur == 3:
        if bfs():
            ans = True
        return

    for k in range(n):
        for j in range(n):
            if hall[k][j] == 'X':
                hall[k][j] = 'O'
                solution(cur + 1)
                hall[k][j] = 'X'


solution(0)

if ans:
    print("YES")
else:
    print("NO")
