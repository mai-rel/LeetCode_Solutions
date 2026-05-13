from typing import List


def decimalRepresentation(n: int) -> List[int]:
    result = []
    degree = 0

    while n > 0:
        last_digit = n % 10
        if last_digit != 0:
            result.append(last_digit * (10 ** degree))
        n //= 10
        degree += 1

    return result[::-1]