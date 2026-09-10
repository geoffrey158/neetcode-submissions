class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0 #return value, max amouunt of profit possible

        left = 0
        
        for right in range(len(prices)):
            if prices[left] > prices[right]: #buy price is higher than sell price
                left = right
            else: #calculate current profit and see if it's the max amount of profit possible
                currP = prices[right] - prices[left]
                maxP = max(maxP,currP)  
            
            right += 1          

            
            
        
        return maxP 