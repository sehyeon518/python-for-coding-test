# 4-4.py
N, M = map(int, input().split())
x, y, head = map(int, input().split())
x -= 1
y -= 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

the_map = []
for n in range(N):
    m = list(map(int, input().split()))
    the_map += [m]
visited = [[0] * M for _ in range(N)]
visited[x][y] = 1
count = 1
turn = 0


def print_table(table):
    print("현재 방문 현황")
    for i in table:
        print(i)


# print("시작", end=" ")
# print_table(visited)

while True:

    head = (head - 1) % 4
    turn += 1
    # print_table(visited)
    # print('현재 방향:', head)
    # print('회전 횟수:', turn)

    next_x = x + dx[head]
    next_y = y + dy[head]
    if 0 <= next_x < N and 0 <= next_y < M:
        if visited[next_x][next_y] == 0:  # 가보지 않은 칸이 존재한다
            visited[next_x][next_y] = 1   # 왼쪽으로 회전하여 전진한다.
            count += 1
            turn = 0
            if the_map[next_x][next_y] == 0:
                x = next_x
                y = next_y
            else:
                continue

    elif turn >= 4:
        break


print(count)

# 4-4.py 답안 예시
N, M = map(int, input().split())
x, y, head = map(int, input().split())
x -= 1
y -= 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

the_map = []
for n in range(N):
    m = list(map(int, input().split()))
    the_map += [m]
visited = [[0] * M for _ in range(N)]
visited[x][y] = 1
count = 0
turn = 0

while True:

    head = (head - 1) % 4

    next_x = x + dx[head]
    next_y = y + dy[head]
    if the_map[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
        visited[next_x][next_y] = 1
        count += 1
        x = next_x
        y = next_y
        turn = 0
    else:
        turn += 1

    if turn == 4:
        next_x = x - dx[head]
        next_y = y - dy[head]
        if visited[next_x][next_y] == 0:
            x = next_x
            y = next_y
        else:
            break
        turn = 0

print(count)
