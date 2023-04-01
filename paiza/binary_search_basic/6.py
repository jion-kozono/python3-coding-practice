n, k = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

def is_ok(x):
    # 単位価値がx以上となる選び方は存在するか？
    # (k個の財宝の価値の和) ÷ (k個の財宝の重さの和)
    # (v_1 + v_2 + ... + v_k) / (w_1 + w_2 + ... + w_k) ≧ x
    # (v_1 + v_2 + ... + v_k) - x * (w_1 + w_2 + ... + w_k) ≧ 0
    # (v_1 - x*w_1) + (v_2 - x*w_2) + ... + (v_k - x*w_k) ≧ 0

    VXW = [vi - x * wi for vi, wi in zip(V, W)]
    # 降順に並べ替える
    VXW.sort(reverse=True)
    return sum(VXW[:k]) >= 0

def binary_search(ng, ok):
    while (abs(ok - ng) > 10**-6):  # 絶対誤差小数8桁程度
        mid = (ok + ng) / 2 # 少数を含むので//でなくて良い
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search(5001,0))
