class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxA = 0 #return value maximum amount of water 

        left = 0 
        right = len(heights)-1


        while left <= right:
            currA = min(heights[left],heights[right]) * (right-left)

            maxA = max(currA,maxA)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1 

        return maxA  