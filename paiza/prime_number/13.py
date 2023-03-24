def is_prime(x: int) -> bool:
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


ans = []
# 平方数が偶数の時はゴールドバッハ予想より2 つの素数の和で表すことができる。
# 以下平方数が奇数の時を考える
# 2 つの整数の和が奇数になるのは「偶数 + 奇数」の場合のみであり、素数のうち偶数のものは 2 のみである。
# よって、N が 2 つの素数の和で表されるとき、「N = 2 + 素数」の形であるので、N - 2 が素数の場合のみ N は paiza 予想を満たす。
for i in range(3, int((10 ** 8) ** 0.5) + 1, 2):
    N = i*i
    if not is_prime(N - 2):
        ans.append(N)

if len(ans) == 0:
    print("paiza's conjecture is correct.")
else:
    for a in ans:
        print(a)
