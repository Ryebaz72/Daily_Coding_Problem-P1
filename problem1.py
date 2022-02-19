def add_two_to_give_k(num_list, k):
    list_len = len(num_list)
    a = 0
    b = 0
    n = (list_len - 1) ** 2
    while a < n:
        while b < list_len:
            if num_list[a] + num_list[b] == k:
                print(f'{num_list[a]} + {num_list[b]} = {k}')
                return True
            b += 1
        a += 1
    return False

if __name__ == '__main__':
    num_list = [10, 15, 3, 6, 5, 8]
    k = 18
    answer = add_two_to_give_k(num_list, k)
    print(answer)