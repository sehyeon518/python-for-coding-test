# 3-2.py
N, M, K = map(int, input().split())
list = list(map(int, input().split()))

list.sort()
biggest = list[-1]
second = list[-2]

sequence = biggest * K + second
nseq = M // (K+1)
nbig = M - nseq * (K+1)

result = nseq * sequence + nbig * biggest
print(result)

# 3-2.py 답안 예시
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
biggest = data[N-1]
second = data[N-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
