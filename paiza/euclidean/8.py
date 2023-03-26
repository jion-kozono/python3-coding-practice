N, A = map(int, input().split())

# 自然数 N と整数 A が与えられるので、1 〜 100,000 の数のうち、N を法として A と合同なもの（A を含む）を、小さい方から順に全て出力してください。

for i in range(1, 100001):
    if A % N == i % N:
        print(i)
