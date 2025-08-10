class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # make a array of start/end points
        # traverse the array, keep track of the brightness
        d = collections.defaultdict(int)
        for i, dis in lights:
            d[i - dis] += 1
            d[i + dis + 1] -= 1
        
        max_val, max_idx, cur = - sys.maxsize, 0, 0
        for idx, val in sorted(d.items()):
            cur += val
            if cur > max_val:
                max_val = cur
                max_idx = idx

        return max_idx


