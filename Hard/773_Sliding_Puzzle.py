from typing import List
from collections import deque


def slidingPuzzle(board: List[List[int]]) -> int:
    adjacent_cells = {(0, 0): [(0, 1), (1, 0)],
                      (0, 1): [(0, 0), (0, 2), (1, 1)],
                      (0, 2): [(0, 1), (1, 2)],
                      (1, 0): [(1, 1), (0, 0)],
                      (1, 1): [(1, 0), (1, 2), (0, 1)],
                      (1, 2): [(0, 2), (1, 1)]}


    if 0 in board[0]:
        start_row = 0
        start_col = board[0].index(0)
    else:
        start_row = 1
        start_col = board[1].index(0)

    seen_states = set()
    start_state = tuple([tuple(row) for row in board])
    seen_states.add(start_state)
    steps = 0

    queue = deque([[start_state, start_row, start_col]])

    while queue:

        for _ in range(len(queue)):
            state, row, col = queue.popleft()

            if state == ((1, 2, 3), (4, 5, 0)):
                return steps

            state = list(state)
            current_board = [list(row) for row in state]

            for row2, col2 in adjacent_cells[(row, col)]:
                current_board[row][col], current_board[row2][col2] = current_board[row2][col2], current_board[row][col]

                new_state = tuple([tuple(row) for row in current_board])

                current_board[row][col], current_board[row2][col2] = current_board[row2][col2], current_board[row][col]

                if new_state in seen_states:
                    continue

                seen_states.add(new_state)
                queue.append([new_state, row2, col2])

        steps += 1

    return -1