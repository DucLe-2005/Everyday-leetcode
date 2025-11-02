class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[1, 2], [2, 1], [-1, 2], [2, -1], [-2, 1], [1, -2], [-1, -2], [-2, -1]]
        
        target_q = deque([(x, y, 0)])  # x, y, distance from target
        target_map = {(x, y): 0}  # (x, y): distance

        origin_q = deque([(0, 0, 0)])  # 0, 0, distance from origin
        origin_map = {(0, 0): 0}  # (x, y): distance

        while True:
            origin_x, origin_y, origin_d = origin_q.popleft()
            if (origin_x, origin_y) in target_map:
                return origin_d + target_map[(origin_x, origin_y)]
            
            target_x, target_y, target_d = target_q.popleft()
            if (target_x, target_y) in origin_map:
                return target_d + origin_map[(target_x, target_y)]
            
            # origin's bfs
            for dx, dy in directions:
                nx, ny = origin_x + dx, origin_y + dy
                new_d = origin_d + 1
                if (nx, ny) not in origin_map:
                    origin_map[(nx, ny)] = new_d
                    origin_q.append((nx, ny, new_d))

                # target's bfs
                nx, ny = target_x + dx, target_y + dy
                new_d = target_d + 1
                if (nx, ny) not in target_map:
                    target_map[(nx, ny)] = new_d
                    target_q.append((nx, ny, new_d))

