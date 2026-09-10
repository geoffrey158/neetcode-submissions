class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height)-1 
        leftMax = height[left]
        rightMax = height[right]

        currSum = 0 #return value 
        while left < right:
            
            if leftMax < rightMax:
                left += 1 
                leftMax = max(leftMax,height[left])
                currSum += leftMax - height[left]
            
            else: #leftMax > rightMax
                right -=1
                rightMax = max(rightMax,height[right])
                currSum += rightMax - height[right]
        
        return currSum

