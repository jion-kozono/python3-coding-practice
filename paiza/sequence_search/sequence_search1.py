n = int(input())
A = list(map(int, input().split()))
k = int(input())

ans = 0

for i in range(n):
    if A[i] == k:
        ans+=1

print(ans)
