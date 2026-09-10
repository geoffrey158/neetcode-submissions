class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        #str(lens) + "#" is used as a delimiter, tells you number of characters to decode after the delimiter #, ie. 4#

        return ans
        

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 #used as counter while iterating 

        while i < len(s):
            j = i 
            while s[j] != '#': #loops until we reach the end of integer 
                j += 1 
            length = int(s[i:j]) #length of each word, the number before the # delimiter 

            i = j + 1 #starting position, index after the # delimiter 
            j = i + length #ending position, starting position + length of string 
            ans.append(s[i:j]) #adds the word into the ans list 
            i = j #move i to j to check for more words and for while condition 

        return ans  
            
            