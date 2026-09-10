class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        chars = {'}':'{',']':'[',')':'('} #combination of parenthesis 

        #iterate through each character of string 
        for c in s:
            
            #if the character is a closing bracket 
            if c in chars:
                #if the closing bracket does not match 
                if not stack or stack[-1] != chars[c]:
                    return False 
                else:
                    stack.pop()
            else:
                stack.append(c)

        
        return len(stack)== 0

