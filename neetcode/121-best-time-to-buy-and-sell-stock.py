# problem url - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## first try 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left,right = 0, 1 # left=buy , right=sell
        # right = left+1
        size_of_list = len(prices) -1
        if size_of_list == 0:
            return 0
        max_profit = 0
        buy, sell = prices[left], prices[right]    
        profit = sell - buy
        index = 0
        while index <= size_of_list:
            
            if profit < 0 and right +1<= size_of_list:
                if right - left > 1:
                    left=right
                    right+=1
                else:
                    left+=1
                    right+=1
                
            if profit >= 0 and right +1  <= size_of_list:
                right+=1
                sell = prices[right]  
            
            if max_profit == 0 and int(profit) >= 0:
                max_profit = profit
            if profit > max_profit:
                max_profit = profit            
            
            buy, sell = prices[left], prices[right]    
            profit = sell - buy

            index +=1
        return max_profit
        
## second way - need to understand more 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res
