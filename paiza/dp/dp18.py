# https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_step0

# for i = 0 to x
#     dp[i] <- false

# dp[0] <- true   // おもりを選ばなければ、重さの和を0とすることができる

# for i = 1 to n  // おもり i までのおもりを使って
#     for j = x down to a_i    // 重さの和を j とすることができるか？
#         if dp[j-a_i] is true then
#             dp[j] <- true

# if dp[x] is true then
#     print "yes"
# else
#     print "no"

n, x = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [False] * (x+1)
dp[0] = True

for val in a:
    for j in range(x, val - 1, -1):
        if dp[j-val]:
            dp[j] = True
print("yes" if dp[x] else "no")
