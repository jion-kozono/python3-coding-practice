A = [1,5,9,7,5,3,2,5,8,4]

# 数列 a の a_2 から a_7 までの和を、累積和を使うことで求め、一行で出力してください。
cumulative_sum = [0] * (11)
for i in range(10):
    cumulative_sum[i+1] = A[i] + cumulative_sum[i]

ans = 0
for i in range(len(cumulative_sum)- 3):
    ans = max(ans, cumulative_sum[i+3] - cumulative_sum[i])
print(ans)
