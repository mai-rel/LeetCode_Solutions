from typing import List
from collections import defaultdict


def gardenNoAdj(n: int, paths: List[List[int]]) -> List[int]:
    graph = defaultdict(list)

    for a, b in paths:
        graph[a].append(b)
        graph[b].append(a)

    answer = [0] * n

    for garden in graph:
        allowed_types = [True, True, True, True]

        for near_garden in graph[garden]:
            flower_type = answer[near_garden - 1]
            if flower_type:
                allowed_types[flower_type - 1] = False

        current_type = allowed_types.index(True) + 1
        answer[garden - 1] = current_type

    for i in range(n):
        if not answer[i]:
            answer[i] = 1

    return answer