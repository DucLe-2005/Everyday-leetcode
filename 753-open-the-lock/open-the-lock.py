class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited: 
            return -1
        
        res = 0
        queue = deque([('0000', 0)])
        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves

            for i in range(4):
                digit = int(state[i])
                new_digit = (digit - 1) % 10
                new_state = state[0:i] + str(new_digit) + state[i+1:]

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
                
                new_digit = (digit + 1) % 10
                new_state = state[0:i] + str(new_digit) + state[i+1:]

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        
        return -1
            



