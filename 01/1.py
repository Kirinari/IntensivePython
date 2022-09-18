def square_roots(a, b, c):
    D = (b ** 2 - 4 * a * c)
    if D >= 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return (x1, x2)
    return None

assert square_roots(1, -2, 1) == (1.0, 1.0)
assert square_roots(1, 2, 1) == (-1.0, -1.0)
assert square_roots(1, 1, 1) == None
assert square_roots(1, 0, 0) == (0.0, 0.0)
assert square_roots(1, 0, -4) == (2.0, -2.0)
assert square_roots(1, 4, 5) == None
