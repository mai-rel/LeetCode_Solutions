from typing import List
from collections import deque, Counter


def watchedVideosByFriends(watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[
    str]:
    queue = deque([id])
    seen = set()
    seen.add(id)

    while level > 0:

        for _ in range(len(queue)):
            friend_id = queue.popleft()
            for next_friend_id in friends[friend_id]:
                if next_friend_id in seen:
                    continue

                seen.add(next_friend_id)
                queue.append(next_friend_id)

        level -= 1

    videos = Counter()

    while queue:
        friend_id = queue.popleft()
        for video in watchedVideos[friend_id]:
            videos[video] += 1

    result = [video for video, _ in sorted(videos.items(), key=lambda x: (x[1], x[0]))]
    
    return result