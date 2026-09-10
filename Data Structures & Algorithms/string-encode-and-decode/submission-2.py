class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
             #use a delimiter so it can be used for decoding 
             #so if the word is song, it gets encoded as 4#song
            res += str(len(char)) + "#" + char
        return res

    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0 
        
        while i < len(s):
            j = i #use it as counter until we find the first delimiter # 

            while s[j] != '#':
                j += 1 
            
            length = int(s[i:j]) #number before the delimiter to tell how long the string is 
            i = j + 1 #we change i to the first character after the delimiter #
            j = i + length #we change j to the first character + length that was encoded before delimiter
            res.append(s[i:j]) #splice and add it to the resulting list 
            i = j #reset and do it over again 

        return res 

