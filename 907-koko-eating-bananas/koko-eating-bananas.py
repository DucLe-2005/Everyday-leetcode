class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = 1
        # ans = max(piles)
        # for k in range(1, max(piles)+1):
        #     cur_h = 0
        #     for p in piles:
        #         cur_h += ceil(p/k)
        #         if cur_h > h:
        #             break
        #     if cur_h <= h:
        #         ans = min(ans, k)
        # return ans

        l, r = 1, max(piles)
        ans = max(piles)

        while l <= r:
            mid = (l+r)//2
            cur_h = sum(ceil(p/mid) for p in piles)

            if cur_h <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans        
