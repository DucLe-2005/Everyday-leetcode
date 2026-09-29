class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # time: O(nlogn)
        # space: O(n)
        buy_orders = []
        sell_orders = []

        for price, amount, t in orders:
            if t == 0: # buy
                while amount > 0 and sell_orders and sell_orders[0][0] <= price:
                    sell_price, available = heapq.heappop(sell_orders)

                    matched = min(available, amount)
                    
                    available -= matched
                    amount -= matched

                    if available > 0:
                        heapq.heappush(sell_orders, (sell_price, available))
                
                if amount > 0:
                    heapq.heappush(buy_orders, (-price, amount))
            else:
                while amount > 0 and buy_orders and -buy_orders[0][0] >= price:
                    neg_buy_price, available = heapq.heappop(buy_orders)
                    
                    matched = min(available, amount)

                    available -= matched
                    amount -= matched

                    if available > 0:
                        heapq.heappush(buy_orders, (neg_buy_price, available))
                
                if amount > 0:
                    heapq.heappush(sell_orders, (price, amount))
        
        return (sum(x for _, x in sell_orders) + sum(x for _, x in buy_orders)) % (10**9 + 7)