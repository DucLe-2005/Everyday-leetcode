from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if n == 1:
            return True
        elif s[n-1]==1:
            return False

        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    q.append(j)

            farthest = max(farthest, i + maxJump)

        return False