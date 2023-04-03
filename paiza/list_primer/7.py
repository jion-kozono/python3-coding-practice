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

def delete(p):
    global back

    current_ptr = start_ptr
    while current_ptr != end_ptr:
        if current_ptr == p:
            next_ptr[current_ptr] = next_ptr[next_ptr[current_ptr]]
            break
        current_ptr = next_ptr[current_ptr]

def print_list_values():
    current_ptr = start_ptr
    while current_ptr != end_ptr:
        if current_ptr != start_ptr:
            print(value[current_ptr])
        current_ptr = next_ptr[current_ptr]


# 先頭から P 番目のノードを削除してください。
n, p= MI()
p-=1
value[start_ptr] = value[end_ptr] = -1
next_ptr[start_ptr] = end_ptr
next_ptr[end_ptr] = -1

for i in range(n):
    a = I()
    push_back(a)

delete(p)

print_list_values()
