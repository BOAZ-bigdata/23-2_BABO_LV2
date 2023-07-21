'''
   북4
서2    동1
   남3

반시계방향

ㄱ자 꺾이는 모양
: 4 - 2
: 2 - 3
: 3 - 1
: 3 - 1 (해당 패턴이 두 번 나옴)

0
1
2
3
4
5
'''

k = int(input())
lines = []

max_width_idx = 0;
max_width = 0;
max_height_idx = 0;
max_height = 0;
for i in range(6):
    direct, length = map(int, input().split(" "))
    if (direct == 2 or direct == 1) and length > max_width:
        max_width = length
        max_width_idx = i;

    if (direct == 3 or direct == 4) and length > max_height:
        max_height = length
        max_height_idx = i;

    lines.append((direct, length))

small_height = abs(lines[(max_height_idx -1) % 6][1] - lines[(max_height_idx+1) % 6][1])
small_width = abs(lines[(max_width_idx -1) % 6][1] - lines[(max_width_idx+1) % 6][1])


print((max_width * max_height - small_height * small_width) * k)