class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time: O(n)
        # space: O(1)

        fleets = 0
        current_fleet_time = 0
        for pos, s in sorted(zip(position, speed), key=lambda x: x[0], reverse=True):
            time = (target - pos) / s
            if time > current_fleet_time:
                fleets += 1
                current_fleet_time = time

        return fleets            
        