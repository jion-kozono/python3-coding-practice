import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

value = [None] * 1024
next_ptr = [None] * 1024
empty_min_idx = 1  # まだ使用していない配列の要素で、最も小さいインデックス
back = 0  # 末尾の要素の一つ前の要素のインデックスを保持する変数
start_ptr = 0  # リストの開始のインデックス
end_ptr = 1023  # リストの末尾の次のインデックス

def push_back(a):
    global empty_min_idx, back

    # 新しいポインタを作成
    new_ptr = empty_min_idx
    empty_min_idx+=1
    value[new_ptr] = a
    next_ptr[new_ptr] = end_ptr

    # 繋ぎかえ
    next_ptr[back] = new_ptr
    back = new_ptr

def delete(l, r):
    current_ptr = start_ptr
    for _ in range(l):  # 削除したい区間の直前まで移動する
        if current_ptr == end_ptr:  # current_ptr がリストのサイズより大きい場合
            break
        current_ptr = next_ptr[current_ptr]

    if current_ptr != end_ptr:
        range_next_ptr = current_ptr  # 区間の削除直後のインデックス
        for _ in range(r-l+1):
            if range_next_ptr == end_ptr:
                break
            range_next_ptr = next_ptr[range_next_ptr]
        next_ptr[current_ptr] = range_next_ptr

def print_list_values():
    current_ptr = start_ptr
    while current_ptr != end_ptr:
        if current_ptr != start_ptr:
            print(value[current_ptr])
        current_ptr = next_ptr[current_ptr]


# 先頭から数えて L 番目のノードから R - 1 番目のノードをすべて削除してください。 L = R のときは何もしなくてよいです。
n, l, r= MI()
l-=1
r-=1
value[start_ptr] = value[end_ptr] = -1
next_ptr[start_ptr] = end_ptr
next_ptr[end_ptr] = -1

for i in range(n):
    a = I()
    push_back(a)

delete(l, r)

print_list_values()
