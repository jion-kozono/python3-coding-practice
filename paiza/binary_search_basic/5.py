# https://paiza.jp/works/mondai/binary_search/binary_search__application_step0

n,k = map(int, input().split())
A = list(map(int,input().split()))

left = 0.0
right = 10001.0
for i in range(100):
    num_of_pipes = 0
    mid = (left + right)/2
    # 作れるパイプの数を数える
    for a in A:
        num_of_pipes += a // mid # 本数は整数である必要がある
    if num_of_pipes < k: # k本切り出せない場合、探索範囲を、１本あたりの長さが小さいほうに絞る
        right = mid
    else: # k本以上切り出せる場合、探索範囲を、１本あたりの長さが大きいほうに絞る
        left = mid
print(left)
