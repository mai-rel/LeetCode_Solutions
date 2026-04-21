from typing import List
from math import inf

def maximize_expression_of_three(nums: List[int]) -> int:
    max_num1 = -inf
    max_num2 = -inf
    min_num = inf

    for num in nums:
        if num >= max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif num > max_num2:
            max_num2 = num

        min_num = min(min_num, num)

    return max_num1 + max_num2 - min_num