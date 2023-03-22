# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_boss

n = int(input())
a = [int(input()) for i in range(n)]

dp = [1] * n
for i in range(1, n):
    dp[i] = 1
    for j in range(0, i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
