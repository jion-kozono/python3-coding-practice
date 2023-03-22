N, X = map(int, input().split())

# 計算量が2^Nとなる。
# burger = "P"

# for i in range(N):
#     burger = "B" + burger + "P" + burger + "B"

# print(burger[0:X].count("P"))

#レベルNはレベルN-1によって再起的に定義されている
# LN = 2LN-1 +3 (L0 = 1)
# SN = 2SN-1 +3 (S0 = 1)


# 計算量O(N)
def rec(N, X, L, S):
    if N == 0:
        return 1
    # Xの大きさに応じて場合分け
    # B Ln-1 P Ln-1 B
    # note: 条件分岐の基準はパティに到達するか
    if X==1: # Bだけなので0
        return 0
    # (B) Ln-1 Bは余計なのでX-1をした個数を求める
    elif X <= L[N-1] + 1:
        return rec(N-1, X-1, L, S)
    # B Ln-1 P でひとつ前の層の個数にひとつたす
    elif X == L[N-1]+2:
        return S[N-1]+1
    # (B Ln-1 P) Ln-1
    elif X <= L[N-1] * 2 + 2:
        return rec(N-1, X-L[N-1]-2, L, S)
    else:
        return S[N-1]*2 +1


L = [1] * (N+1)
S = [1] * (N+1)

for n in range(1, N+1):
    L[n] = L[n-1] * 2 + 3
    S[n] = S[n-1] * 2 + 1

# 再起的に求める
print(rec(N,X,L,S))
