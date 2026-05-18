from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if not n:
        return True

    length = len(flowerbed)
    if length == 1:
        if flowerbed[0]:
            return False
        return 1 >= n

    i = 0
    count = 0

    while i < length:
        if flowerbed[i]:
            i += 2
        elif i > 0 and flowerbed[i - 1]:
            i += 1
        elif i < length - 1 and flowerbed[i + 1]:
            i += 3
        else:
            count += 1
            i += 2

    return count >= n
