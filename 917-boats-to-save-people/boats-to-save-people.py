class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # time: O(nlogn)
        # space: O(n)
        res = 0
        low, high = 0, len(people) - 1
        people.sort()
        while low <= high:
            if people[low] + people[high] <= limit:
                low += 1
                high -= 1
            else:
                high -= 1
            res += 1
        
        return res