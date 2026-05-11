from collections import deque, defaultdict
import heapq
from typing import List


def form_groups(graph, v, station_group, index, groups):
    queue = deque([v])
    station_group[v] = index
    components = []
    heapq.heappush(components, v)

    while queue:
        st = queue.popleft()
        for next_st in graph[st]:
            if next_st in station_group:
                continue
            station_group[next_st] = index
            queue.append(next_st)
            heapq.heappush(components, next_st)

    groups[index] = components


def processQueries(c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
    station_group = {}
    groups = defaultdict(list)
    is_online = [True] * (c + 1)
    result = []

    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    index = 0

    for v in graph:
        if v in station_group:
            continue
        form_groups(graph, v, station_group, index, groups)
        index += 1

    for action, v in queries:
        if action == 2:
            is_online[v] = False

        elif action == 1:
            if is_online[v]:
                result.append(v)
            elif v not in station_group:
                result.append(-1)
            else:
                group = station_group[v]
                valid_station = -1

                while groups[group]:
                    station = groups[group][0]
                    if is_online[station]:
                        valid_station = station
                        break
                    else:
                        heapq.heappop(groups[group])

                result.append(valid_station)

    return result