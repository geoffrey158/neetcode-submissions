class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #keep track of longest substring/also the result 
        res = 0 
        left = 0 
        #use hashmap to keep track of duplicates
        mp = {} 

        for right in range(len(s)):

            #If a duplicate is found, update left to our stored next valid position
            if s[right] in mp: 
                left = max(mp[s[right]]+1, left)
            
            res = max(res, right-left+1)
            #Store the next index for this character, as this will be the next valid position to de-duplicate
            mp[s[right]] = right

        return res

        #Time complexity: O(n)
        #Space complexity: O(m)

        
        