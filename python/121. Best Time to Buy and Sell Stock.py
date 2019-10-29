class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        min_pre = [prices[0]]
        for num in prices[1:]:
            if num < min_pre[-1]:
                min_pre.append(num)
            else:
                min_pre.append(min_pre[-1])
        max_gap = -1
        for num, min_v in zip(prices, min_pre):
            max_gap = (num - min_v) if (num - min_v) > max_gap else max_gap
        max_gap = max_gap if max_gap >= 0 else 0
        return max_gap