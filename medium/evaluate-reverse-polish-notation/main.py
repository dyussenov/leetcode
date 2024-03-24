from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"*", "-", "+", "/"}

        for i in tokens:
            print(stack)
            if len(i) > 1 or i not in operators:
                stack.append(int(i))
            else:
                operands = (stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                if i == "+":
                    stack.append(sum(operands))
                elif i == "-":
                    stack.append(operands[0] - operands[1])
                elif i == "*":
                    stack.append(operands[0] * operands[1])
                else:
                    stack.append(int(operands[0] / operands[1]))

        return stack[0]


# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["2","1","+","3","*"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
r = Solution()
print(r.evalRPN(tokens))
