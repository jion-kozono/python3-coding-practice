# https://paiza.jp/works/mondai/sort_efficient/sort_efficient__merge

# アルゴリズムが正しく実装されていることを確認するために導入するカウンタ変数、ソート処理には関係がないことに注意
count = 0
INF = 1000000001

# 部分データ列 A[left] ~ A[mid-1], A[mid] ~ A[right-1] はそれぞれ整列済み
# 2つの部分データ列をマージし、A[left] ~ A[right-1] を整列済みにする
def merge(A, left, mid, right):
    global count
    l = A[left:mid]
    r = A[mid:right]
    l.append(INF)
    r.append(INF)

    lindex = 0
    rindex = 0

    for i in range(left, right):
        if l[lindex] < r[rindex]:
            A[i] = l[lindex]
            lindex += 1
        else:
            A[i] = r[rindex]
            rindex += 1
            count += 1


# A[left] ~ A[right-1] をマージソートする
# 配列 A をマージソートするには merge_sort(A, 0, n) を呼び出す

def merge_sort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
A = list(map(int, input().split()))
merge_sort(A, 0, n)
print(*A)
print(count)
