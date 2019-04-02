
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