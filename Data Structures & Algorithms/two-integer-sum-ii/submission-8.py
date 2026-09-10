class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #sorted array - numbers
        left = 0 
        right = len(numbers) - 1 
        
        while left < right:
            
            currSum = numbers[left] + numbers[right]

            if currSum > target: #if current sum is greater than target we need to move the right pointer to the left and recalculate 
                right -= 1 
            elif currSum < target: #if current sum is less than target we need to move the left pointer to the right and recalculate
                left += 1 
            else:
                return [left+1,right+1] #Increment left and right by 1 because we need to return the index of the array
        
        #Time complexity: O(n), Input array travesed at most once
        #Space complexity: O(1), We only use additional space to store two indices and the sum
            
            