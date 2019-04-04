
def get_combos_helper(arr, buffer, start_index, buffer_index):
    if buffer_index == len(buffer):
        yield buffer
    elif start_index == len(arr):
        return
    else:
        for i in range(start_index, len(arr)):
            buffer[buffer_index] = arr[i]
            yield from get_combos_helper(arr, buffer, i + 1, buffer_index + 1)

def get_combos_length_n(arr, n):
    buffer = [None] * n
    yield from get_combos_helper(arr, buffer, 0, 0)


num_char_map = {2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y']}

def phone_to_word_helper(num_arr, buffer, arr_index, buff_index):
    if buff_index == len(buffer):
        yield buffer
    elif arr_index == len(num_arr):
        return
    else:
        for i in range(arr_index, len(num_arr)):
            num = num_arr[i]
            if num in num_char_map:
                for char in num_char_map[num]:
                    buffer[buff_index] = char
                    yield from phone_to_word_helper(num_arr, buffer, arr_index + 1, buff_index + 1)
                buff_index -= 1

def phone_to_num(nums):
    buffer = [None] * len(nums)
    yield from phone_to_word_helper(nums, buffer, 0, 0)


def get_permutations_helper(arr, buffer, buff_index, _n):
    if buff_index == len(buffer):
        yield buffer
    else:
        for n in arr:
            if n not in buffer:
                buffer[buff_index] = n
                yield from get_permutations_helper(arr, buffer, buff_index + 1, _n)
                buffer.remove(n)
                buffer.append(None)

def get_permutations_length_n(arr, n):
    buffer = [None] * n
    yield from get_permutations_helper(arr, buffer, 0, n)


def get_all_subsets_helper(_set, subset, arr_index):
    yield subset
    if arr_index == len(_set):
        return
    else:
        for i in range(arr_index, len(_set)):
            subset.append(_set[i])
            yield from get_all_subsets_helper(_set, subset, i + 1)
            subset.remove(_set[i])
            #arr_index -= 1

def get_all_subsets(arr):
    yield from get_all_subsets_helper(arr, [], 0)
