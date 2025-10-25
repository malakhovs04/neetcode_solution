<<<<<<< HEAD
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n: 
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
=======
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n: 
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
        return res