from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead or target in dead:
            return -1

        if target == "0000":
            return 0

        start_q = deque(["0000"])
        end_q = deque([target])

        # state -> distance from that side
        start_dist = {"0000": 0}
        end_dist = {target: 0}

        while start_q and end_q:
            # Expand the smaller frontier for better performance.
            if len(start_q) <= len(end_q):
                result = self.expand(
                    start_q,
                    start_dist,
                    end_dist,
                    dead
                )
            else:
                result = self.expand(
                    end_q,
                    end_dist,
                    start_dist,
                    dead
                )

            if result != -1:
                return result

        return -1

    def expand(
        self,
        queue: deque,
        current_dist: dict[str, int],
        other_dist: dict[str, int],
        dead: set[str]
    ) -> int:
        # Expand exactly one BFS level.
        for _ in range(len(queue)):
            state = queue.popleft()
            moves = current_dist[state]

            for i in range(4):
                digit = int(state[i])

                for change in (-1, 1):
                    new_digit = (digit + change) % 10
                    neighbor = (
                        state[:i]
                        + str(new_digit)
                        + state[i + 1:]
                    )

                    if neighbor in dead or neighbor in current_dist:
                        continue

                    current_dist[neighbor] = moves + 1

                    if neighbor in other_dist:
                        return (
                            current_dist[neighbor]
                            + other_dist[neighbor]
                        )

                    queue.append(neighbor)

        return -1