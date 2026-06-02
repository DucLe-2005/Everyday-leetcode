class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # if start1 > end2: move slot2 forward
        # if start2 > end1: move slot1 forward
        # else calculate overlaps
        # time: O(n log n + m log m)
        # space: O(1)
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):

            start1, end1 = slots1[i][0], slots1[i][1]
            start2, end2 = slots2[j][0], slots2[j][1]

            if start1 >= end2:
                j += 1
            elif start2 >= end1:
                i += 1
            else:
                end = min(end1, end2)
                start = max(start1, start2)
                if end - start >= duration:
                    return [start, start + duration]
                elif end1 > end2:
                    j += 1
                else:
                    i += 1
        
        return []
