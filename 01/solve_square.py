import math
def square_roots(a, b, c):
    D = (b ** 2 - 4 * a * c)
    if math.isclose(D, 0.0, rel_tol=1e-20) or D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return (x1, x2)
    return None

def checker(a, b, c, sols):
    x = square_roots(a, b, c)
    
    if x is None:
        return sols is None
    
    return math.isclose(x[0], sols[0], rel_tol=1e-20) and \
           math.isclose(x[1], sols[1], rel_tol=1e-20)       

assert checker(1, -2, 1, (1.0, 1.0))
assert checker(1, 2, 1, (-1.0, -1.0))
assert checker(1, 1, 1, None)
assert checker(1, 0, 0, (0.0, 0.0))
assert checker(1, 0, -4, (2.0, -2.0))
assert checker(1, 4, 5, None)
