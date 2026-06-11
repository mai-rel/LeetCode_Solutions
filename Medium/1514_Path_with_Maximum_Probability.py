from typing import List
from collections import defaultdict
import heapq


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                   end_node: int) -> float:
    graph = defaultdict(list)

    for i, verts in enumerate(edges):
        v1, v2 = verts
        graph[v1].append((i, v2))
        graph[v2].append((i, v1))

    heap = []
    heapq.heappush(heap, (-1, start_node))

    probs = [0] * n
    probs[start_node] = 1

    while heap:
        prob, vertex = heapq.heappop(heap)
        prob *= (-1)
        if probs[vertex] > prob:
            continue

        for index, next_vertex in graph[vertex]:
            next_prob = succProb[index]
            new_prob = prob * next_prob
            if probs[next_vertex] >= new_prob:
                continue
            probs[next_vertex] = new_prob
            heapq.heappush(heap, (-new_prob, next_vertex))

    return probs[end_node]