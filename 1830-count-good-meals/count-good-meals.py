class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        food_map = defaultdict(int)

        for val in deliciousness:
            food_map[val] += 1
        
        res = 0
        for a in food_map:
            for power in range(0, 22):
                b = 2**power - a
                if b == a:
                    res += food_map[a] * (food_map[a] - 1) // 2
                
                elif b in food_map and b > a:
                    res += food_map[a] * food_map[b]\

        return res % (10**9 + 7)