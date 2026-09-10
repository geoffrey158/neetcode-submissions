class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = [] 

        for t in tokens:

            if t == "+":
                stack.append(stack.pop()+stack.pop())
            
            elif t == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)

            elif t == "*":
                stack.append(stack.pop()*stack.pop())

            elif t == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
                #truncate towards 0, can't use // because it's floor divions towards negative infinity 
                #if we use int(), we remove decimal, moving it towards 0 
            else:
                stack.append(int(t))

        return stack.pop()

        
        