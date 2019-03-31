
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


def binary_search_closest(arr, number):
    # NOTE: arr should be sorted
    start = 0
    end = len(arr) - 1
    closest = 100000000  # hardcoded huge value to avoid check for None on first iter.

    while start <= end:
        mid = start + (end - start) // 2  # to avoid overflow
        element = arr[mid]
        closest = mid if abs(number-element) < closest else closest
        if element < number:
            start = mid + 1
            continue
        elif element > number:
            end = mid - 1
        else:
            # keep searching backwards until finding the first occurrence.
            while arr[mid - 1] == number:
                mid -= 1
            return mid

    return closest


def find_min_in_cycled_arr(arr):
    # NOTE: arr may be cycled. but sorted.
    start = 0
    end = len(arr) - 1
    right = arr[end]

    while start <= end:
        mid = start + (end - start) // 2  # to avoid overflow
        if arr[mid] < right and (mid == 0 or arr[mid -1] > arr[mid]):
            return mid
        elif arr[mid] > right:
            start = mid + 1
        elif arr[mid] < right:
            end = mid - 1

    return mid


def binary_search_unknown_length(arr, element):
    # NOTE: arr should be sorted
    # do binary search for finding end.
    start, end = 0, 1
    end_found, limit = False, None
    while start < end:
        try:
            arr[end]
            start = end
            if not end_found:
                end *= 2
            else:
                end = (end + limit) // 2
        except IndexError:
            # end should be between prev and possible_end
            end_found = True
            limit = end
            end =(start + end) // 2

    # find the element
    start = 0
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
