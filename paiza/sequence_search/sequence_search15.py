n = int(input())
results = [input().split() for _ in range(n)]
k, l = map(int, input().split())

for name, score in results:
    if k <= int(score) <= l:
        print(name)
