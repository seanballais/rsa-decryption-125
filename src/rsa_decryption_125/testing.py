import math

def obtain_pq(n):
    p = 0.1
    k = math.ceil(math.sqrt(n))
    while not p.is_integer():
        p = k - math.sqrt((k ** 2) - n)
        k += 1

    p = int(p)

    return p, n // p

def extended_euclidean_algorithm(b, a):
    # Code from:
    # https: // en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    # Still trying to understand the math behind this.
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return  b, x0, y0

def solve_linear_congruence(a, b, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if b % gcd > 0:
        # No solutions.
        return None

    return (x * b) % m

a = int(input('a = '))
b = int(input('b = '))
m = int(input('m = '))

solution = solve_linear_congruence(a, b, m)

print('Solution: x = {}'.format(solution))