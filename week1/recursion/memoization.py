
def x_power_n(x, n, memo_map):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n in memo_map:
        return memo_map[n]
    else:
        n1 = n//2
        n2 = n//2 if n % 2 == 0 else n//2 + 1
        res = x_power_n(x, n1, memo_map) * x_power_n(x, n2, memo_map)
        memo_map[n] = res
        return res
