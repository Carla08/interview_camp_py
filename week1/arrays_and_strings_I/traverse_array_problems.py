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




