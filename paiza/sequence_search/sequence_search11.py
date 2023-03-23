n = int(input())
A = list(map(int, input().split()))
k = int(input())

result = []

for a in A:
    if a <= k:
        result.append(a)

print(max(result))
