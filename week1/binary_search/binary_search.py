
def binary_search(arr, element):
    # NOTE: arr should be sorted
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2  # to avoid overflow
        if arr[mid] < element:
            start = mid + 1
            continue
        elif arr[mid] > element:
            end = mid - 1
        else:
            # arr[mid] = element. Found it!
            return mid

    return None


def binary_search_duplicates(arr, element):
    # NOTE: arr should be sorted
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2  # to avoid overflow
        if arr[mid] < element:
            start = mid + 1
            continue
        elif arr[mid] > element:
            end = mid - 1
        else:
            # keep searching backwards until finding the first occurrence.
            while arr[mid - 1] == element:
                mid -= 1
            return mid

    return None
