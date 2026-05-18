from collections import deque


def findLexSmallestString(s: str, a: int, b: int) -> str:
    result = s
    seen = set()
    seen.add(s)
    queue = deque([s])
    n = len(s)

    while queue:
        st = queue.popleft()
        st1 = st[b:] + st[:b]
        st2 = list(st)

        for i in range(1, n, 2):
            value = (int(st2[i]) + a) % 10
            st2[i] = str(value)

        st2 = ''.join(st2)

        for new_s in [st1, st2]:
            if new_s in seen:
                continue
            result = min(result, new_s)
            seen.add(new_s)
            queue.append(new_s)

    return result

