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

def insert(p,x):
    global empty_min_idx
    new_ptr = empty_min_idx
    empty_min_idx += 1
    value[new_ptr] = x
    current_ptr = start_ptr
    for i in range(p):
        if current_ptr == end_ptr:
            break
        current_ptr = next_ptr[current_ptr]
    if current_ptr != end_ptr:
        next = next_ptr[current_ptr]
        prev_ptr[next] = new_ptr
        next_ptr[current_ptr] = new_ptr
        next_ptr[new_ptr] = next
        prev_ptr[new_ptr] = current_ptr

def delete(p):
    current_ptr = start_ptr
    for i in range(p+1):
        if current_ptr == end_ptr:
            break
        current_ptr = next_ptr[current_ptr]
    if current_ptr != end_ptr:
        front = next_ptr[current_ptr]
        back = prev_ptr[current_ptr]

        next_ptr[back] = front
        prev_ptr[front] = back

def print_list_values():
    current_ptr = start_ptr
    while current_ptr != end_ptr:
        if current_ptr != start_ptr:
            print(value[current_ptr])
        current_ptr = next_ptr[current_ptr]

n, q = map(int, input().split())

value[start_ptr] = -1
value[end_ptr] = -1
next_ptr[start_ptr] = end_ptr
next_ptr[end_ptr] = -1
prev_ptr[end_ptr] = start_ptr
prev_ptr[start_ptr] = -1

for i in range(n):
    a = int(input())
    push_back(a)

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1:]
        p-=1
        insert(p,x)
    else:
        p = query[1]
        p-=1
        delete(p)

print_list_values()
