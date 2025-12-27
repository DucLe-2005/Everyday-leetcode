class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0 and stack[-1] < -a:  # Smaller one explodes
                    stack.pop()

                if stack and stack[-1] == -a:  # Both are same size
                    stack.pop()
                    continue
                
                if not stack or stack[-1] < 0:
                    stack.append(a)
            else:
                stack.append(a)

        return stack
