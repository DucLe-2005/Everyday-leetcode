class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # if get buy order, want to match smallest sell order
        # if get sell order, want to match largest buy order
        buy_orders = [] # max heap, (price, amount)
        sell_orders = [] # min heap, (price, amount)

        for price, amount, order_type in orders:
            if order_type == 0: # buy
                while sell_orders and sell_orders[0][0] <= price and amount:
                    sell_price, sell_amount = heapq.heappop(sell_orders)

                    matched = min(amount, sell_amount)
                    amount -= matched
                    sell_amount -= matched

                    if sell_amount > 0:
                        heapq.heappush(sell_orders, (sell_price, sell_amount))
                if amount:
                    heapq.heappush(buy_orders, (-price, amount))
            else: # sell
                while buy_orders and -buy_orders[0][0] >= price and amount:
                    neg_buy_price, buy_amount = heapq.heappop(buy_orders)

                    matched = min(amount, buy_amount)
                    amount -= matched
                    buy_amount -= matched

                    if buy_amount:
                        heapq.heappush(buy_orders, (neg_buy_price, buy_amount))
                if amount:
                    heapq.heappush(sell_orders, (price, amount))
        
        total = 0

        for _, amount in buy_orders:
            total += amount
        for _, amount in sell_orders:
            total += amount
        
        return total % (10**9 + 7)