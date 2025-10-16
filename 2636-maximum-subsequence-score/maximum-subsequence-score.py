class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 1. sort [nums1[i], nums2[i]] in decreasing order
        # 2. iterate over every nums2[i] and treat it as minimum in the selected group; we can freely choose k from nums1[0:i+1] (including nums1[i]) 
        # 3. use a heap to store the top k elements from nums1 for the current selected group


        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x : -x[1])

        top_k_elements = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_elements)
        heapq.heapify(top_k_elements)

        res = top_k_sum * pairs[k - 1][1]

        # start at kth pair
        for n1, n2 in pairs[k:]:
            top_k_sum = top_k_sum - heapq.heappop(top_k_elements) + n1
            heapq.heappush(top_k_elements, n1)
            res = max(res, top_k_sum * n2)
        
        return res
        
    



