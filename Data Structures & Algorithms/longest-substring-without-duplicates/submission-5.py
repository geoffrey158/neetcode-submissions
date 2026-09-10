class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0 

        max_len = 1 #return value 

        hashset = set()#keep track of current characters 

        left = 0
        for right in range(len(s)):            
            #if left and right are the same character 
            while s[right] in hashset:
                hashset.remove(s[left])#remove duplicate from hashset 
                left += 1 #move the left pointer until the duplicate character is gone

            hashset.add(s[right]) #adds the unduplicate character to the hashset 
            max_len = max(max_len,right-left+1)#right-left+1 because we want the length of the substring 

        return max_len
