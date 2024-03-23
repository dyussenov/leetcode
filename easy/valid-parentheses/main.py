"""Related topics:String, Stack"""


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = []
        if len(s) % 2 == 1:
            return False
        for symbol in s:
            if symbol in parentheses:
                if len(stack) > 0 and parentheses[symbol] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return True if not stack else False


case_1 = "}}"
r = Solution()
print(r.isValid(case_1))
