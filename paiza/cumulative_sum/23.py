# https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__1d_imos_step1

n, range_n = 10, 5
# 1 マス目から 3 マス目
# 1 マス目から 8 マス目
# 3 マス目から 8 マス目
# 3 マス目から 6 マス目
# 7 マス目から 9 マス目

# [[1,3],[1,8],...,[7,9]]
squares = [0 for _ in range(n)]
ranges = [[1,3],[1,8],[3,8],[3,6],[7,9]]

for start, end in ranges:
    squares[start-1] +=1
    squares[end] -= 1

cumulative_sum = [0] * (n+1)
for i in range(n):
    cumulative_sum[i+1] = cumulative_sum[i] + squares[i]

print(max(cumulative_sum))

# 模範回答
a = [0] * 11
L = [1, 1, 3, 3, 7]
R = [3, 8, 8, 6, 9]

for i in range(5):
    a[L[i] - 1] += 1
    a[R[i]] -= 1

for i in range(10):
    a[i + 1] += a[i]

print(max(a))
