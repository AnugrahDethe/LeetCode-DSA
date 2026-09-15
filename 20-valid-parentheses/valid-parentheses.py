class Solution:
    def isValid(self, s):
        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            if char in '([{':
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack.pop() != brackets[char]:
                    return False

        return len(stack) == 0