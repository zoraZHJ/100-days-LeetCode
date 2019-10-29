class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        profit = 0
        ascend_order = False
        buy = prices[0]
        pre_price = buy
        for price in prices:
            if price >= pre_price:
                ascend_order = True
            elif price < pre_price:
                ascend_order = False
                profit = profit + (pre_price - buy)
                buy = price
            pre_price = price

        if ascend_order:
            profit = profit + (pre_price - buy)
            
        return profit