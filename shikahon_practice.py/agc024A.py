A, B, C, K = map(int, input().split())

# answer: A - B
# (A, B, C) => (B+C, A+C, A+B)
# AとBの差は B+C - (A+C) = B - A
# つまり周期はA-BからB-Aに変化していて、一度の操作で-1倍される
# kが偶数の時はA-B, 奇数の時はB-Aとなることがわかる。
print(A-B if K % 2 == 0 else B-A)
