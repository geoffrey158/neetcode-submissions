class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        right = 1

        maxProfit = 0

        while right < len(prices):
            #If the buy price is lower than sell price, guarantee profit, keep track of maxProfit overall
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit,currProfit) 
            else:
                left = right
            right += 1 

        return maxProfit 