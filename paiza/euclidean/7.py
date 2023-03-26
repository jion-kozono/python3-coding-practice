
def gcd(x,y):
    return gcd(y, x%y) if x % y else y

N, A = map(int, input().split())

# https://paiza.jp/works/mondai/euclidean_primer/euclidean_primer__nasty_sugoroku
# -A , -B , 0 , 0 , A , B の 6 つの目の出た回数をそれぞれ a 〜 f とすると、移動したマス数は -Aa-Bb+Ae+Bfとなります。
# これを整理すると A(e-a) + B(f-b) となります。

# a 〜 f は回数であり整数であるので、e-a , f-b は整数となります。
# よって、paiza 君が移動したマス数は、ある整数 x , y を用いて、 Ax + By と表すことができます。

# paiza 君がゴールするための条件は、移動の結果 N マスちょうど進むことができること、すなわち Ax + By = Nを満たす整数の組 (x , y) が存在することです。

# ここで、paiza 君が移動できる最小のマス数を考えます。Ax + By = Nを満たす (x , y) が存在するときの最小の N の値は gcd(A , B) であるから、paiza君の最小の移動のマス数は gcd(A , B) となります。つまり、paiza くんが移動できるのは gcd(A, B) の倍数マスのみです。よって N が gcd(A , B) の倍数マスでない、つまり N が gcd(A, B)で割り切れない時 paiza 君はゴールすることができません。

none = True
for i in range(1, 1001):
    min_move = gcd(A, i)
    if N % min_move != 0 and i != A:
        print(i)
        none = False
if none: print(-1)
