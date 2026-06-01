class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = len(fruits)
        used_baskets = set()
        for fruit in fruits:
            for i in range(len(baskets)):
                if i not in used_baskets and baskets[i] >= fruit:
                    used_baskets.add(i)
                    res -= 1
                    break
        
        return res
