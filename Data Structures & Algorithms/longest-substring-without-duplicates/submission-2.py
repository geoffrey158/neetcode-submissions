class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0 #longest without duplicate character - length, return value

        left = 0
        hashset = set()

        for right in range(len(s)):
            
            #if a duplicate character is found 
            while s[right] in hashset:
                #move left pointer to get rid of duplicate character 
                hashset.remove(s[left])
                left += 1
                    
            res = max(res,right-left+1)
            hashset.add(s[right])
        
        return res
                
                


