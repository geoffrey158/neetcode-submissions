class Solution(object):
    def isValid(self, s):

        #The stack to keep track of opening brackets
        stack = [] 

        #Hashmap for keeping track of mappings between opened and closed brackets
        Map = {")":"(","}":"{","]":"["}

        #iterate through every bracket in s 
        for char in s:
            #if the character is a closing bracket, every key is a closing bracket
            if char in Map: 
            #if stack is not empty and value at the top is matching opening bracket 
            #stack[-1], last value added in the stack
                if stack and stack[-1] == Map[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)

        #Return true if stack is empty
        #Return false if stack is not empty 
        if not stack:
            return True
        else:
            return False

	#Time Complexity:O(n),going through every input character once 
	#Space Complexity:O(n),using a stack
