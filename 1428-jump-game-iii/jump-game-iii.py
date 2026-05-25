class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # use bfs spanning out from arr[start]
        # use a set to record visited numbers to avoid revisiting
        # time: O(n)
        # space: O(n)

        q = deque([start])
        visited = set()  
        while q:
            pop = q.popleft()
            if arr[pop] == 0:
                return True
            
            right = pop + arr[pop]
            if right < len(arr) and right not in visited:
                q.append(right)
                visited.add(right)

            left = pop - arr[pop]
            if left >= 0 and left not in visited:
                q.append(left)
                visited.add(left)
            
        return False