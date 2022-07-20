# 3-1.py
N = 1260
count = 0
coin = [500, 100, 50, 10]

for i in coin:
    while N-i >= 0:
        N-=i
        count+=1
print(count)

# 3-1.py 답안 예시
n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
	count += n//coin
	n %= coin
print(count)
