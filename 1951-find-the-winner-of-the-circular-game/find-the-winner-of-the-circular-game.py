class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # queue: [1, ...., n]
        # while queue has more than 1 element:
        # for k - 1 times:
        # pop from queue and push to queue
        # the first node in queue is eliminated
        # time: O(n * k)
        # space: O(n)

        q = deque([x for x in range(1, n+1)])
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        
        return q[0]

