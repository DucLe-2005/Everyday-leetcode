class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # time: O(nlogn) , O(nlogn + min(n,k)logn)
        # space: O(n)
        
        capital_heap = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(capital_heap)
        
        total_capital = w
        profit_heap = []

        while k > 0:
            # Process all projects that can be initiated
            while capital_heap and capital_heap[0][0] <= total_capital:
                _, profit = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, -profit)

            if not profit_heap:
                break
            
            total_capital += -heapq.heappop(profit_heap)
            k -= 1
        
        return total_capital
            
