# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_boss

# dp[1] <- 1

# for i = 2 to n
#     if a[i-1] <= a[i] then
#         dp[i] <- dp[i-1]+1
#     else
#         dp[i] <- 1

# print max({dp[1], ... ,dp[n]})

n = int(input())
a = [int(input()) for i in range(n)]

dp = [1] * n

for i in range(1, n):
    if a[i] >= a[i-1]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = 1

print(max(dp))
