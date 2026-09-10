class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = [] #stack to keep track of operations 
        res = 0 #return value, keeps track of total score  

        
        #iterate through the operations list
        for i in operations: 

            if i == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2]) #adds the sum of the previous two scores, last two elements in a stack
            elif i == "D":
                res += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif i == "C":
                res -= stack.pop()#remove the previous score from the record 
    
            else:
                res += int(i)
                stack.append(int(i))
                
        
        return res 