n = int(input())
A = list(map(int, input().split()))
k = int(input())


for i in range(n):
    if A[i] == k:
        ans = i+1
        print(ans)
