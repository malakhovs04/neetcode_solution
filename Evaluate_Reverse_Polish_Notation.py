<<<<<<< HEAD
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens: 
            if token in {'+','-','*','/'}:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)
                
                stack.append(res)

            else:
                stack.append(int(token))
                
=======
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens: 
            if token in {'+','-','*','/'}:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)
                
                stack.append(res)

            else:
                stack.append(int(token))
                
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
        return stack[0]