# 4-2.py
N = int(input())
count = 0

for i in range(N + 1):
    if i in [3, 13, 23]:
        count += 3600
        continue
    for j in range(60):
        if j in [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]:
            count += 60
            continue
        for k in range(60):
            if k in [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]:
                count += 1
print(count)

# 4-1.py 답안 예시
N = int(input())
plan = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moving = ['L', 'R', 'U', 'D']

for m in plan:
    for n in range(len(moving)):
        if m == moving[n]:
            next_x = x + dx[n]
            next_y = y + dy[n]
    if next_x < 1 or next_y < 1 or next_y > N or next_y > N:
        continue
    x, y = next_x, next_y
print(x, y)
