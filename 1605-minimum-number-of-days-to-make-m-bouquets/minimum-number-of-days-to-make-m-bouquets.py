class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            bouquets = self.get_num_of_bouquets(bloomDay, mid, k)
            
            if bouquets < m:
                l = mid + 1
            else:
                r = mid
        
        return l
    
    def get_num_of_bouquets(self, bloomDay, mid, k):
        num_of_bouquets = 0
        count = 0

        for day in bloomDay:
            if day <= mid:
                count += 1
            else:
                count = 0
            
            if count == k:
                num_of_bouquets += 1
                count = 0
        
        return num_of_bouquets
