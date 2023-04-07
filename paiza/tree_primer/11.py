def calc_length(now: int):
    for nxt in g[now]:
        if len_from_T[nxt] == -1:
            len_from_T[nxt] = len_from_T[now] + 1
            parent[nxt] = now
            calc_length(nxt)

# ・1 行目には、山のチェックポイントの数 N, 山の頂点に割り当てられたチェックポイントの番号 T, paiza 君が出発したチェックポイントの番号 S, paiza 君が山を登った回数 C, 降りた回数 D が与えられます。
# ・続く N-1 行では、山の N-1 本の道の両端のチェックポイントの番号が与えられます。
N, T, S, C, D = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

parent = [0] * N
parent[T - 1] = -1
len_from_T = [-1] * N
len_from_T[T - 1] = 0

calc_length(T - 1)

# スタート地点から頂点までの距離を len_from_T[s], 登る回数を x, 降りる回数を y とすると答えは次のように決定します。
# x >= len_from_T[s] なら 根から y - (x - len_from_T[s]) 回降りた位置すべてが答えになる
if len_from_T[S - 1] <= C:
    for i in range(N):
        if len_from_T[i] == len_from_T[S - 1] - C + D:
            print(i + 1)
# x < len_from_T[s] なら s から x 回登った地点(これは一意に決まります)から y 回降りた位置すべてが答えになる
else:
    # highest に到達しうる最も高いチェックポイントの番号を格納し、各頂点について、高さがあっているかどうかとその頂点から一番高く登った時のチェックポイントが highest に一致するかどうかでその頂点が到達し得るかどうかを判定しています。
    highest = S - 1
    for i in range(C):
        highest = parent[highest]

    for i in range(N):
        if len_from_T[i] == len_from_T[S - 1] - C + D:
            ancestor = i
            for j in range(D):
                ancestor = parent[ancestor]

            if ancestor == highest:
                print(i + 1)
