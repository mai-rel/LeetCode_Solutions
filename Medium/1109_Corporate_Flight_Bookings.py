from typing import List


def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    diff = [0] * (n + 1)

    for first, last, seats in bookings:
        diff[first - 1] += seats
        diff[last] -= seats

    result = []
    total = 0

    for i in range(n):
        total += diff[i]
        result.append(total)

    return result