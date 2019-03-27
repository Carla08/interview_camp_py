def find_contiguos_to_sort_subarray(arr):
    """
    Given an array of integers, find the continuous subarray, which when sorted,
    results in the entire array being sorted.
    For example: A = [0,2,5,3,1,8,6,9], result is the subarray [2,5,3,1,8,6]
    """
    start = 0
    end = len(arr) - 1
    start_return, end_return = start, end

    # start for finding the first mistmatch from start the end.
    # O(n)
    while start <= end:
        if arr[start + 1] < arr[start]:
            start_return = start
            break
        start += 1

    # search for the mismatch from end to start.
    # O(n)
    while end >= start:
        if arr[end - 1] > arr[end]:
            end_return = end
            break
        end -= 1

    # expand searching for minimum
    # O(n)
    _min = min(arr[start_return: end_return+1])
    for i, n in enumerate(arr[:start_return]):
        if n > _min:
            start_return = i
            break

    for i, n in enumerate(arr[end_return:]):
        if n < _min:
            end_return = i
            break

    # Total run time = O(n)
    return start_return, end_return

def move_zeros_to_end(arr):
    """
    Move all zeroes to the end of the given integer array.
    For example, if A = [2,3,0,3,0,1,0], Output = [2,3,3,1,0,0,0].
    """
    start = 0
    end = len(arr) - 1

    # O(n)
    while start <= end:
        if arr[start] != 0:
            start += 1
            continue
        if arr[end] == 0:
            end -= 1
            continue
        # if it got to this points means arr[start] == 0 and arr[end] != 0
        # swap
        arr[end], arr[start] = arr[start], arr[end]

    return arr
