# https://paiza.jp/works/mondai/binary_search/binary_search__application_step3

# 長さ L [cm] の太巻きがあり、これを n 人で分けようとしています。太巻きにはあらかじめ k 個の切れ目が入っており、i 個目の切れ目は左端から A_i [cm] のところに入っています。あなたは、切れ目を n-1 個選んでそこで切ることにより、太巻きを n 分割しようとしています。n 人はみなお腹がいっぱいなので、なるべく少なく食べたいと思っています。切れ目の選び方を工夫したとき、最も長い太巻きの長さを最小でいくつにできるかを答えてください

L, n, k = map(int, input().split())
A = [int(x) for x in input().split()]

A = [0] + A + [L]
left, right = 0, L
for i in range(1, k + 2):
    left = max(left, A[i] - A[i - 1])

left -= 1
while right - left > 1:
    mid = (left + right) // 2

    last_index, index, parts = 0, 0, 0
    while True:
        while index + 1 < k + 2 and A[index + 1] - A[last_index] <= mid:
            index += 1
        parts += 1
        if index == k + 1:
            break
        last_index = index
    if parts > n:
        left = mid
    else:
        right = mid

print(right)
