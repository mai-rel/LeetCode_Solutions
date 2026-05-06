from typing import List
from collections import defaultdict


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(set)

    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    ranks = {city: len(connected_cities) for city, connected_cities in graph.items()}

    max_rank = 0

    for city in range(n):
        if not graph[city]:
            continue

        rank = ranks[city]

        for city2 in range(city + 1, n):
            if not graph[city2]:
                continue

            rank2 = ranks[city2]
            rank_of_two = rank + rank2

            if city2 in graph[city]:
                rank_of_two -= 1

            max_rank = max(max_rank, rank_of_two)

    return max_rank