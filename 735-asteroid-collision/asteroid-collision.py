class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if not stack or x > 0:
                stack.append(x)
            else:
                # remove asteroids moving right that are smaller than x
                while stack and stack[-1] > 0 and stack[-1] < -x:
                    stack.pop()

                if not stack or stack[-1] < 0: # all go left
                    stack.append(x)
                elif stack[-1] == -x: # right = left
                    stack.pop()
                
        return stack


                    