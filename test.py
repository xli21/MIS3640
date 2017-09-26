def fact(n):
    result = 1
    if n == 1:
        return result
    print('curent n =', n)
    result = n * fact(n - 1)
    return result


print(fact(7))
