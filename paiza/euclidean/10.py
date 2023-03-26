M, A = map(int, input().split())

def extGCD(a, b):
    if b:
        y, x = extGCD(b, a%b)
        y -= (a//b)*x
        return x, y
    return 1, 0


# M と互いに素である整数 A に対して、 A × N = 1(mod M) となる 1 以上 M 未満の整数 N が必ず存在し、
# この N を 「mod M での A の mod 逆元」といい、 A^{-1} (mod M) と書きます。
# mod M での A の mod 逆元を求めるには、 x , y についての 1 次方程式 Ax + My = 1 の 解 x が分かれば良いです。
# gcd(A,M) = 1 であるので、この方程式の解 x は拡張ユークリッドの互除法を用いることで求めることができます。

x, y = extGCD(A, M)
# 負の場合があるので、同じ数を足してそれの余りを求めると正の数になる。
x = (x+M) % M
print(x)
