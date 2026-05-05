from typing import List
from collections import defaultdict, deque


def get_distances(v, graph, n):
    dist = [0] * n
    visited = set()
    visited.add(v)
    queue = deque([v])
    d = 0

    while queue:
        d += 1

        for _ in range(len(queue)):
            node = queue.popleft()
            for next_node in graph[node]:
                if next_node in visited:
                    continue
                dist[next_node] = d
                visited.add(next_node)
                queue.append(next_node)

    return dist


def specialNodes(n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    x_dist = get_distances(x, graph, n)
    y_dist = get_distances(y, graph, n)
    z_dist = get_distances(z, graph, n)

    count = 0

    for i in range(n):
        values = [x_dist[i], y_dist[i], z_dist[i]]
        values.sort()
        a, b, c = values
        if a ** 2 + b ** 2 == c ** 2:
            count += 1

    return count