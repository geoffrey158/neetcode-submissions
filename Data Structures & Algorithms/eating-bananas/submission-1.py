class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #number of hours you have to eat all the bananas 

        #binary search eating rate or hours

        left = 1 #the minimum bananas that can be eaten 
        right = max(piles) #the maxmium bananas that can be eaten 
        minspeed = right #return value, start at the maximum bananas 

        while left <= right: 
            mid = left + (right-left)//2 
            
            #represents the totaltime it takes to eat all the piles
            totalTime = 0 
            #iterate through the piles to see how long it takes to eat all the piles 
            for p in piles: 
                totalTime += math.ceil(float(p)/mid)

            #if the calculated total time is less than h, we update the minspeed 
            if totalTime <= h:
                minspeed = mid 
                right = mid - 1 
            else:
                left = mid + 1 
        
        return minspeed 

#Time complexity: O(n*logm) since we used binary search, and used a for loop to get the total time in piles everytime
#Space complexity: O(1)
             