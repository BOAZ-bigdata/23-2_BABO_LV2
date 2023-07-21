'''
n x n
(r, c) => r행 c열(1부터 시작)
치킨 거리 = 집과 가장 가까운 치킨집 사이 거리
도시 치킨 거리 = 모든 치킨 거리의 합
거리 = abs(r1-r2) + abs(c1-c2)

0 = 빈칸
1 = 집
2 = 치킨집

남아 있을 수 있는 치킨집이 m개일 때, 도시의 치킨 거리 구하기


sol)
치킨집 개수 중 m개의 조합...?
'''

from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chicks = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i+1, j+1))
        elif city[i][j] == 2:
            chicks.append((i+1, j+1))

check = []
for i in combinations(chicks, m):
    check.append(i)

distance = 1000000
for i in range(len(check)):
    total = 0
    for h in houses:
        chick_dis = 9999
        for j in range(m):
            chick_dis = min(chick_dis, abs(h[0] - check[i][j][0]) + abs(h[1] - check[i][j][1]))
        total += chick_dis
    distance = min(distance, total)

print(distance)

