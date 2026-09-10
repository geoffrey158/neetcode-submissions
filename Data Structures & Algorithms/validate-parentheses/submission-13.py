class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}':'{',']':'[',')':'('} #combination of parenthesis 

        for c in s:
            if c in hashmap:
                
                #if the stack empty or the closing bracket does not match the top element 
                if not stack or stack[-1] != hashmap[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

    

        return not stack