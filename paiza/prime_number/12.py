m1,m2,b1,b2 = map(int, input().split())

# 「m1 と m2 を互いに素な正の整数とする。
# Z を m1 で割った余りが b1 であり、Z を m2 で割ったあまりが b2 であるような整数 Z が 0 以上 m1 × m2 未満にただ 1 つ存在する。」

# Z % m1 == b1 and Z % m2 == b2
n = m1 * m2
for Z in range(n):
    if  Z % m1 == b1 and Z % m2 == b2:
        print(Z)
        break

# 模範解答
# https://paiza.jp/works/mondai/reviews/show/cb5a2c7337be96e76a91c4247facb9ec

# 0 以上 m1 × m2 未満の全ての数について m1 , m2 で割った余りが b1 , b2 かどうかを調べると、制約より計算回数が最悪ケースで 10,000,000,000 回となってしまい実行時間制限に間に合いません。
# 0 以上 m1 × m2 未満の整数のうち、 m1 で割った余りが b1 になるような整数 Z は Z = m1 * i + b1 (0 ≦ i < m2)という形で表すことができ、その個数は m2 個です。この m2 個の各整数について m2 で割った余りが b2 になるかどうかを調べることでこの問題を最大 100,000　回程度の計算で解くことができます。
for i in range(m2):
    Z = m1 * i + b1
    if Z % m2 == b2:
        print(Z)
        break
