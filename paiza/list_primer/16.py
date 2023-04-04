value = [None] * 1024
next_ptr = [None] * 1024
prev_ptr = [None] * 1024
empty_min_idx = 1  # まだ使用していない配列の要素で、最も小さいインデックス
start_ptr = 0  # リストの先頭のインデックス
end_ptr = 1023  # リストの末尾の次のインデックス

def push_back(a):
    global empty_min_idx
    new_ptr = empty_min_idx
    value[new_ptr] = a
    empty_min_idx += 1
    prev_last = prev_ptr[end_ptr]
    prev_ptr[new_ptr] = prev_last
    next_ptr[new_ptr] = end_ptr
    next_ptr[prev_last] = new_ptr
    prev_ptr[end_ptr] = new_ptr

def delete(l,r):
    current_ptr = start_ptr
    for i in range(l):
        if current_ptr == end_ptr:
            break
        current_ptr = next_ptr[current_ptr]

    if current_ptr != end_ptr:
        range_next_ptr = current_ptr  # 区間の削除直後のインデックス
        for i in range(r -l+1):
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

n, l, r = map(int, input().split())
l -= 1
r -= 1
value[start_ptr] = -1
value[end_ptr] = -1
next_ptr[start_ptr] = end_ptr
next_ptr[end_ptr] = -1
prev_ptr[end_ptr] = start_ptr
prev_ptr[start_ptr] = -1

for i in range(n):
    a = int(input())
    push_back(a)

delete(l,r)

print_list_values()
