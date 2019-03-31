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


def mexican_flag(arr):
    """
    Given an array with n objects colored Red, White or Green, sort them so that objects
    of the same color are adjacent, with the colors in the order Red, White and Green.
    Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Green).
    For example, if A = [1,0,1,2,1,0,1,2], Output = [0,0,1,1,1,1,2,2].
    """
    # HARDCODED PIVOT:
    pivot = 1
    low = 0
    high = len(arr) - 1
    mid = 0

    while mid <= high:
        to_place = arr[mid]
        if to_place > pivot:
            arr[mid],arr[high] = arr[high], arr[mid]
            high -= 1
        elif to_place == pivot:
            mid += 1
        elif to_place < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        print(arr)
    return arr


def find_contiguos_subarray_sums_x(arr, x):
    # NOTE: Find one contiguos subarray which sums x. To find all subarrays
    # it's a DP problem not covered here.
    # create common diff arr
    # O(n)
    common_diff = []
    diff_map = {}
    for i,n in enumerate(arr):
        try:
            diff = common_diff[i - 1] + n
            common_diff.append(diff)
            diff_to_x = diff - x
            if diff == x:
                print(0, i)
                return 0, i
            elif diff_to_x in diff_map:
                print(diff_map[diff_to_x] + 1, i)
                return diff_map[diff_to_x] + 1, i
            else:
                diff_map[diff] = i
        except IndexError:
            common_diff.append(n)
            diff_map[n] = i
            continue
