class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr) 
        currMax = -1 #store the current max value 
        #thought process:find the greatest element first then make everything to the left that number 
        #start in reverse order
        #last element is always -1 
        for i in range(len(arr)-1,-1,-1):
            #assign value to return list 
            res[i] = currMax
            #update the current max value 
            currMax = max(currMax,arr[i])

        
        return res