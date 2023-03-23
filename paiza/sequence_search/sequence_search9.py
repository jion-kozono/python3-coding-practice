n = int(input())
A = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    if A[i] % 2 != 0:
        print(i+1)
        break
