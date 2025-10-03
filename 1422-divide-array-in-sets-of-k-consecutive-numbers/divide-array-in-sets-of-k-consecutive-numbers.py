class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)

        sorted_nums = sorted(counts.keys())

        queue = deque()
        current_groups = 0
        last_num = -1

        for current_num in sorted_nums:
            if (current_groups > 0 and current_num > last_num + 1) or (counts[current_num] < current_groups):
                return False
            
            queue.append(counts[current_num] - current_groups)
            current_groups = counts[current_num]
            last_num = current_num

            if len(queue) == k:
                current_groups -= queue.popleft()
            
        return current_groups == 0
