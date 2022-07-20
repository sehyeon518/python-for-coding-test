# 3-3.py
N, M = map(int, input().split())
cards = []
for n in range(N):
    card = list(map(int, input().split()))
    card.sort()
    cards.append(card[0])
cards.sort()
print(cards[-1])

# 3-2.py 답안 예시 2
N, M = map(int, input().split())
result = 0
for i in range(N):
	data = list(map(int, input().split()))
	min_value = 10001
	for a in data:
		min_value = min(a, min_value)
	result = max(result, min_value)
print(result)

# 3-2.py 답안 예시 2
N, M = map(int, input().split())
result = 0
for i in range(N):
	data = list(map(int, input().split()))
	min_value = 10001
	for a in data:
		min_value = min(a, min_value)
	result = max(result, min_value)
print(result)
