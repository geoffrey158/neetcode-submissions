class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        left = 0
        count = {} #count frequency of elements

        maxf = 0 #used to keep track of the most frequent element in the substring
        for right in range(len(s)):
            count[s[right]] = 1+ count.get(s[right],0)
            maxf = max(maxf, count[s[right]]) #keep track of the most frequent element in the substring
            
            #(right - left + 1) - freq > k, if the current substring minus most frequent element is greater than k
            #the susbtring doesn't have enough ks to replace, we shrink from the left until substring is valid 
            while(right-left+1) - maxf > k:
                count[s[left]] -= 1
                left += 1 
            
            res = max(res,right-left+1)

        return res            