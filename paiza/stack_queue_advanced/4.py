import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

n = I()
books = collections.deque()

for i in range(n):
    q = LS()
    query = q[0]
    if query == "buy_book":
        x = int(q[1])
        books.append(x)
    else:
        y = int(q[1])
        while y:
            top_book = books.pop()
            if top_book == y:
                break
            if top_book > y:
                top_book-=y
                books.append(top_book)
                break
            else: # top_book < y
                y-=top_book

books_num = unread_p_num = 0
while books:
    books_num += 1
    unread_p_num+=books.pop()

print(books_num)
print(unread_p_num)
