class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {} #keep track of the # of characters 

        res = 0 # return value
        
        freq = 0 #keep track of most frequent element 
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            freq = max(freq, count[s[right]])
            
            while (right-left+1) - freq > k:
                count[s[left]] -= 1
                left += 1 
            
            res = max(res,right-left+1)
        return res 



