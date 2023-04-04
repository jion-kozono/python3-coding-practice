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

n, p = map(int, input().split())
p -= 1
value[start_ptr] = -1
value[end_ptr] = -1
next_ptr[start_ptr] = end_ptr
next_ptr[end_ptr] = -1
prev_ptr[end_ptr] = start_ptr
prev_ptr[start_ptr] = -1

for i in range(n):
    a = int(input())
    push_back(a)

delete(p)

print_list_values()
