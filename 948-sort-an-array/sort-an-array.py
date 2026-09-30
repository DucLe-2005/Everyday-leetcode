import random

class Solution:
    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

    def randomized_quicksort(self, nums, lo, hi):
        if lo >= hi:
            return

        lt, gt = self.partition_three_way(nums, lo, hi)

        # Equal region is already sorted
        self.randomized_quicksort(nums, lo, lt - 1)
        self.randomized_quicksort(nums, gt + 1, hi)

    def partition_three_way(self, nums, lo, hi):
        p = random.randint(lo, hi)

        # Move pivot to nums[lo]
        nums[lo], nums[p] = nums[p], nums[lo]
        pivot = nums[lo]

        lt = lo
        i = lo
        gt = hi

        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1

            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1

            else:
                i += 1

        return lt, gt