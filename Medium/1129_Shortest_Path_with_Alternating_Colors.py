from typing import List
from collections import deque, defaultdict


def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    graph = defaultdict(lambda: defaultdict(list))
    visited = set()

    for u, v in blueEdges:
        graph[u]['blue'].append(v)

    for u, v in redEdges:
        graph[u]['red'].append(v)

    queue = deque()

    dist = [-1] * n
    dist[0] = 0

    for color in ['blue', 'red']:
        for v in graph[0][color]:
            queue.append((v, color))
            visited.add((v, color))

    d = 1

    while queue:

        for _ in range(len(queue)):
            v, color = queue.popleft()
            if dist[v] == -1:
                dist[v] = d
            else:
                dist[v] = min(dist[v], d)

            next_color = 'red' if color == 'blue' else 'blue'

            for next_v in graph[v][next_color]:
                if v == 0 or (next_v, next_color) in visited:
                    continue

                visited.add((next_v, next_color))
                queue.append((next_v, next_color))

        d += 1

    return dist
