def max_heapify(a, i, n):
    while 2*i + 1 < n:
        left, right = 2*i + 1, 2*i + 2
        
        child = left
        if right < n and a[right] > a[left]: 
            child = right
        if a[i] >= a[child]: 
            return
        
        a[i], a[child] = a[child], a[i]
        i = child

def build_max_heap(a):
    n = len(a)
    for i in range(n // 2 -1, -1, -1):
        max_heapify(a, i, n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        build_max_heap(nums)
        i = len(nums) - 1

        for _ in range(k - 1):
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            max_heapify(nums, 0, i+1)

        return nums[0]