class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # time: O(nlogn)
        # space: O(n)

        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1
        
        min_list = [key for key in count.keys()]
        heapq.heapify(min_list)

        while min_list:
            first = min_list[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_list[0]: # there's a hole
                        return False
                    heapq.heappop(min_list)
        
        return True