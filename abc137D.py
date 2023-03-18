from heapq import heappop, heappush

N, M = map(int, input().split())

# AtoB[v] : A[i] = v となる i に対する B[i] の集合
AtoB = [[] for i in range(M+1)]
for i in range(N):
    # 仕事の入力
    A, B = map(int, input().split())

    # 報酬支払いはM日を超える場合は無意味
    if A > M:
        continue

    # データ登録
    AtoB[A].append(B)

# 報酬の最大値を表す変数
result = 0

que = []

# M-1日目から0日目へと遡る (AtoB[0]から順にみる)
for Bs in AtoB:
    # ヒープに遡った分の仕事を追加する
    for B in Bs:
        # Python3 のヒープは小さい順なので符号反転して追加
        heappush(que, -B)

    # ヒープが空でなければ報酬最大の仕事を答えに足す
    if que:
        result -= heappop(que)

print(result)
