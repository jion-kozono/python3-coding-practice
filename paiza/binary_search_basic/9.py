# https://paiza.jp/works/mondai/binary_search/binary_search__application_boss

# 数列 A = (A_1, A_2, ..., A_n) と数列 B = (B_1, B_2, ..., B_m) が与えられます。
# これらの数列を用いて、n 行 m 列のマス目に数を書き込むことを考えます。具体的には、i 行 j 列目(1 ≦ i ≦ n, 1 ≦ j ≦ m) に | A_i - B_j | を書き込みます。
# 表に書き込まれる数は全部で n*m 個ありますが、それらを小さいほうから並べたとき k 番目にくる値を求めてください。

def binary_search(A, n, k):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if A[mid] < k:
            left = mid + 1
        else:
            right = mid

    return right


n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]
k = int(input())

B.sort()
left, right = -1, 200000000
while right - left > 1:
    mid = (left + right) // 2
    smaller = 0
    for i in range(n):
        smaller += binary_search(B, len(B), A[i] + mid + 1) - binary_search(
            B, len(B), A[i] - mid
        )

    if smaller < k:
        left = mid
    else:
        right = mid

print(right)
