from typing import List


def numTeams(rating: List[int]) -> int:
    teams = 0
    n = len(rating)

    smaller_rates_before = [0] * n
    greater_rates_before = [0] * n

    for i in range(n):
        for j in range(i):
            if rating[j] < rating[i]:
                teams += smaller_rates_before[j]
                smaller_rates_before[i] += 1
            elif rating[j] > rating[i]:
                teams += greater_rates_before[j]
                greater_rates_before[i] += 1

    return teams