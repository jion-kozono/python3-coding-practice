N, Q = map(int, input().split())
S = input()
L, R = [], []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

sums = [0] * (N+1)
isAfterA = False
for i in range(N):
    if isAfterA and S[i] == "C":
        sums[i+1] = sums[i] + 1
    else:
        sums[i+1] = sums[i]
    if S[i] == "A": isAfterA = True

for i in range(Q):
    left, right = L[i], R[i]
    ans = sums[right] - sums[left]
    print(ans)
