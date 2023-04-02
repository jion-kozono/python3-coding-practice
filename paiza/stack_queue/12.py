import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
A = LI()

st = []

for i in range(N):
    st.append(A[i])
    while len(st) >= 2:
        top1 = st[-1]  # スタックの上から一番目
        st.pop()
        top2 = st[-1]  # スタックの上から二番目
        st.pop()
        if top1 == top2:
            st.append(2 * top2)
        else:
            st.append(top2)
            st.append(top1)
            break


while len(st) > 0:
    print(st[-1])
    st.pop()
