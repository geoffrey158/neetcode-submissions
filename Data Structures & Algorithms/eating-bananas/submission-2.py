class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        left = 1 #slowest eating speed possible 
        right = max(piles) #fastest eating speed possible
        res = right #slowest possible eating speed koko can eat 

        while left <= right:
            mid = left + (right-left)//2

            #see if mid eating speed is valid or not
            currSum = 0  
            for i in range(len(piles)):
                currSum += math.ceil(piles[i]/mid)
            
            #not a valid speed, have to eat faster 
            if currSum > h:
                left = mid + 1
            else: #valid eating speed, continue to check to see if there is a better eating speed
                res = mid
                right = mid - 1 
            

        
        return res 