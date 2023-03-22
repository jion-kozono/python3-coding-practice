# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_continuous_boss

n = int(input())
a = [int(input()) for i in range(n)]

dp = [1] * n

for i in range(1, n):
    if a[i] <= a[i-1]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = 1

print(max(dp))
