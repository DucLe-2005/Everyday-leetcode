class Solution:
    def climbStairs(self, n: int) -> int:
        # climb1 -> climb2 -> ...

        climb1, climb2 = 0, 1
        for _ in range(n):
            new_climb = climb1 + climb2
            climb1 = climb2
            climb2 = new_climb
        
        return climb2