import math
with open('crypto/Substitution Cipher I/output.txt') as f:
    OUTPUT = f.read().strip()


def solve(y: int) -> int:
    # 13*(x**2) + 3*(x) + (7 - y) = 0
    # x = (-3 + √(9 + 4*13*(y - 7)))/26
    D = math.isqrt((9 + 4*13*(y - 7)))
    return (-3 + D)//26


print(''.join([chr(solve(ord(c))) for c in OUTPUT]))
