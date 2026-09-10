class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxA = 0 #return value 

        left = 0 
        right = len(heights)-1

        while left < right:
            
            #area = length x height
            #we can only use the smallest height otherwise water overflows 
            currA = min(heights[left],heights[right]) * (right-left)
            maxA = max(maxA,currA)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxA 