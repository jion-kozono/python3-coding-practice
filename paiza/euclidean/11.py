
# 整数 A , B , M が与えられるので、 A^B(mod M) を求めましょう。

# まず b の 2 進数表現を考えます。b の最下位の桁が 2 かどうかを確認します。
# 最下位の桁が 1 の場合、 a を ans にかけます。
# この処理が終わったら、a を a の 2 乗に置き換え、b を右に 1 ビットシフト(もしくは ÷2)します。
# これを b が 0 以下になるまで繰り返すことで、i 回目のときに、a ^ (2 ^ (i - 1)) のかけ算を行うことができます。
def modpow(a, b, m):
    ans = 1
    while (0 < b):
        if (b & 1):
            ans = (ans * a) % m

        a = (a * a) % m
        b >>= 1

    return ans

A, B, M = map(int, input().split())

print(modpow(A, B, M))
