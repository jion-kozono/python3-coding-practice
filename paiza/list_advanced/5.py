import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
keys = LS()
letters = []
cursor_idx = 0
for i in range(N):
    # Left, Right が入力されたときはカーソルを左右に移動させます。移動できない場合は何もしません。
    if keys[i] == "Left":
        if cursor_idx != 0:
            cursor_idx-=1
    elif keys[i] == "Right":
        if cursor_idx != len(letters):
            cursor_idx+=1
    # Delete が入力されたときはカーソルの左隣の文字を 1 つ削除します。カーソルの左隣に文字が存在しない場合は何もしません。
    elif keys[i] == "Delete":
        if cursor_idx != 0:
            cursor_idx -= 1
            letters.pop(cursor_idx)
    # 半角アルファベット小文字が入力されたときは現在のカーソルのすぐ左隣に文字を挿入します。
    else:
        letters.insert(cursor_idx, keys[i])
        cursor_idx+=1

print(*letters)
