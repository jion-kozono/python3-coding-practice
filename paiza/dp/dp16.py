# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_step0

# dp[1] <- 1

# for i = 2 to n
#     dp[i] <- 1  // 木 i のみからなる部分列の長さ
#     for j = 1 to i-1
#         if a[j] < a[i] then
#             dp[i] <- max(dp[i], dp[j]+1)    // 最後が木 j であるような増加部分列の末尾に木 i をくっつける

# print max({dp[1], ... ,dp[n]})

n = int(input())
a = [int(input()) for i in range(n)]

dp = [1] * n
for i in range(1, n):
    dp[i] = 1
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
