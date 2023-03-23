n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    if A[i] % 2 == 0:
        print(i+1)
        break
