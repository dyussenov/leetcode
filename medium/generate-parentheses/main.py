from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def addParenthese(opened: int, closed: int) -> None:
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened > closed:
                stack.append(")")
                addParenthese(opened, closed + 1)
                stack.pop()

            if opened < n:
                stack.append("(")
                addParenthese(opened + 1, closed)
                stack.pop()

        addParenthese(0, 0)
        return res


n = 9
r = Solution()
print(r.generateParenthesis(n))
