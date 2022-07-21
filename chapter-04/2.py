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

# 4-2.py 답안 예시
N = int(input())
count = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
