class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0 #return value, max amouunt of profit possible

        left = 0
        
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right

            currP = prices[right] - prices[left]
            maxP = max(maxP,currP)  
            right += 1          

            
            
        
        return maxP 