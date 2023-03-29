A = [1,5,9,7,5,3,2,2,8,4]

# 数列 a の a_2 から a_7 までの和を、累積和を使うことで求め、一行で出力してください。
cumulative_sum = [0] * (11)
for i in range(10):
    if A[i] % 2 == 0:
        cumulative_sum[i+1] = cumulative_sum[i] + 1
    else:
        cumulative_sum[i+1] = cumulative_sum[i]

print(cumulative_sum[8] - cumulative_sum[2])
