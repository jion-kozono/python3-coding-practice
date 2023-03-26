# https://paiza.jp/works/mondai/euclidean_primer/euclidean_primer__fraction
a, b, cal, c, d = input().split()
a,b,c,d = map(int, [a,b,c,d])

def gcd(x,y):
    return gcd(y, x%y) if x % y else y

numerator = denominator = 0
if (cal == '+'):
    numerator = a * d + b * c
    denominator = b * d
elif (cal == '-'):
    numerator = a * d - b * c
    denominator = b * d
elif (cal == '*'):
    numerator = a * c
    denominator = b * d
else:
    numerator = a * d
    denominator = b * c

if (numerator == 0):
    denominator = 1
else:
    div = gcd(abs(numerator), abs(denominator))
    numerator //= div
    denominator //= div
    if (denominator < 0):
    # 分母が0の場合は分子、分母ともに符号を逆転する
      denominator *= -1
      numerator *= -1

print(numerator, denominator)
