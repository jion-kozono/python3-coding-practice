# https:#paiza.jp/works/mondai/sort_efficient/sort_efficient__shell

def insertion_sort(A,n,h):
    num_of_move = 0
    for i in range(h, n):
        # A[i] を、整列済みの A[i-ah], ..., A[i-2h], A[i-h] の適切な位置に挿入する
        # 実装の都合上、A[i] の値が上書きされてしまうことがあるので、予め A[i] の値をコピーしておく
        x = A[i]

        # A[i] の適切な挿入位置を表す変数 j を用意
        j = i-h

        # A[i] の適切な挿入位置が見つかるまで、A[i] より大きい要素を後ろにずらしていく
        while j >= 0 and A[j] > x:
            A[j+h] = A[j]
            j -= h
            num_of_move+=1

        # A[i] を挿入
        A[j+h] = x
    print(num_of_move)


def shell_sort(A, n, H):
    for h in H:
        insertion_sort(A, n, h)

n = int(input())
A = list(map(int, input().split()))
k = int(input())
H = list(map(int, input().split()))

shell_sort(A, n, H)
