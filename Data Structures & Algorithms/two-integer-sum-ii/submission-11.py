class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1 
        #return indexes 
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]#+1 because questions wants 1-indexed answers
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        return []