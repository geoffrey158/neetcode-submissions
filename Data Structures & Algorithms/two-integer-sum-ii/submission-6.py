class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1 

        while left < right:

            currSum = numbers[left] + numbers[right] 

            if currSum == target: 
                #left+1 and right+1 bc it wants us to return the indices(1-indexed) of the two numbers 
                return [left+1,right+1] 
            elif currSum > target:
                right -= 1 
            elif currSum < target:
                left += 1 
            
    #Time complexity:O(n)
    #Space complexity:O(1)



            


        


        