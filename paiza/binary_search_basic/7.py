# https://paiza.jp/works/mondai/binary_search/binary_search__application_step2

# 長さ L [cm] の太巻きがあり、これを n 人で分けようとしています。太巻きにはあらかじめ k 個の切れ目が入っており、i 個目の切れ目は左端から A_i [cm] のところに入っています。あなたは、切れ目を n-1 個選んでそこで切ることにより、太巻きを n 分割しようとしています。n 人はみなお腹がすいているので、なるべくたくさん食べたいと思っています。切れ目の選び方を工夫したとき、最も短い太巻きの長さを最大でいくつにできるかを答えてください。

L, n, k = map(int, input().split())
A = [int(x) for x in input().split()]

A = [0] + A + [L]
left, right = 0, L+1
while abs(right - left) > 1:
    mid = (left + right) // 2

    last_index, parts = 0, 0
    for i in range(k + 2):
        if A[i] - A[last_index] >= mid:
            parts += 1
            last_index = i

    if parts < n:
        right = mid
    else:
        left = mid

print(left)
