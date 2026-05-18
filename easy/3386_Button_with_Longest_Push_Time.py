from typing import List


def buttonWithLongestTime(events: List[List[int]]) -> int:
    button, max_time = events[0]

    for i in range(1, len(events)):
        number, time = events[i]
        _, prev_time = events[i - 1]

        time_press = time - prev_time
        if time_press > max_time:
            max_time = time_press
            button = number
        elif time_press == max_time:
            button = min(button, number)

    return button