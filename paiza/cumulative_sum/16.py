n, x, y = map(int,input().split())
s = input()

# 文字列 str の 3 文字目から 8 文字目までの 'b' の個数を累積和を用いて求めてください。
b = [0] * (n)
for i in range(n):
    if s[i] == "b":
        b[i] = 1

cumulative_sum = [0] * (n+1)
for i in range(n):
    if b[i] == 1:
        cumulative_sum[i+1] = cumulative_sum[i] + 1
    else:
        cumulative_sum[i+1] = cumulative_sum[i]

print(cumulative_sum[y] - cumulative_sum[x-1])
