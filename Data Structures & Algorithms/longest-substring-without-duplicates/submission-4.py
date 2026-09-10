class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0 

        max_len = 1 #return value 

        hashset = set()#keep track of current characters 
        hashset.add(s[0])#adds first element to hashset 
        left = 0
        for right in range(1,len(s)):            
            #if left and right are the same character 
            if s[right] in hashset:
                while s[right] in hashset:
                    hashset.remove(s[left])
                    left += 1 #move the left pointer until the duplicate character is gone

            #if left and right are not the same character
            
            hashset.add(s[right])
            max_len = max(max_len,right-left+1)

        return max_len
