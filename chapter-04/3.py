# 4-3.py
p = input()
x = ord(p[0]) - 96
y = int(p[1])

moving = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
count = 0
for dx, dy in moving:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)

# 4-3.py 답안 예시
p = input()
x = ord(p[0]) - ord('a') + 1
y = int(p[1])

moving = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
count = 0
for step in moving:
    nx = x + step[0]
    ny = y + step[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)
