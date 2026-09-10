class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0 #return value, long sequence with character replacement k 
        maxf = 0 #the character that appears the most in s 
        left = 0 #one side of sliding window 
        count = {} #use to store the frequency of each character 

        #sliding window st
        for right in range(len(s)):

            #increase the count of character in the hashmap as we slide the window to the right 
            count[s[right]] = 1 + count.get(s[right],0)
            maxf = max(maxf,count[s[right]]) #check to see if we need to update the maxfrequency variable 

            while(right-left+1) - maxf > k:
                count[s[left]] -= 1 
                left += 1 
            res = max(res, right-left+1)
        
        return res 


